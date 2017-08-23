# coding: utf-8
from __future__ import unicode_literals


class ShellCommandError(Exception):
    """Ошибки из stderr"""


class CertificateChainNotChecked(ShellCommandError):
    """Цепочка сертификатов не проверена"""


class InvalidSignature(ShellCommandError):
    """Подпись не верна"""


class CertificatesNotFound(ShellCommandError):
    """Сертификат не найден"""
