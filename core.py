import os
import shutil

from Log.log_decorator import log
from Log.logger import logger


@log
def create_file(name, text=None):
    with open(name, 'w', encoding='utf-8') as f:
        if text:
            f.write(text)


@log
def create_folder(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        logger.critical(f'Директория {name} уже существует')


@log
def get_list(folders_only=False):
    result = os.listdir()
    if folders_only:
        result = [f for f in result if os.path.isdir(f)]
    print(result)


@log
def delete_file(name):
    if os.path.isdir(name):
        os.rmdir(name)
    else:
        os.remove(name)


@log
def change_dir(name):
    os.chdir(name)
    logger.info(f'Смена рабочей директории на {os.getcwd()}')
    print(os.getcwd())


@log
def copy_file(name, new_name):
    if os.path.isdir(name):
        shutil.copytree(name, new_name)
    else:
        shutil.copy(name, new_name)


def print_help():
    """
    Commands in help
    :return:
    """
    print('Поддерживаемые команды:')
    print('list - список файлов и директорий')
    print('list_True - список директорий')
    print('create_file - создание файла')
    print('create_folder - создание директории')
    print('delete - удаление файла или директории')
    print('copy - копирование файла или директории')
    print('help - вывести подсказки по командам')
    print('exit - выход из программы')


# Отладка

if __name__ == '__main__':
    create_file('test.dat')
    create_file('test.dat', 'test text')
    create_folder('test_folder 1')
    get_list()
    get_list(True)
    delete_file('test.dat')
    delete_file('test_folder 1')
    copy_file('test.dat', 'new_test.dat')
    copy_file('test_folder 1', 'new_test_folder 1')
