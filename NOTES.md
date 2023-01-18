# Running Fluent Migrations

**These notes are a work in progress and probably only make sense to the
individual who wrote them!**

venv activate at /home/rob/moz/fluent/venv/bin

## Testing

- `./scripts/quarantine-to-strings.sh`
  - (do not push)

- Need to adjust the `comm-strings-quarantine/_configs/*toml` files to not import m-c resources
    - `./scripts/munge_configs.py`

- Check es-MX
    - `./scripts/compare_locales_esMX.sh`

- Check that all locales work
    - `./scripts/migration.sh wet-run`


## Run migrations for real

- `./scripts/reset-repos.sh`
- Stop sync in Pontoon
- `./scripts/quarantine-to-strings.sh`
    - push to comm-l10n to update en-US
- `./scripts/migration.sh wet-run push`
- IF all went well (it should have) - enable Pontoon Sync again

## Problems?

During testing, might be useful to remove the `comm-l10n` and `comm-strings-quarantine` clones.

