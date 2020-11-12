import os,inspect
import sys
sys.path.append('../')
from logging.handlers import TimedRotatingFileHandler
import requests
import logging
logdir = './log'
try:
    os.mkdir(logdir)
except Exception as e:
    pass


scriptName = os.path.basename(sys.argv[0].replace('.py', ''))
frame = inspect.stack()[-1]
caller_filename = frame[0].f_code.co_filename
log_basename = os.path.splitext(os.path.basename(caller_filename))[0]
LOG_FORMAT = '[%(asctime)s] %(levelname)8s - %(name)s - %(message)s'
logFileName = logdir + os.sep + \
    '{}.log'.format(log_basename)


Handler = TimedRotatingFileHandler(logFileName, when="midnight", interval=1, encoding='utf-8', backupCount=30)




if __name__ == '__main__':
    print(log_basename)
    print(scriptName)
