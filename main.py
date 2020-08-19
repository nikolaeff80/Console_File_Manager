import sys

from core import get_list, create_file, create_folder, delete_file, copy_file, print_help, change_dir

try:
    command = sys.argv[1]
except IndexError:
    print('Необходимо выбрать команду. Для помощи help')
else:
    if command == 'list':
        get_list()
    elif command == 'list_True':
        get_list(True)
    elif command == 'create_file':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Требуется указать имя файла')
        else:
            create_file(name)
    elif command == 'create_folder':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Требуется указать имя директории')
        else:
            create_folder(name)
    elif command == 'chd':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Необходимо указать имя директории')
        else:
            change_dir(name)
    elif command == 'delete':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Требуется указать имя директории или файла')
        else:
            delete_file(name)
    elif command == 'copy':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Требуется указать имя директории или файла')
        else:
            try:
                new_name = sys.argv[3]
            except IndexError:
                print('Требуется указать новое имя директории или файла')
            else:
                copy_file(name, new_name)
    elif command == 'help':
        print_help()
