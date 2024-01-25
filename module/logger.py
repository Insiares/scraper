import logging


def init_logger():

    format_string = '%(asctime)s - %(levelname)s - %(message)s'
    logger = logging.basicConfig(level=logging.INFO,
                                 format=format_string,
                                 datefmt='[%d/%b/%Y %H:%M:%S]')
    file_handler = logging.FileHandler('./logs/app.log')
    file_handler.setLevel(logging.INFO)
    formatter = logging.Formatter(format_string, datefmt='[%d/%b/%Y %H:%M:%S]')
    file_handler.setFormatter(formatter)
    logging.getLogger(logger).addHandler(file_handler)

    return logger, file_handler
