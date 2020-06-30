import functools
import logging
from functools import wraps
import inspect

logging.basicConfig(level=logging.INFO, format='%(asctime)-16s %(levelname)-8s %(message)s')


def use_logging(func):
    '''参数打印装饰器'''

    def wrapper(*args, **kwargs):
        logging.info("[当前调用的方法是]: {}".format(func.__name__))
        for i in range(len(args)):
            logging.info("[第{}个参数是]: {}".format(i, args[i]))
        for k, v in kwargs:
            logging.info("key is: {}  value is: {}".format(k, v))
        return func(*args, **kwargs)

    return wrapper


def params_check(*types, **kwtypes):
    '''校验入参合法性'''

    def decorator(func):
        @functools.wraps(func)  # 保留元信息
        def wrapper(*args, **kwargs):
            # 判断可变长参数
            res1 = [isinstance(para, type) for para, type in zip(args, types)]
            assert all(res1), "args type is not expect"
            # 判断关键字参数
            res2 = [isinstance(kwargs[key], kwtypes[key]) for key in kwargs]
            assert all(res2), "keyword para is not expect"
            return func(*args, **kwargs)

        return wrapper

    return decorator


def logit(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        logging.info("[当前被调用方法是]: {}".format(func.__name__))
        para_name = inspect.getfullargspec(func).args
        para_value = list(locals()[u'args'])
        para_dic = locals()[u'kwargs']
        for i in range(len(para_name)):
            if para_name[i] != u'self':
                try:
                    logging.info(u'[%s is]: %s %s' % (para_name[i], para_value[i], type(para_value[i])))
                except Exception as e:
                    pass
        if para_dic:
            for key in para_dic:
                logging.info(u'[%s is]: %s' % (key, para_dic[key]))
        res = func(*args, **kwargs)
        logging.info("[执行结果为]: {}".format(res))
        return res

    return with_logging


class Logit(object):
    def __init__(self, level):
        self.level = level

    def __call__(self, func, *args, **kwargs):
        def wrapper(*args, **kwargs):
            if self.level == "info":
                logging.info("[当前调用的函数是]: {}".format(func.__name__))
                for i in range(len(args)):
                    logging.info("[第{}个参数是]: {}".format(i, args[i]))
                for k, v in kwargs.items():
                    logging.info("key is: {}  value is: {}".format(k, v))
                return func(*args, **kwargs)

        return wrapper


@use_logging
def add(x, y):
    return x + y


if __name__ == '__main__':
    add(1, 2)
