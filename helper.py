import logging
import logging.config


def config_logger(app):
    logging.config.dictConfig(app.config.get("LOGGING_CONFIG"))
    logger = logging.getLogger(app.config.get("DEFAULT_LOGGER_NAME"))
    app.logger.addHandler(logger)
    app.logger.info("hello")
