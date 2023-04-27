#!/bin/bash

set -eE

. ./scripts/common.sh

which mach > /dev/null 2>&1 || error_die "'mach' not found. Is it in your path?"

ACTIONS="$*"

# shellcheck disable=SC2086
mach tb-l10n-quarantine-to-strings -q "$QUARANTINE_PATH" -l "$STRINGS_PATH" $ACTIONS

hack_hgrc "$STRINGS_PATH"/.hg/hgrc

exit 0

### Remainder of script is the original shell version of quarantine-to-strings
### kept here for posterity.

exit 1

FILEMAP="/tmp/filemap.txt"
SPLICEMAP="/tmp/splicemap.txt"


write_filemap() {
  cat - > $FILEMAP << _EOF_
exclude _configs
rename . en-US
_EOF_
}

write_splicemap() {
  _first_to_convert="$1"
  _tip_of_prev_history="$2"
  if [[ -z "${_first_to_convert}" || -z "${_tip_of_prev_history}" ]]; then
    echo "write_splicemap() didn't receive the right arguments."
    die 6
  fi
  echo "${_first_to_convert} ${_tip_of_prev_history}" > $SPLICEMAP
}

update_string_from_quarantine() {
  _qtine="$1"
  _strings="$2"
  
  echo "Updating to strings tip"
  hg up -R "${STRINGS_PATH}" -r tip
  _current_tip=$(hg log -R "${STRINGS_PATH}" \
    -r . \
    --template '{node}\n')


  _last_convert_rev=$(hg log -R "${STRINGS_PATH}" \
    -r 'last(extra("convert_source", "comm-strings-quarantine"))' \
    --template '{get(extras,"convert_revision")}\n')
  if [[ -z "$_last_convert_rev" ]]; then
    _last_convert_rev="-1"
    _first_convert_rev=$(hg log -R "${QUARANTINE_PATH}" \
      -r 0 \
      --template '{node}\n')
  else
    _first_convert_rev=$(hg log -R "${QUARANTINE_PATH}" \
      -r "first(children(${_last_convert_rev}))" \
      --template '{node}\n')
  fi
  echo "last converted: ${_last_convert_rev}"
  echo "first to convert: ${_first_convert_rev}"

  write_splicemap "${_first_convert_rev}" "${_current_tip}"

  hg convert \
    --config convert.hg.saverev=True \
    --config convert.hg.sourcename="comm-strings-quarantine" \
    --config convert.hg.revs="${_first_convert_rev}:tip" \
    --filemap $FILEMAP \
    --splicemap $SPLICEMAP \
    --datesort \
    "${_qtine}" "${_strings}"

  hg up -R "${STRINGS_PATH}" -r tip
}


clone_repo "$QUARANTINE_URL" "$QUARANTINE_PATH"
clone_repo "$STRINGS_URL" "$STRINGS_PATH"

write_filemap

update_string_from_quarantine "$QUARANTINE_PATH" "$STRINGS_PATH"

# vim: set ts=2 sw=2 sts=2 et tw=80: #
