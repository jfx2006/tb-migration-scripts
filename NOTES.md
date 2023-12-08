# Running Fluent Migrations

**These notes are a work in progress and probably only make sense to the
individual who wrote them!**

## Setup

### mach

First, for `quarantine-to-strings.sh` to run, `mach` must be in your `$PATH`.
The easiest way to meet this requirement is to have a symlink named `mach` that
links to an up-to-date Thunderbird source directory (mozilla-central +
comm-central).

```sh
cd ~/bin
ln -s $GECKO/mach mach
```

### tb-fluent-migrate

The migration scripts should all be using `fluent.migratetb` now. If not, you
will have to change the imports at the top of the script.

Create a Python virtualenvironment somewhere easily accessible, activate, and
install `tb-fluent-migrate`.

```shell
python3 -m venv migrations_venv
source ./migrations_venv/bin/activate
# The quotes in the next line are important! 
pip install "fluent.migrate[hg] @ git+https://github.com/jfx2006/tb-fluent-migrate"
pip install tomlkit
```


# Running migrations

## Prep

- Copy recipies from a comm-central checkout to the recipes directory:
   `$ cp $topsrcdir/comm/python/l10n/tb_fluent_migrations/bug*.py recipes/`

## Testing

- `./scripts/quarantine-to-strings.sh clean prep migrate`
  - This script relies on a `mach` from you Thunderbird source checkout in $PATH.

- Need to adjust the `comm-strings-quarantine/_configs/*toml` files to not import m-c resources
    - `./scripts/munge_configs.py`

- Check es-MX
    - `./scripts/compare_locales_esMX.sh`

- Check that all locales work
    - `./scripts/migration.sh wet-run`


## Run migrations for real

- Stop sync in Pontoon
- Monitor [Sync log](https://pontoon.mozilla.org/sync/log/)
- `./scripts/quarantine-to-strings.sh clean prep migrate push`
    - This will push to comm-l10n to update en-US
- `./scripts/migration.sh wet-run`
  - When source strings have updated, push migrated strings
  - `pushd comm-l10n; hg push -r .; popd`
- Monitor [Source Repo Update](https://hg.mozilla.org/users/m_owca.info/thunderbird/)
  it updates every 10 minutes. Wait for it to see the new strings before enabling
  sync.
- IF all went well (it should have) - enable Pontoon Sync again


## Archive migrations

- Move the copies in this repo into the appropriate subfolder of recipes for the
  current milestone. Push to Github.
- Move the copies in comm-central into the `completed` subdirectory of
  `tb_fluent_migrations`.
  Push with a "No bug" commit message and "DONTBUILD".

## Problems?

During testing, might be useful to remove the `comm-l10n` and `comm-strings-quarantine` clones.

