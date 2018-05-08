# coding=utf8

# Any copyright is dedicated to the Public Domain.
# http://creativecommons.org/publicdomain/zero/1.0/

from __future__ import absolute_import
import fluent.syntax.ast as FTL
from fluent.migrate import COPY, CONCAT


def migrate(ctx):
    """Bug 1424682 - Migrate the chrome of Preferences to Fluent, part {index}."""

    ctx.add_transforms(
        'browser/browser/preferences/preferences.ftl',
        'browser/browser/preferences/preferences.ftl',
        [
            FTL.Message(
                id=FTL.Identifier('pref-page'),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('title'),
                        FTL.Pattern(
                            elements=[
                                FTL.Placeable(
                                    expression=FTL.SelectExpression(
                                        expression=FTL.CallExpression(
                                            callee=FTL.Function('PLATFORM')
                                        ),
                                        variants=[
                                            FTL.Variant(
                                                key=FTL.VariantName('windows'),
                                                default=False,
                                                value=COPY(
                                                    'browser/chrome/browser/preferences/preferences.dtd',
                                                    'prefWindow.titleWin'
                                                )
                                            ),
                                            FTL.Variant(
                                                key=FTL.VariantName('other'),
                                                default=True,
                                                value=COPY(
                                                    'browser/chrome/browser/preferences/preferences.dtd',
                                                    'prefWindow.title'
                                                )
                                            )
                                        ]
                                    )
                                )
                            ]
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('search-input'),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('style'),
                        CONCAT(
                            FTL.TextElement('width: '),
                            COPY(
                                'browser/chrome/browser/preferences/preferences.dtd',
                                'searchField.width'
                            )
                        ),
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('pane-general-title'),
                value=COPY(
                    'browser/chrome/browser/preferences/preferences.dtd',
                    'paneGeneral.title'
                )
            ),
            FTL.Message(
                id=FTL.Identifier('category-general'),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('tooltiptext'),
                        CONCAT(
                            MESSAGE_REFERENCE('pane-general-title')
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('pane-search-title'),
                value=COPY(
                    'browser/chrome/browser/preferences/preferences.dtd',
                    'paneSearch.title'
                )
            ),
            FTL.Message(
                id=FTL.Identifier('category-search'),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('tooltiptext'),
                        CONCAT(
                            MESSAGE_REFERENCE('pane-search-title')
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('pane-privacy-title'),
                value=COPY(
                    'browser/chrome/browser/preferences/preferences.dtd',
                    'panePrivacySecurity.title'
                )
            ),
            FTL.Message(
                id=FTL.Identifier('category-privacy'),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('tooltiptext'),
                        CONCAT(
                            MESSAGE_REFERENCE('pane-privacy-title')
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('pane-sync-title'),
                value=COPY(
                    'browser/chrome/browser/preferences/preferences.dtd',
                    'paneSync1.title'
                )
            ),
            FTL.Message(
                id=FTL.Identifier('category-sync'),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('tooltiptext'),
                        CONCAT(
                            MESSAGE_REFERENCE('pane-sync-title')
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('help-button-label'),
                value=REPLACE(
                    'browser/chrome/browser/preferences/preferences.dtd',
                    'helpButton2.label',
                    {
                        '&brandShortName;' : MESSAGE_REFERENCE('-brand-short-name')
                    }
                )
            ),
            FTL.Message(
                id=FTL.Identifier('focus-search'),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('key'),
                        COPY(
                            'toolkit/chrome/passwordmgr/passwordManager.dtd',
                            'focusSearch1.key'
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('close-button'),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('aria-label'),
                        COPY(
                            'toolkit/chrome/global/preferences.dtd',
                            'preferencesCloseButton.label'
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('feature-enable-requires-restart'),
                value=REPLACE(
                    'browser/chrome/browser/preferences/preferences.properties',
                    'featureEnableRequiresRestart',
                    {
                        '%S' : MESSAGE_REFERENCE('-brand-short-name')
                    }
                )
            ),
            FTL.Message(
                id=FTL.Identifier('feature-disable-requires-restart'),
                value=REPLACE(
                    'browser/chrome/browser/preferences/preferences.properties',
                    'featureDisableRequiresRestart',
                    {
                        '%S' : MESSAGE_REFERENCE('-brand-short-name')
                    }
                )
            ),
            FTL.Message(
                id=FTL.Identifier('should-restart-title'),
                value=REPLACE(
                    'browser/chrome/browser/preferences/preferences.properties',
                    'shouldRestartTitle',
                    {
                        '%S' : MESSAGE_REFERENCE('-brand-short-name')
                    }
                )
            ),
            FTL.Message(
                id=FTL.Identifier('should-restart-ok'),
                value=REPLACE(
                    'browser/chrome/browser/preferences/preferences.properties',
                    'okToRestartButton',
                    {
                        '%S' : MESSAGE_REFERENCE('-brand-short-name')
                    }
                )
            ),
            FTL.Message(
                id=FTL.Identifier('restart-later'),
                value=COPY(
                    'browser/chrome/browser/preferences/preferences.properties',
                    'restartLater',
                )
            ),
        ]
    )
