#! /usr/bin/env bash

set -eE

. ./scripts/common.sh

compare-locales ${quarantine_path}/_configs/mail.toml ${l10n_clones_path} es-MX > /tmp/b4.txt
./scripts/migration.sh es-MX wet-run
compare-locales ${quarantine_path}/_configs/mail.toml ${l10n_clones_path} es-MX > /tmp/a4.txt

meld /tmp/b4.txt /tmp/a4.txt
