# coding=utf-8
class Config:
    DEBUG = True
    # 设置加密密钥
    # CJCKsWgWl/6kU4mmhLoVig4Q2s0BLFXXtqsczQ17LXc/6QXgMiXEyjr+PnLs4M1T0zQ=
    SECRET_KEY = "CJCKsWgWl/6kU4mmhLoVig4Q2s0BLFXXtqsczQ17LXc/6QXgMiXEyjr+PnLs4M1T0zQ="

    # 将session链接到数据库
    SESSION_TYPE = 'redis'