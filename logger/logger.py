# -*- coding: utf-8 -*-

from loguru import logger

# logger.add('file_{time}.log')

# 每天12:00会创建日志文件
logger.add('file_2.log', rotation="16:30")

# 超过1MB，创建日志文件
logger.add('file_1.log', rotation="1 MB")

# 压缩日志
logger.add('file_1.log', compression="zip")

logger.debug("That's it, beautiful and simple logging!")