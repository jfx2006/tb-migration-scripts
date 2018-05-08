# coding=utf8

# Any copyright is dedicated to the Public Domain.
# http://creativecommons.org/publicdomain/zero/1.0/

from __future__ import absolute_import
import fluent.syntax.ast as FTL
from fluent.migrate import COPY, CONCAT

def migrate(ctx):
    """Bug 1451992 - Migrate Preferences::Subdialogs::Connection to Fluent, part {index}."""

    ctx.add_transforms(
        'browser/browser/preferences/connection.ftl',
        'browser/browser/preferences/connection.ftl',
        [
            FTL.Message(
                id=FTL.Identifier('connection-window'),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('title'),
                        COPY(
                            'browser/chrome/browser/preferences/connection.dtd',
                            'connectionsDialog.title'
                        )
                    ),
                    FTL.Attribute(
                        FTL.Identifier('style'),
                        FTL.Pattern(
                            elements=[
                                FTL.Placeable(
                                    expression=FTL.SelectExpression(
                                        expression=FTL.CallExpression(
                                            callee=FTL.Function('PLATFORM')
                                        ),
                                        variants=[
                                            FTL.Variant(
                                                key=FTL.VariantName('macos'),
                                                default=False,
                                                value=CONCAT(
                                                    FTL.TextElement('width: '),
                                                    COPY(
                                                        'browser/chrome/browser/preferences/connection.dtd',
                                                        'window.macWidth2'
                                                    )
                                                )
                                            ),
                                            FTL.Variant(
                                                key=FTL.VariantName('other'),
                                                default=True,
                                                value=CONCAT(
                                                    FTL.TextElement('width: '),
                                                    COPY(
                                                        'browser/chrome/browser/preferences/connection.dtd',
                                                        'window.width2'
                                                    )
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
                id=FTL.Identifier('connection-close-key'),
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
                id=FTL.Identifier('connection-disable-extension'),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('label'),
                        COPY(
                            'browser/chrome/browser/preferences/main.dtd',
                            'disableExtension.label'
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('connection-proxy-configure'),
                value=COPY(
                    'browser/chrome/browser/preferences/connection.dtd',
                    'proxyTitle.label2'
                )
            ),
            FTL.Message(
                id=FTL.Identifier('connection-proxy-option-no'),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('label'),
                        COPY(
                            'browser/chrome/browser/preferences/connection.dtd',
                            'noProxyTypeRadio.label'
                        )
                    ),
                    FTL.Attribute(
                        FTL.Identifier('accesskey'),
                        COPY(
                            'browser/chrome/browser/preferences/connection.dtd',
                            'noProxyTypeRadio.accesskey'
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('connection-proxy-option-system'),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('label'),
                        COPY(
                            'browser/chrome/browser/preferences/connection.dtd',
                            'systemTypeRadio.label'
                        )
                    ),
                    FTL.Attribute(
                        FTL.Identifier('accesskey'),
                        COPY(
                            'browser/chrome/browser/preferences/connection.dtd',
                            'systemTypeRadio.accesskey'
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('connection-proxy-option-auto'),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('label'),
                        COPY(
                            'browser/chrome/browser/preferences/connection.dtd',
                            'WPADTypeRadio.label'
                        )
                    ),
                    FTL.Attribute(
                        FTL.Identifier('accesskey'),
                        COPY(
                            'browser/chrome/browser/preferences/connection.dtd',
                            'WPADTypeRadio.accesskey'
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('connection-proxy-option-manual'),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('label'),
                        COPY(
                            'browser/chrome/browser/preferences/connection.dtd',
                            'manualTypeRadio2.label'
                        )
                    ),
                    FTL.Attribute(
                        FTL.Identifier('accesskey'),
                        COPY(
                            'browser/chrome/browser/preferences/connection.dtd',
                            'manualTypeRadio2.accesskey'
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('connection-proxy-http'),
                value=COPY(
                    'browser/chrome/browser/preferences/connection.dtd',
                    'http2.label'
                ),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('accesskey'),
                        COPY(
                            'browser/chrome/browser/preferences/connection.dtd',
                            'http2.accesskey'
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('connection-proxy-http-port'),
                value=COPY(
                    'browser/chrome/browser/preferences/connection.dtd',
                    'port2.label'
                ),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('accesskey'),
                        COPY(
                            'browser/chrome/browser/preferences/connection.dtd',
                            'HTTPport.accesskey'
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('connection-proxy-http-share'),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('label'),
                        COPY(
                            'browser/chrome/browser/preferences/connection.dtd',
                            'shareproxy.label'
                        )
                    ),
                    FTL.Attribute(
                        FTL.Identifier('accesskey'),
                        COPY(
                            'browser/chrome/browser/preferences/connection.dtd',
                            'shareproxy.accesskey'
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('connection-proxy-ssl'),
                value=COPY(
                    'browser/chrome/browser/preferences/connection.dtd',
                    'ssl2.label'
                ),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('accesskey'),
                        COPY(
                            'browser/chrome/browser/preferences/connection.dtd',
                            'ssl2.accesskey'
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('connection-proxy-ssl-port'),
                value=COPY(
                    'browser/chrome/browser/preferences/connection.dtd',
                    'port2.label'
                ),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('accesskey'),
                        COPY(
                            'browser/chrome/browser/preferences/connection.dtd',
                            'SSLport.accesskey'
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('connection-proxy-ftp'),
                value=COPY(
                    'browser/chrome/browser/preferences/connection.dtd',
                    'ftp2.label'
                ),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('accesskey'),
                        COPY(
                            'browser/chrome/browser/preferences/connection.dtd',
                            'ftp2.accesskey'
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('connection-proxy-ftp-port'),
                value=COPY(
                    'browser/chrome/browser/preferences/connection.dtd',
                    'port2.label'
                ),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('accesskey'),
                        COPY(
                            'browser/chrome/browser/preferences/connection.dtd',
                            'FTPport.accesskey'
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('connection-proxy-socks'),
                value=COPY(
                    'browser/chrome/browser/preferences/connection.dtd',
                    'socks2.label'
                ),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('accesskey'),
                        COPY(
                            'browser/chrome/browser/preferences/connection.dtd',
                            'socks2.accesskey'
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('connection-proxy-socks-port'),
                value=COPY(
                    'browser/chrome/browser/preferences/connection.dtd',
                    'port2.label'
                ),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('accesskey'),
                        COPY(
                            'browser/chrome/browser/preferences/connection.dtd',
                            'SOCKSport.accesskey'
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('connection-proxy-socks4'),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('label'),
                        COPY(
                            'browser/chrome/browser/preferences/connection.dtd',
                            'socks4.label'
                        )
                    ),
                    FTL.Attribute(
                        FTL.Identifier('accesskey'),
                        COPY(
                            'browser/chrome/browser/preferences/connection.dtd',
                            'socks4.accesskey'
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('connection-proxy-socks5'),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('label'),
                        COPY(
                            'browser/chrome/browser/preferences/connection.dtd',
                            'socks5.label'
                        )
                    ),
                    FTL.Attribute(
                        FTL.Identifier('accesskey'),
                        COPY(
                            'browser/chrome/browser/preferences/connection.dtd',
                            'socks5.accesskey'
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('connection-proxy-noproxy'),
                value=COPY(
                    'browser/chrome/browser/preferences/connection.dtd',
                    'noproxy2.label'
                ),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('accesskey'),
                        COPY(
                            'browser/chrome/browser/preferences/connection.dtd',
                            'noproxy2.accesskey'
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('connection-proxy-noproxy-desc'),
                value=COPY(
                    'browser/chrome/browser/preferences/connection.dtd',
                    'noproxyExplain.label'
                )
            ),
            FTL.Message(
                id=FTL.Identifier('connection-proxy-autotype'),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('label'),
                        COPY(
                            'browser/chrome/browser/preferences/connection.dtd',
                            'autoTypeRadio2.label'
                        )
                    ),
                    FTL.Attribute(
                        FTL.Identifier('accesskey'),
                        COPY(
                            'browser/chrome/browser/preferences/connection.dtd',
                            'autoTypeRadio2.accesskey'
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('connection-proxy-reload'),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('label'),
                        COPY(
                            'browser/chrome/browser/preferences/connection.dtd',
                            'reload.label'
                        )
                    ),
                    FTL.Attribute(
                        FTL.Identifier('accesskey'),
                        COPY(
                            'browser/chrome/browser/preferences/connection.dtd',
                            'reload.accesskey'
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('connection-proxy-autologin'),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('label'),
                        COPY(
                            'browser/chrome/browser/preferences/connection.dtd',
                            'autologinproxy.label'
                        )
                    ),
                    FTL.Attribute(
                        FTL.Identifier('accesskey'),
                        COPY(
                            'browser/chrome/browser/preferences/connection.dtd',
                            'autologinproxy.accesskey'
                        )
                    ),
                    FTL.Attribute(
                        FTL.Identifier('tooltip'),
                        COPY(
                            'browser/chrome/browser/preferences/connection.dtd',
                            'autologinproxy.tooltip'
                        )
                    )
                ]
            ),
            FTL.Message(
                id=FTL.Identifier('connection-proxy-socks-remote-dns'),
                attributes=[
                    FTL.Attribute(
                        FTL.Identifier('label'),
                        COPY(
                            'browser/chrome/browser/preferences/connection.dtd',
                            'socksRemoteDNS.label2'
                        )
                    ),
                    FTL.Attribute(
                        FTL.Identifier('accesskey'),
                        COPY(
                            'browser/chrome/browser/preferences/connection.dtd',
                            'socksRemoteDNS.accesskey'
                        )
                    )
                ]
            )
        ]
    )
