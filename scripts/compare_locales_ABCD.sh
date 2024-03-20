#! /usr/bin/env bash

set -eE

LANG="$1"
if [[ -z "$LANG" ]]; then
  echo "Defaulting to lang en-GB!"
  LANG="en-GB"
fi

. ./scripts/common.sh

compare-locales ${quarantine_path}/_configs/mail.toml ${l10n_clones_path} ${LANG} > /tmp/b4.txt
./scripts/migration.sh ${LANG} wet-run
compare-locales ${quarantine_path}/_configs/mail.toml ${l10n_clones_path} ${LANG} > /tmp/a4.txt

diffuse /tmp/b4.txt /tmp/a4.txt
