from Log.logger import logger


def log(func_to_log):
    """Функция-декоратор."""

    def log_saver(*args, **kwargs):
        ret = func_to_log(*args, **kwargs)
        logger.info(f'Была вызвана функция {func_to_log.__name__} c параметрами {args}, {kwargs}. '
                    f'Вызов из модуля {func_to_log.__module__}')
        return ret

    return log_saver
