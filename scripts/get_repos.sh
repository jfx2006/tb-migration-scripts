#! /usr/bin/env bash

function interrupt_code()
# This code runs if user hits control-c
{
  printf "\n*** Operation interrupted ***\n"
  exit $?
}

# Trap keyboard interrupt (control-c)
trap interrupt_code SIGINT

script_path="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
root_path="$(dirname "${script_path}")"

hack_hgrc() {
  _rc="$1"
python - "${_rc}" << _EOF_
import sys
import configparser
file = sys.argv[1]
config = configparser.ConfigParser(delimiters=("=",))
config.read(file)
config["paths"]["default:pushurl"] = config["paths"]["default"].replace("https", "ssh")
with open(file, "w") as fp:
    config.write(fp)
_EOF_
}


# Pull from hg server
hg --cwd ${root_path}/ clone https://hg.mozilla.org/projects/comm-strings-quarantine
hack_hgrc "${root_path}/comm-strings-quarantine/.hg/hgrc"

# Pull from hg server
hg --cwd ${root_path}/ clone https://hg.mozilla.org/projects/comm-l10n
hack_hgrc "${root_path}/comm-l10n/.hg/hgrc"
