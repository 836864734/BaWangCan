import logging
import sys


# 创建一个日志器logger并设置其日志级别为DEBUG
def getLogger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # 创建一个流处理器handler并设置其日志级别为DEBUG
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)

    # 创建一个格式器formatter并将其添加到处理器handler
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)

    # 为日志器logger添加上面创建的处理器handler
    logger.addHandler(handler)
    # 日志输出
    # logger.debug('debug message')
    # logger.info('info message')
    # logger.warn('warn message')
    # logger.error('error message')
    # logger.critical('critical message')

    return logger
