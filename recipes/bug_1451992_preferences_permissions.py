# coding=utf8

# Any copyright is dedicated to the Public Domain.
# http://creativecommons.org/publicdomain/zero/1.0/

from __future__ import absolute_import
import fluent.syntax.ast as FTL
from fluent.migrate.helpers import MESSAGE_REFERENCE
from fluent.migrate import COPY, CONCAT, REPLACE

def migrate(ctx):
    """Bug 1451992 - Migrate Preferences::Subdialogs::Permissions to Fluent, part {index}."""

    ctx.add_transforms(
        'browser/browser/preferences/permissions.ftl',
        'browser/browser/preferences/permissions.ftl',
        [
            FTL.Message(
                id=FTL.Identifier('permissions-window'),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('title'),
                        COPY(
                            'browser/chrome/browser/preferences/permissions.dtd',
                            'window.title'
                        )
                    ),
                    FTL.Attribute(
                        FTL.Identifier('style'),
                        CONCAT(
                            FTL.TextElement('width: '),
                            COPY(
                                'browser/chrome/browser/preferences/permissions.dtd',
                                'window.width'
                            )
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('permissions-close-key'),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('key'),
                        COPY(
                            'browser/chrome/browser/preferences/permissions.dtd',
                            'windowClose.key'
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('permissions-address'),
                value=COPY(
                    'browser/chrome/browser/preferences/permissions.dtd',
                    'address2.label'
                ),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('accesskey'),
                        COPY(
                            'browser/chrome/browser/preferences/permissions.dtd',
                            'address2.accesskey'
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('permissions-block'),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('label'),
                        COPY(
                            'browser/chrome/browser/preferences/permissions.dtd',
                            'block.label'
                        )
                    ),
                    FTL.Attribute(
                        FTL.Identifier('accesskey'),
                        COPY(
                            'browser/chrome/browser/preferences/permissions.dtd',
                            'block.accesskey'
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('permissions-session'),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('label'),
                        COPY(
                            'browser/chrome/browser/preferences/permissions.dtd',
                            'session.label'
                        )
                    ),
                    FTL.Attribute(
                        FTL.Identifier('accesskey'),
                        COPY(
                            'browser/chrome/browser/preferences/permissions.dtd',
                            'session.accesskey'
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('permissions-allow'),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('label'),
                        COPY(
                            'browser/chrome/browser/preferences/permissions.dtd',
                            'allow.label'
                        )
                    ),
                    FTL.Attribute(
                        FTL.Identifier('accesskey'),
                        COPY(
                            'browser/chrome/browser/preferences/permissions.dtd',
                            'allow.accesskey'
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('permissions-site-name'),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('label'),
                        COPY(
                            'browser/chrome/browser/preferences/permissions.dtd',
                            'treehead.sitename2.label'
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('permissions-status'),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('label'),
                        COPY(
                            'browser/chrome/browser/preferences/permissions.dtd',
                            'treehead.status.label'
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('permissions-remove'),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('label'),
                        COPY(
                            'browser/chrome/browser/preferences/permissions.dtd',
                            'removepermission2.label'
                        )
                    ),
                    FTL.Attribute(
                        FTL.Identifier('accesskey'),
                        COPY(
                            'browser/chrome/browser/preferences/permissions.dtd',
                            'removepermission2.accesskey'
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('permissions-remove-all'),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('label'),
                        COPY(
                            'browser/chrome/browser/preferences/permissions.dtd',
                            'removeallpermissions2.label'
                        )
                    ),
                    FTL.Attribute(
                        FTL.Identifier('accesskey'),
                        COPY(
                            'browser/chrome/browser/preferences/permissions.dtd',
                            'removeallpermissions2.accesskey'
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('permissions-button-cancel'),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('label'),
                        COPY(
                            'browser/chrome/browser/preferences/permissions.dtd',
                            'button.cancel.label'
                        )
                    ),
                    FTL.Attribute(
                        FTL.Identifier('accesskey'),
                        COPY(
                            'browser/chrome/browser/preferences/permissions.dtd',
                            'button.cancel.accesskey'
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('permissions-button-ok'),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('label'),
                        COPY(
                            'browser/chrome/browser/preferences/permissions.dtd',
                            'button.ok.label'
                        )
                    ),
                    FTL.Attribute(
                        FTL.Identifier('accesskey'),
                        COPY(
                            'browser/chrome/browser/preferences/permissions.dtd',
                            'button.ok.accesskey'
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('permissions-searchbox'),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('placeholder'),
                        COPY(
                            'browser/chrome/browser/preferences/permissions.dtd',
                            'searchbox.placeholder'
                        )
                    )
                ]
            )
        ]
    )
