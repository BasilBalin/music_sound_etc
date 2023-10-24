#!/usr/bin/python
# -*- coding: utf-8 -*-


import os
import glob
from pathlib import Path


dict_file_names = {
    'initial_dir': r'D:\sep\o', 
    'shared_ending_1': '*.mp3', 
    'shared_ending_2': '*.flac', 
    'shared_ending_3': '*.wav', 
    'dir_mask': 'Ensembled_Outputs_*', 
    '': r'', 
}


def mkdirs_replace_and_delete_old_dirs(extention):

    k = 'initial_dir'
    initial_dir = dict_file_names[k]

    k_ending = extention
    # Список полных путей к файлам
    ls_files = glob.glob(rf'{initial_dir}\{dict_file_names[k_ending]}')

    # создание каталогов
    ls_dst_dirs = []
    for full_path in ls_files[:]:  # СНЯТЬ ОГРАНИЧЕНИЕ!
        # Преобразуйте полный путь в объект Path
        path = Path(full_path)
        # Извлеките имя файла без расширения
        file_name_without_extension = path.stem
        # создаём папку с названием как у файла
        dst_dir = rf'{initial_dir}\{file_name_without_extension}'
        if not os.path.exists(dst_dir):
            os.mkdir(dst_dir)
        ls_dst_dirs.append(dst_dir)

    for dst_dir in ls_dst_dirs:

        # поиск и перемещение файлов
        k = 'dir_mask'
        for full_path in glob.glob(rf'{initial_dir}\{dict_file_names[k_ending]}') + glob.glob(rf'{initial_dir}\{dict_file_names[k]}\{dict_file_names[k_ending]}'):

            for f_type in ["_(Vocals)", "_(Instrumental)", ]:
                
                full_path_by_f_type = full_path.split(f_type)

                if len(full_path_by_f_type) > 1 and f_type in dst_dir and Path(dst_dir).name.split(f_type)[0] in full_path:
                    # Путь к исходному файлу
                    src = Path(full_path)
                    # Путь, куда нужно переместить (переименовать) файл
                    dst = Path(rf'{dst_dir}\{src.name}')
                    # Перемещаем (переименовываем) файл
                    src.rename(dst)

    # удалим лишние папки
    for dir_to_delete in glob.glob(rf'{initial_dir}\{dict_file_names[k]}'):
        if len(glob.glob(rf'{dir_to_delete}\*.*')) == 0:
            os.rmdir(dir_to_delete)


def main():
     for ext in ['shared_ending_1', 'shared_ending_2', 'shared_ending_3', ]:
        mkdirs_replace_and_delete_old_dirs(ext)


if __name__ == '__main__':
     main()