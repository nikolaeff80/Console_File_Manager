import logging
import os
import sys

sys.path.append('../')

# создаём формировщик логов (formatter):
fm_formatter = logging.Formatter('%(asctime)s %(levelname)s %(filename)s %(message)s')

# Подготовка имени файла для логирования
path = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(path, 'file_m.log')

# создаём потоки вывода логов
steam = logging.StreamHandler(sys.stderr)
steam.setFormatter(fm_formatter)
steam.setLevel(logging.WARNING)
log_file = logging.FileHandler(path, encoding='utf8')
log_file.setFormatter(fm_formatter)

# создаём регистратор и настраиваем его
logger = logging.getLogger('file_logger')
logger.addHandler(steam)
logger.addHandler(log_file)
logger.setLevel(logging.DEBUG)

# отладка
if __name__ == '__main__':
    logger.critical('Test critical event')
    logger.error('Test error ivent')
    logger.debug('Test debug ivent')
    logger.info('Test info ivent')
