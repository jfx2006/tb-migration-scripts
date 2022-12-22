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


# Pull from hg server
hg --cwd ${root_path}/ clone https://hg.mozilla.org/projects/comm-strings-quarantine

# Pull from hg server
hg --cwd ${root_path}/ clone https://hg.mozilla.org/projects/comm-l10n
