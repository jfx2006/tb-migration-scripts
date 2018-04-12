# coding=utf8

# Any copyright is dedicated to the Public Domain.
# http://creativecommons.org/publicdomain/zero/1.0/

from __future__ import absolute_import
import fluent.syntax.ast as FTL
from fluent.migrate.helpers import MESSAGE_REFERENCE
from fluent.migrate import COPY, CONCAT, REPLACE

def migrate(ctx):
    """Bug 1451992 - Migrate Preferences::Subdialogs::Fonts to Fluent, part {index}."""

    ctx.add_transforms(
        'browser/browser/preferences/fonts.ftl',
        'browser/browser/preferences/fonts.ftl',
        [
            FTL.Message(
                id=FTL.Identifier('fonts-window'),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('title'),
                        COPY(
                            'browser/chrome/browser/preferences/fonts.dtd',
                            'fontsDialog.title'
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('fonts-window-close'),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('key'),
                        COPY(
                            'toolkit/chrome/global/preferences.dtd',
                            'windowClose.key'
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('fonts-langgroup-header'),
                value=COPY(
                    'browser/chrome/browser/preferences/fonts.dtd',
                    'fonts.label'
                ),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('accesskey'),
                        COPY(
                            'browser/chrome/browser/preferences/fonts.dtd',
                            'fonts.accesskey'
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('fonts-langgroup-arabic'),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('label'),
                        COPY(
                            'browser/chrome/browser/preferences/fonts.dtd',
                            'font.langGroup.arabic'
                        )
                    )
                ]
            ),

            FTL.Message(
                id=FTL.Identifier('fonts-langgroup-armenian'),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('label'),
                        COPY(
                            'browser/chrome/browser/preferences/fonts.dtd',
                            'font.langGroup.armenian'
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('fonts-langgroup-bengali'),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('label'),
                        COPY(
                            'browser/chrome/browser/preferences/fonts.dtd',
                            'font.langGroup.bengali'
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('fonts-langgroup-simpl-chinese'),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('label'),
                        COPY(
                            'browser/chrome/browser/preferences/fonts.dtd',
                            'font.langGroup.simpl-chinese'
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('fonts-langgroup-trad-chinese-hk'),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('label'),
                        COPY(
                            'browser/chrome/browser/preferences/fonts.dtd',
                            'font.langGroup.trad-chinese-hk'
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('fonts-langgroup-trad-chinese'),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('label'),
                        COPY(
                            'browser/chrome/browser/preferences/fonts.dtd',
                            'font.langGroup.trad-chinese'
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('fonts-langgroup-cyrillic'),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('label'),
                        COPY(
                            'browser/chrome/browser/preferences/fonts.dtd',
                            'font.langGroup.cyrillic'
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('fonts-langgroup-devanagari'),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('label'),
                        COPY(
                            'browser/chrome/browser/preferences/fonts.dtd',
                            'font.langGroup.devanagari'
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('fonts-langgroup-ethiopic'),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('label'),
                        COPY(
                            'browser/chrome/browser/preferences/fonts.dtd',
                            'font.langGroup.ethiopic'
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('fonts-langgroup-georgian'),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('label'),
                        COPY(
                            'browser/chrome/browser/preferences/fonts.dtd',
                            'font.langGroup.georgian'
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('fonts-langgroup-el'),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('label'),
                        COPY(
                            'browser/chrome/browser/preferences/fonts.dtd',
                            'font.langGroup.el'
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('fonts-langgroup-gujarati'),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('label'),
                        COPY(
                            'browser/chrome/browser/preferences/fonts.dtd',
                            'font.langGroup.gujarati'
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('fonts-langgroup-gurmukhi'),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('label'),
                        COPY(
                            'browser/chrome/browser/preferences/fonts.dtd',
                            'font.langGroup.gurmukhi'
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('fonts-langgroup-japanese'),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('label'),
                        COPY(
                            'browser/chrome/browser/preferences/fonts.dtd',
                            'font.langGroup.japanese'
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('fonts-langgroup-hebrew'),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('label'),
                        COPY(
                            'browser/chrome/browser/preferences/fonts.dtd',
                            'font.langGroup.hebrew'
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('fonts-langgroup-kannada'),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('label'),
                        COPY(
                            'browser/chrome/browser/preferences/fonts.dtd',
                            'font.langGroup.kannada'
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('fonts-langgroup-khmer'),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('label'),
                        COPY(
                            'browser/chrome/browser/preferences/fonts.dtd',
                            'font.langGroup.khmer'
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('fonts-langgroup-korean'),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('label'),
                        COPY(
                            'browser/chrome/browser/preferences/fonts.dtd',
                            'font.langGroup.korean'
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('fonts-langgroup-latin'),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('label'),
                        COPY(
                            'browser/chrome/browser/preferences/fonts.dtd',
                            'font.langGroup.latin'
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('fonts-langgroup-malayalam'),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('label'),
                        COPY(
                            'browser/chrome/browser/preferences/fonts.dtd',
                            'font.langGroup.malayalam'
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('fonts-langgroup-math'),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('label'),
                        COPY(
                            'browser/chrome/browser/preferences/fonts.dtd',
                            'font.langGroup.math'
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('fonts-langgroup-odia'),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('label'),
                        COPY(
                            'browser/chrome/browser/preferences/fonts.dtd',
                            'font.langGroup.odia'
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('fonts-langgroup-sinhala'),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('label'),
                        COPY(
                            'browser/chrome/browser/preferences/fonts.dtd',
                            'font.langGroup.sinhala'
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('fonts-langgroup-tamil'),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('label'),
                        COPY(
                            'browser/chrome/browser/preferences/fonts.dtd',
                            'font.langGroup.tamil'
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('fonts-langgroup-telugu'),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('label'),
                        COPY(
                            'browser/chrome/browser/preferences/fonts.dtd',
                            'font.langGroup.telugu'
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('fonts-langgroup-thai'),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('label'),
                        COPY(
                            'browser/chrome/browser/preferences/fonts.dtd',
                            'font.langGroup.thai'
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('fonts-langgroup-tibetan'),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('label'),
                        COPY(
                            'browser/chrome/browser/preferences/fonts.dtd',
                            'font.langGroup.tibetan'
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('fonts-langgroup-canadian'),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('label'),
                        COPY(
                            'browser/chrome/browser/preferences/fonts.dtd',
                            'font.langGroup.canadian'
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('fonts-langgroup-other'),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('label'),
                        COPY(
                            'browser/chrome/browser/preferences/fonts.dtd',
                            'font.langGroup.other'
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('fonts-proportional-header'),
                value=COPY(
                    'browser/chrome/browser/preferences/fonts.dtd',
                    'proportional2.label'
                ),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('accesskey'),
                        COPY(
                            'browser/chrome/browser/preferences/fonts.dtd',
                            'proportional2.accesskey'
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('fonts-default-serif'),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('label'),
                        COPY(
                            'browser/chrome/browser/preferences/fonts.dtd',
                            'useDefaultFontSerif.label'
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('fonts-default-sans-serif'),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('label'),
                        COPY(
                            'browser/chrome/browser/preferences/fonts.dtd',
                            'useDefaultFontSansSerif.label'
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('fonts-proportional-size'),
                value=COPY(
                    'browser/chrome/browser/preferences/fonts.dtd',
                    'size2.label'
                ),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('accesskey'),
                        COPY(
                            'browser/chrome/browser/preferences/fonts.dtd',
                            'sizeProportional.accesskey'
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('fonts-serif'),
                value=COPY(
                    'browser/chrome/browser/preferences/fonts.dtd',
                    'serif2.label'
                ),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('accesskey'),
                        COPY(
                            'browser/chrome/browser/preferences/fonts.dtd',
                            'serif2.accesskey'
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('fonts-sans-serif'),
                value=COPY(
                    'browser/chrome/browser/preferences/fonts.dtd',
                    'sans-serif2.label'
                ),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('accesskey'),
                        COPY(
                            'browser/chrome/browser/preferences/fonts.dtd',
                            'sans-serif2.accesskey'
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('fonts-monospace'),
                value=COPY(
                    'browser/chrome/browser/preferences/fonts.dtd',
                    'monospace2.label'
                ),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('accesskey'),
                        COPY(
                            'browser/chrome/browser/preferences/fonts.dtd',
                            'monospace2.accesskey'
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('fonts-monospace-size'),
                value=COPY(
                    'browser/chrome/browser/preferences/fonts.dtd',
                    'size2.label'
                ),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('accesskey'),
                        COPY(
                            'browser/chrome/browser/preferences/fonts.dtd',
                            'sizeMonospace.accesskey'
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('fonts-minsize'),
                value=COPY(
                    'browser/chrome/browser/preferences/fonts.dtd',
                    'minSize2.label'
                ),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('accesskey'),
                        COPY(
                            'browser/chrome/browser/preferences/fonts.dtd',
                            'minSize2.accesskey'
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('fonts-minsize-none'),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('label'),
                        COPY(
                            'browser/chrome/browser/preferences/fonts.dtd',
                            'minSize.none'
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('fonts-allow-own'),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('label'),
                        COPY(
                            'browser/chrome/browser/preferences/fonts.dtd',
                            'allowPagesToUseOwn.label'
                        )
                    ),
                    FTL.Attribute(
                        FTL.Identifier('accesskey'),
                        COPY(
                            'browser/chrome/browser/preferences/fonts.dtd',
                            'allowPagesToUseOwn.accesskey'
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('fonts-languages-fallback-header'),
                value=COPY(
                    'browser/chrome/browser/preferences/fonts.dtd',
                    'languages.customize.Fallback2.grouplabel'
                )
            ),
            FTL.Message(
                id=FTL.Identifier('fonts-languages-fallback-desc'),
                value=COPY(
                    'browser/chrome/browser/preferences/fonts.dtd',
                    'languages.customize.Fallback2.desc'
                )
            ),
            FTL.Message(
                id=FTL.Identifier('fonts-languages-fallback-label'),
                value=COPY(
                    'browser/chrome/browser/preferences/fonts.dtd',
                    'languages.customize.Fallback3.label'
                ),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('accesskey'),
                        COPY(
                            'browser/chrome/browser/preferences/fonts.dtd',
                            'languages.customize.Fallback3.accesskey'
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('fonts-languages-fallback-name-auto'),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('label'),
                        COPY(
                            'browser/chrome/browser/preferences/fonts.dtd',
                            'languages.customize.Fallback.auto'
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('fonts-languages-fallback-name-arabic'),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('label'),
                        COPY(
                            'browser/chrome/browser/preferences/fonts.dtd',
                            'languages.customize.Fallback.arabic'
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('fonts-languages-fallback-name-baltic'),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('label'),
                        COPY(
                            'browser/chrome/browser/preferences/fonts.dtd',
                            'languages.customize.Fallback.baltic'
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('fonts-languages-fallback-name-ceiso'),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('label'),
                        COPY(
                            'browser/chrome/browser/preferences/fonts.dtd',
                            'languages.customize.Fallback.ceiso'
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('fonts-languages-fallback-name-cewindows'),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('label'),
                        COPY(
                            'browser/chrome/browser/preferences/fonts.dtd',
                            'languages.customize.Fallback.cewindows'
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('fonts-languages-fallback-name-simplified'),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('label'),
                        COPY(
                            'browser/chrome/browser/preferences/fonts.dtd',
                            'languages.customize.Fallback.simplified'
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('fonts-languages-fallback-name-traditional'),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('label'),
                        COPY(
                            'browser/chrome/browser/preferences/fonts.dtd',
                            'languages.customize.Fallback.traditional'
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('fonts-languages-fallback-name-cyrillic'),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('label'),
                        COPY(
                            'browser/chrome/browser/preferences/fonts.dtd',
                            'languages.customize.Fallback.cyrillic'
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('fonts-languages-fallback-name-greek'),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('label'),
                        COPY(
                            'browser/chrome/browser/preferences/fonts.dtd',
                            'languages.customize.Fallback.greek'
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('fonts-languages-fallback-name-hebrew'),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('label'),
                        COPY(
                            'browser/chrome/browser/preferences/fonts.dtd',
                            'languages.customize.Fallback.hebrew'
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('fonts-languages-fallback-name-japanese'),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('label'),
                        COPY(
                            'browser/chrome/browser/preferences/fonts.dtd',
                            'languages.customize.Fallback.japanese'
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('fonts-languages-fallback-name-korean'),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('label'),
                        COPY(
                            'browser/chrome/browser/preferences/fonts.dtd',
                            'languages.customize.Fallback.korean'
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('fonts-languages-fallback-name-thai'),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('label'),
                        COPY(
                            'browser/chrome/browser/preferences/fonts.dtd',
                            'languages.customize.Fallback.thai'
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('fonts-languages-fallback-name-turkish'),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('label'),
                        COPY(
                            'browser/chrome/browser/preferences/fonts.dtd',
                            'languages.customize.Fallback.turkish'
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('fonts-languages-fallback-name-vietnamese'),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('label'),
                        COPY(
                            'browser/chrome/browser/preferences/fonts.dtd',
                            'languages.customize.Fallback.vietnamese'
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('fonts-languages-fallback-name-other'),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('label'),
                        COPY(
                            'browser/chrome/browser/preferences/fonts.dtd',
                            'languages.customize.Fallback.other'
                        )
                    )
                ]
            )
        ]
    )
