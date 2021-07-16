import logging

LOG_FORMAT = "%(asctime)s %(levelname)8s - %(message)s"
# escape sequence \n: new line, \t: tab, \r: return, \": "
logging.basicConfig(filename=r"C:\Users\12818\workspace\Terry\python1\jwang.log", level=logging.DEBUG, format=LOG_FORMAT)
# create an instance of class
logger = logging.getLogger("Huaxia")

logger.debug("My first debug message.")
logger.info("My first info message.")
logger.warning("My first warning message.")
logger.error("My first error message.")
logger.fatal("My first fatal message.")
print(logger.level)
