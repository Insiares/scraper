import logging
import os


def init_logger():

    log_file_path = 'logs/app.log'
    log_folder = os.path.dirname(log_file_path)
    if not os.path.exists(log_folder):
        os.makedirs(log_folder)

    if not os.path.isfile(log_file_path):
        with open(log_file_path, 'w'):
            pass  # Créez simplement le fichier vide

    format_string = '%(asctime)s - %(levelname)s - %(message)s'
    logger = logging.basicConfig(level=logging.INFO,
                                 format=format_string,
                                 datefmt='[%d/%b/%Y %H:%M:%S]')
    file_handler = logging.FileHandler(log_file_path)
    file_handler.setLevel(logging.INFO)
    formatter = logging.Formatter(format_string, datefmt='[%d/%b/%Y %H:%M:%S]')
    file_handler.setFormatter(formatter)
    logging.getLogger(logger).addHandler(file_handler)

    return logger, file_handler
