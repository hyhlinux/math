# coding:utf-8
# 可以被所有模块导入

import logging
import datetime
import json

# logging.basicConfig(
#   # filename='/tmp/apkpure_dcma.log',
#   level=logging.INFO,
#   format='%(asctime)s:%(funcName)15s:%(lineno)5s%(levelname)8s:%(name)10s:%(message)s',
#   datefmt='%Y/%m/%d %I:%M:%S' # )
# logging.basicConfig(level=logging.INFO)
log_format = '%(asctime)s:%(lineno)5s:%(name)10s:%(levelname)8s:%(message)s'
log_filename = '/tmp/test.log'


def create_log(name, level=logging.DEBUG, filename=log_filename, fhb=False, chb=True, format=log_format):
    new_log = logging.getLogger(name)
    new_log.setLevel(level)
    formatter = logging.Formatter(format)
    if fhb:
        fh = logging.FileHandler(filename)
        fh.setLevel(level)
        fh.setFormatter(formatter)
        new_log.addHandler(fh)

    if chb:
        ch = logging.StreamHandler()
        ch.setLevel(level)
        ch.setFormatter(formatter)
        new_log.addHandler(ch)

    new_log.info('create ok!!')
    return new_log


def get_log(name=''):
    return create_log(name)


def obj_format(obj=None, level=logging.DEBUG, timestamp=True, modle_name=False):
    '''

    :param obj: 字典类型对象, 写到es的数据格式.
    :param level: 调用logger模块是的日志级别，默认为debug.
    :param timestamp: 默认会添加创建时间，utc时间.
    :param modle_name: 默认会添加本模块的__name__变量.
    :return: 对obj序列化为字符串, 传给logger的message变量.
    '''

    if not obj:
        raise 'obj is None'

    # if not type(obj) is dict:
    #     raise 'type(obj) must be dict'
    if not isinstance(obj, dict):
        raise TypeError('type(obj) must be dict')

    if timestamp:
        obj['timestamp'] = datetime.datetime.utcnow().isoformat()

    if modle_name:
        obj['name'] = __name__

    obj['level'] = logging.getLevelName(level)
    return json.dumps(obj)


def main():
    log = get_log()
    log.info('log ok')

if __name__ == '__main__':
    main()
