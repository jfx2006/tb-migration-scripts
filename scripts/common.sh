#! /usr/bin/env bash

script_path="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
root_path="$(dirname "${script_path}")"

. "${script_path}/../config/config"

function interrupt_code()
# This code runs if user hits control-c
{
  printf "\n*** Operation interrupted ***\n"
  exit $?
}

# Trap keyboard interrupt (control-c)
trap interrupt_code SIGINT

die() {
  if [[ -n "$1" ]]; then
    exit "$1"
  fi
  exit 1
}

error_die() {
  echo "$1"
  die 1
}

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

clone_repo() {
  _url="$1"
  _path="$2"

  if [[ -d "${_path}" && -d "${_path}/.hg" ]]; then
    hg -R "${_path}" pull -u
  else
    hg clone "${_url}" "${_path}"
    hack_hgrc "${_path}/.hg/hgrc"
  fi
}
