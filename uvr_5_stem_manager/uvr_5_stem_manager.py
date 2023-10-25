#!/usr/bin/python
# -*- coding: utf-8 -*-


import os
import glob
from pathlib import Path
import tkinter as tk
from tkinter import filedialog


dict_constants = {
    'shared_ending_1': '*.mp3', 
    'shared_ending_2': '*.flac', 
    'shared_ending_3': '*.wav', 
    'dir_mask': 'Ensembled_Outputs_*', 
    '': r'', 
}


def get_dir_from_gui(initial_directory):
    # Создается объект графического интерфейса Tkinter, представляющий основное окно для диалогового окна.
    root = tk.Tk()
    # Устанавливается атрибут окна Tkinter, чтобы оно оставалось поверх других окон. Это делает окно верхним по отношению ко всем остальным окнам.
    root.wm_attributes('-topmost', True)
    # Основное окно Tkinter временно скрывается, так как оно не будет отображаться, но останется активным для обработки событий.
    root.withdraw()

    # Вызывается диалоговое окно для выбора директории
    initial_dir = filedialog.askdirectory(initialdir=initial_directory, 
                                        title=f'Choose your directory which contains stems and "Ensembled_Outputs_*" catalogues', 
                                        )
        
    # Основное окно Tkinter разрушается, завершая работу графического интерфейса Tkinter.
    root.destroy()

    return initial_dir


def mkdirs_replace_and_delete_old_dirs(extention, initial_dir):

    k_ending = extention
    # Список полных путей к файлам
    ls_files = glob.glob(rf'{initial_dir}\{dict_constants[k_ending]}')

    if len(ls_files) > 0:
        # создание каталогов
        ls_dst_dirs = []
        for full_path in ls_files[:]:
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
            for full_path in glob.glob(rf'{initial_dir}\{dict_constants[k_ending]}') + glob.glob(rf'{initial_dir}\{dict_constants[k]}\{dict_constants[k_ending]}'):

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
        for dir_to_delete in glob.glob(rf'{initial_dir}\{dict_constants[k]}'):
            if len(glob.glob(rf'{dir_to_delete}\*.*')) == 0:
                os.rmdir(dir_to_delete)


def main():

    # k = 'initial_dir'
    # initial_dir = dict_constants[k]

    initial_dir = get_dir_from_gui(Path(__file__).parents[1].resolve())

    for ext in ['shared_ending_1', 'shared_ending_2', 'shared_ending_3', ]:
        mkdirs_replace_and_delete_old_dirs(ext, initial_dir)


if __name__ == '__main__':
     main()
