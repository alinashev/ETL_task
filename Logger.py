from logzero import logger, logfile


class Logger:
    @staticmethod
    def write_log(log):
        logfile('logs.log')
        logger.info(log)

    @staticmethod
    def write_error(error):
        logfile('errors.log')
        logger.error(error)