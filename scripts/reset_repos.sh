#! /usr/bin/env bash

set -eE

. ./scripts/common.sh

rm -rf "$QUARANTINE_PATH" "$STRINGS_PATH"

clone_repo "$QUARANTINE_URL" "$QUARANTINE_PATH"
clone_repo "$STRINGS_URL" "$STRINGS_PATH"

