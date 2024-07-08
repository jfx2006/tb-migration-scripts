# Thunderbird Fluent Migrations

This repository stores a copy of each migration recipe created for
`comm-central`, and a script to run the migrations.

## Set up the system

1. Create a virtual environment and install dependencies:

    ```bash
    $ virtualenv venv
    $ source venv/bin/activate
    $ pip install mercurial python-hglib tomlkit
    # Get the fluent.migrate fork from https://github.com/jfx2006/tb-fluent-migrate and install
    $ pip install "<path-to->/tb-fluent-migrate[hg]"
    ```

2. Clone [thunderbird-l10n-source](https://github.com/thunderbird/thunderbird-l10n-source)
and switch to the `update` branch.

3. Clone [thunderbird-l10n](https://github.com/thunderbird/thunderbird-l10n-source).

4. Copy `config/config.dist` as `config`, and adapt the paths to your system.

5. Use `/scripts/migration.sh` to run the migration.

## Run migrations and organization of the `recipes` folder

In order to run a migration, the recipe needs to be available in the `recipes`
folder. The script will look for any Python (`.py`) file starting with `bug_`,
allowing to run multiple recipes in one execution.

After running the migration, recipes need to be moved in one of the `tb`
subfolders. For example, if the migration landed in Thunderbird 109, recipes need to
be moved to `tb109`.

The `no_train` folder is used for recipes that never landed in
`comm-central`.

## Command line options

To dry-run all locales use:

```
$ ./scripts/migration.sh no-updates
```

To run one locale without pushing:

```
$ ./scripts/migration.sh it wet-run
```

For running migrations on all locales and push to repository, use:

```
$ ./scripts/migration.sh wet-run push
```

> [!CAUTION]
> The script assumes your locale clone of `firefox-l10n` is already on the
> correct branch, and that the value of `push.default` in Git’s configuration
> allows to push without an explicit remote or branch.

Run `./scripts/migration.sh help` for help on all available command line options.
