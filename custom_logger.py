import os
import logging

logger = logging.getLogger('root')

def get_custom_logger(logger_name, logger_fname, level=logging.DEBUG):
    """
    Method to return a custom logger with the given name and level
    """
    logger = logging.getLogger(logger_name)
    logger.setLevel(level)
    format_string = ("%(asctime)s %(message)s")
    log_format = logging.Formatter(format_string)
    # Creating and adding the console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_format)
    logger.addHandler(console_handler)
    # Creating and adding the file handler
    file_handler = logging.FileHandler(str(logger_fname), mode='a')
    file_handler.setFormatter(log_format)
    logger.addHandler(file_handler)

    file_handler_clean = logging.FileHandler(str(logger_fname).replace('.log', '')+'_clean.log', mode='a')
    file_handler_clean.setFormatter(logging.Formatter(("%(message)s")))
    logger.addHandler(file_handler_clean)
    return logger

logger = get_custom_logger("root", log_file_path)
