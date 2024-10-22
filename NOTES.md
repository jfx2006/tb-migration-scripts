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

- Find the PR with the Fluent file updates in [thunderbird-l10n-source](https://github.com/thunderbird/thunderbird-l10n-source).
  Do not merge it yet, just note the number, it will be merged later.
- Clone both [thunderbird-l10n-source](https://github.com/thunderbird/thunderbird-l10n-source)
  and [thunderbird-l10n](https://github.com/thunderbird/thunderbird-l10n).
  - thunderbird-l10n-source checkout the "update" branch. This is the branch with
    the PR from above.
  - thunderbird-l10n, create and checkout a new branch off "main" named
    "fluent-migrate-temp"

- Check es-MX - **do not enable push**
    - `./scripts/compare_locales_esMX.sh`

- Check that all locales work -- **do not enable push**
  `./scripts/migration.sh wet-run`
- Ensure there were no errors. Proceed only if there were no errors!


## Run migrations for real

*Keep in mind that Pontoon sync is disabled for the entire time you are running
this migration. It's essential that you have completed the above testing and
that you have another team member ready to review the PR at the end.*

- **Stop sync in Pontoon**
- In thunderbird-l10n, checkout `main` again. Remove your temporary branch.
  Pull in any additional commits to `main` from Pontoon, (`git pull`) and
  create and checkout a new branch `fluent-migrate-$(date +%Y%m%d)`.
- Merge the thunderbird-l0n-source PR from above in Github.
- In your local copy, checkout `thunderbird-l10n-source` main branch and
  pull in changes from the merged PR.
- Monitor [Sync log](https://pontoon.mozilla.org/sync/log/)
- `./scripts/migration.sh wet-run` (do not enable the *push* option!)
- Assuming your testing above was successful, there should be no errors.
- In thunderbird-l10n, `git push origin fluent-migrate-$(date +%Y%m%d)`.
- Create a PR from that push and have another team member review.
- Merge the PR into main.
- **Start sync in Pontoon**
- Remove your local branch.


## Archive migrations

- Move the copies in this repo into the appropriate subfolder of recipes for the
  current milestone. Push to Github.
- Move the copies in comm-central into the `completed` subdirectory of
  `tb_fluent_migrations`.
  Push with a "No bug" commit message and "DONTBUILD".

## Tips

Using fresh clones for testing and real runs is very helpful.

