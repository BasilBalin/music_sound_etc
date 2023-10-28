#!/usr/bin/python
# -*- coding: utf-8 -*-


import glob
import platform
from pathlib import Path
import os


dict_constants = {
    'shared_ending_1': '*.mp3', 
    'shared_ending_2': '*.flac', 
    'shared_ending_3': '*.wav', 
    'dir_mask': 'Ensembled_Outputs_*', 
    '': r'', 
}


if platform.system() == 'Windows':
    sys = 0
elif platform.system() in ['Darwin', 'Linux']:
    sys = 1
else:
    sys = 1

slashes = ['\\', '/', ]


def mkdirs_replace_and_delete_old_dirs(extention, initial_dir):

    k_ending = extention
    # Список полных путей к файлам
    ls_files = glob.glob(rf'{initial_dir}{slashes[sys]}{dict_constants[k_ending]}')

    if len(ls_files) > 0:
        # создание каталогов
        ls_dst_dirs = []
        for full_path in ls_files[:]:
            # Преобразуйте полный путь в объект Path
            path = Path(full_path)
            # Извлеките имя файла без расширения
            file_name_without_extension = path.stem
            # создаём папку с названием как у файла
            dst_dir = rf'{initial_dir}{slashes[sys]}{file_name_without_extension}'
            if not os.path.exists(dst_dir):
                os.mkdir(dst_dir)
            ls_dst_dirs.append(dst_dir)

        for dst_dir in ls_dst_dirs:

            # поиск и перемещение файлов
            k = 'dir_mask'
            for full_path in glob.glob(rf'{initial_dir}{slashes[sys]}{dict_constants[k_ending]}') + glob.glob(rf'{initial_dir}{slashes[sys]}{dict_constants[k]}{slashes[sys]}{dict_constants[k_ending]}'):

                for f_type in ["_(Vocals)", "_(Instrumental)", ]:
                    
                    full_path_by_f_type = full_path.split(f_type)

                    if len(full_path_by_f_type) > 1 and f_type in dst_dir and Path(dst_dir).name.split(f_type)[0] in full_path:
                        # Путь к исходному файлу
                        src = Path(full_path)
                        # Путь, куда нужно переместить (переименовать) файл
                        dst = Path(rf'{dst_dir}{slashes[sys]}{src.name}')
                        # Перемещаем (переименовываем) файл
                        src.rename(dst)

        # удалим лишние папки
        for dir_to_delete in glob.glob(rf'{initial_dir}{slashes[sys]}{dict_constants[k]}'):
            if len(glob.glob(rf'{dir_to_delete}{slashes[sys]}*.*')) == 0:
                os.rmdir(dir_to_delete)


def main():

    initial_dir = Path(__file__).parent.resolve()

    for ext in ['shared_ending_1', 'shared_ending_2', 'shared_ending_3', ]:
        mkdirs_replace_and_delete_old_dirs(ext, initial_dir)


if __name__ == '__main__':
     main()
