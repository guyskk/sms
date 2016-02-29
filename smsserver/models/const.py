# coding: utf8


class SMSVerificationStatus(object):
    unused = 1
    used = 2


class SMSSendStatus(object):
    initial = 0
    success = 1
    failed = 2


class SMSProviderIdent(object):
    yunpian = 1
    dahansantong = 2


class ProviderServiceArea(object):
    nation_wide = 1
    world_wide = 2
