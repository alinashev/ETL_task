from logzero import logger, logfile


class Logger:
    @staticmethod
    def write_log(log):
        logfile('Logs/logs.log')
        logger.info(log)

    @staticmethod
    def write_error(error):
        logfile('Logs/errors.log')
        logger.error(error)