# Any copyright is dedicated to the Public Domain.
# http://creativecommons.org/publicdomain/zero/1.0/

import fluent.syntax.ast as FTL
import fluent.migratetb.helpers
from fluent.migratetb import COPY
from fluent.migratetb.helpers import transforms_from
from fluent.migratetb.helpers import VARIABLE_REFERENCE
from fluent.migratetb.transforms import Transform, TransformPattern, PLURALS, REPLACE_IN_TEXT

"""
duplicate-error =
    { $count ->
        [one] {REPLACE(from_path, "duplicateError", replacements_count_filePath)}
        *[other] {REPLACE(from_path, "duplicateError", replacements_count_filePath)}
    }
"""

def migrate(ctx):
    """Bug 1893758 Calendar Fluent Migrations - Properties Part A Files 2. part {index}"""
    target = reference = "calendar/calendar/calendar.ftl"
    source = "calendar/chrome/calendar/calendar.properties"

    ctx.add_transforms(
        target,
        reference,
        [
            FTL.Message(
                id=FTL.Identifier("duplicate-error"),
                value=PLURALS(
                    source,
                    "duplicateError",
                    VARIABLE_REFERENCE("count"),
                    lambda text: REPLACE_IN_TEXT(
                        text,
                        {"%1$S": VARIABLE_REFERENCE("count"),
                         "%2$S": VARIABLE_REFERENCE("filePath")
                        },
                    )
                )
            )
        ],
    )
