#!/usr/bin/env python3

"""
Used to remove references to gecko strings from comm-strings-quarantine
_configs/{mail,calendar}.toml. This is needed when running Fluent migrations
and possibly other times.
"""

from pathlib import Path

from tomlkit import load as toml_load, dump as toml_dump

MAIL_TOML = Path(__file__).parent / "../comm-strings-quarantine/_configs/mail.toml"


def startswith_any(text, matches):
    """
    Check to see if text starts with any of the values in matches
    :param text:str Text to check using text.startswith()
    :param matches:tuple(str) strings to compare to
    :return boolean: Whether or not a match was found
    """
    return any([text.startswith(m) for m in matches])


def main():
    with open("comm-strings-quarantine/_configs/mail.toml") as fp:
        doc = toml_load(fp)

    remove_paths = [
        path
        for path in doc["paths"]
        if startswith_any(path["reference"], ("devtools/", "services/"))
    ]
    for path in remove_paths:
        doc["paths"].remove(path)

    remove_includes = [
        include
        for include in doc["includes"]
        if include["path"] != "_configs/calendar.toml"
    ]
    for include in remove_includes:
        doc["includes"].remove(include)

    with open(MAIL_TOML, "w") as fp:
        toml_dump(doc, fp)


if __name__ == "__main__":
    main()
