# -*- coding: utf-8 -*-
from akad.ttypes import ApplicationType
import re

class Config(object):
    LINE_HOST_DOMAIN            = 'https://gd2.line.naver.jp'
    LINE_OBS_DOMAIN             = 'https://obs-sg.line-apps.com'
    LINE_LOGIN_QUERY_PATH       = '/api/v4p/rs'
    LINE_AUTH_QUERY_PATH        = '/api/v4/TalkService.do'
    LINE_API_QUERY_PATH_FIR     = '/S4'
    LINE_POLL_QUERY_PATH_FIR    = '/P4'
    LINE_CALL_QUERY_PATH        = '/V4'
    LINE_CERTIFICATE_PATH       = '/Q'

    CARRIER     = '51010, 1-0'
    SYSTEM_NAME = 'LINE_BOTS'
    #SYSTEM_VER  = '13.2.2'
    IP_ADDR     = '127.0.0.1'
    EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")

    def __init__(self):
        self.APP_NAME = 'CHANNELCP\t2.9.1\tAndroid OS\t5.1.1'
        self.USER_AGENT = 'LLA/2.9.1 SM-J320G 5.1.1'
        
