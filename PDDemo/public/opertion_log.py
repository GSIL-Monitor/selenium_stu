"""
__author__ = 'LZL'
"""
import logging
import os

class operation_log:
    '''对日志文件的操作'''

    def __init__(self, log_path, log_level=logging.DEBUG):
        '''
        filename：用指定的文件名创建FiledHandler（后边会具体讲解handler的概念），这样日志会被存储在指定的文件中。
        filemode：文件打开方式，在指定了filename时使用这个参数，默认值为“a”还可指定为“w”。
        format：指定handler使用的日志显示格式。
        datefmt：指定日期时间格式。
        level：设置rootlogger的日志级别
        stream：用指定的stream创建StreamHandler。可以指定输出到sys.stderr,sys.stdout或者文件，默认为sys.stderr。若同时列出了filename和stream两个参数，则stream参数会被忽略。
        '''
        logging.basicConfig(level=log_level,
                            format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                            datefmt='%Y %H:%M:%S',
                            filename=log_path,
                            # 追加写入
                            filemode='a+')

    def debug(self, message):
        '''
        设置日志的DEBUG级别的内容
        @param message: 内容
        @return: null
        '''
        logging.debug(message)

    def info(self, message):
        '''
        设置日志的INFO级别的内容
        @param message: 内容
        @return: null
        '''
        logging.info(message)


    def warn(self, message):
        '''
        设置日志的WAR级别的内容
        @param message: 内容
        @return: null
        '''
        logging.warning(message)

    def error(self, message):
        '''
        设置日志的ERROR级别的内容
        @param message: 内容
        @return: null
        '''
        logging.error(message)


    def cri(self, message):
        '''
        设置日志的critical级别的内容
        @param message: 内容
        @return: null
        '''
        logging.critical(message)

if __name__ == '__main__':
    # log_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'report')
    # 想要获取的是当前项目的路径再进行拼接，用os.getcwd()
    log_path = os.path.join(os.path.dirname(os.getcwd()), 'File', 'log.log')
    log_level = logging.ERROR
    logger = operation_log(log_path, log_level)

    logger.debug('debug message')
    logger.info('info message')
    logger.warn('warning message')
    logger.error('error message')
    logger.cri('critical message')

