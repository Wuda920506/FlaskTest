# coding=utf-8
import redis

class Config:
    DEBUG = True
    # 设置加密密钥
    # CJCKsWgWl/6kU4mmhLoVig4Q2s0BLFXXtqsczQ17LXc/6QXgMiXEyjr+PnLs4M1T0zQ=
    SECRET_KEY = "CJCKsWgWl/6kU4mmhLoVig4Q2s0BLFXXtqsczQ17LXc/6QXgMiXEyjr+PnLs4M1T0zQ="

    # 将session链接到数据库
    SESSION_TYPE = 'redis'

    # 指定session过期时间
    PERMANENT_SESSION_LIFETIME = 3000

    # 对session 信息进行签名
    SESSION_USE_SIGNER = True

    # 针对的是Redis数据库，不是给flask指定ip和port
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379

    # 配置和flask无关
    tSESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)