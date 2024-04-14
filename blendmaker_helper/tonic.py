#!/usr/bin/python
# -*- coding: utf-8 -*-

# todo: вынести библиотеки с нотами в отдельный файл

dict_cyrillic = {
    'dict_sharp_flat': {'dict_sharp_dur_moll': {'ls_dur_sharp': (
                                                                 'До',
                                                                 'До#',
                                                                 'Ре',
                                                                 None,
                                                                 'Ми',
                                                                 'Фа',
                                                                 'Фа#',
                                                                 'Соль',
                                                                 None,
                                                                 'Ля',
                                                                 None,
                                                                 'Си',
                                                                 ),
                                                'ls_moll_sharp': (
                                                                  'до',
                                                                  'до#',
                                                                  'ре',
                                                                  'ре#',
                                                                  'ми',
                                                                  'фа',
                                                                  'фа#',
                                                                  'Соль',
                                                                  'Соль#',
                                                                  'ля',
                                                                  'ля#',
                                                                  'си',
                                                                  ),
                                                },
                        'dict_flat_dur_moll': {'ls_dur_flat': (
                                                               'До',
                                                               'Реb',
                                                               'Ре',
                                                               'Миb',
                                                               'Ми',
                                                               'Фа',
                                                               'Сольb',
                                                               'Соль',
                                                               'Ляb',
                                                               'Ля',
                                                               'Сиb',
                                                               'Си',
                                                               ),
                                               'ls_moll_flat': (
                                                                'до',
                                                                None,
                                                                'ре',
                                                                'миb',
                                                                'ми',
                                                                'фа',
                                                                None,
                                                                'соль',
                                                                'ляb',
                                                                'ля',
                                                                'сиb',
                                                                'си',
                                                                ),
                                               }, },
                }

dict_lat = {
    'dict_sharp_flat': {'dict_sharp_dur_moll': {'ls_dur_sharp': (
                                                                 'C',
                                                                 'Cis',
                                                                 'D',
                                                                 None,
                                                                 'E',
                                                                 'F',
                                                                 'Fis',
                                                                 'G',
                                                                 None,
                                                                 'A',
                                                                 None,
                                                                 'B',
                                                                 ),
                                                'ls_moll_sharp': (
                                                                  'c',
                                                                  'cis',
                                                                  'd',
                                                                  'dis',
                                                                  'e',
                                                                  'f',
                                                                  'fis',
                                                                  'g',
                                                                  'gis',
                                                                  'a',
                                                                  'ais',
                                                                  'b'
                                                                  ),
                                                },
                        'dict_flat_dur_moll': {'ls_dur_flat': (
                                                               'C',
                                                               'Des',
                                                               'D',
                                                               'Es',
                                                               'E',
                                                               'F',
                                                               'Ges',
                                                               'G',
                                                               'As',
                                                               'A',
                                                               'Bes',
                                                               'B',
                                                               ),
                                               'ls_moll_flat': (
                                                                 'c',
                                                                 None,
                                                                 'd',
                                                                 'es',
                                                                 'e',
                                                                 'f',
                                                                 None,
                                                                 'g',
                                                                 'as',
                                                                 'a',
                                                                 'bes',
                                                                 'b',
                                                                 ),
                                               }, },
                }

dict_pitch_classes = {
    'dict_sharp_flat': {'dict_sharp_dur_moll': {'ls_dur_sharp': (
                                                                 'C',
                                                                 'C#',
                                                                 'D',
                                                                 None,
                                                                 'E',
                                                                 'F',
                                                                 'F#',
                                                                 'G',
                                                                 None,
                                                                 'A',
                                                                 None,
                                                                 'B'
                                                                 ),
                                                'ls_moll_sharp': (
                                                                  'c',
                                                                  'c#',
                                                                  'd',
                                                                  'd#',
                                                                  'e',
                                                                  'f',
                                                                  'f#',
                                                                  'g',
                                                                  'g#',
                                                                  'a',
                                                                  'a#',
                                                                  'b'),

                                                },
                        'dict_flat_dur_moll': {'ls_dur_flat': (
                                                               'C',
                                                               'Db',
                                                               'D',
                                                               'Eb',
                                                               'E',
                                                               'F',
                                                               'Gb',
                                                               'G',
                                                               'Ab',
                                                               'A',
                                                               'Bb',
                                                               'B'
                                                               ),
                                               'ls_moll_flat': (
                                                                'c',
                                                                None,
                                                                'd',
                                                                'eb',
                                                                'e',
                                                                'f',
                                                                None,
                                                                'g',
                                                                'ab',
                                                                'a',
                                                                'bb',
                                                                'b'
                                                                ),

                                               }, },
                }

dict_camelot = {
    'dict_sharp_flat': {'dict_sharp_dur_moll': {'ls_dur_sharp': (
                                                                 '8B',
                                                                 '3B',
                                                                 '10B',
                                                                 None,
                                                                 '12B',
                                                                 '7B',
                                                                 '2B',
                                                                 '9B',
                                                                 None,
                                                                 '11B',
                                                                 None,
                                                                 '1B',
                                                                 ),
                                                'ls_moll_sharp': (
                                                                  '8A',
                                                                  '3A',
                                                                  '10A',
                                                                  '5A',
                                                                  '12A',
                                                                  '7A',
                                                                  '2A',
                                                                  '9A',
                                                                  '4A',
                                                                  '11A',
                                                                  '6A',
                                                                  '1A',
                                                                  ),
                                                },
                        'dict_flat_dur_moll': {'ls_dur_flat': (
                                                               '8B',
                                                               '3B',
                                                               '10B',
                                                               '5B',
                                                               '12B',
                                                               '7B',
                                                               '2B',
                                                               '9B',
                                                               '4B',
                                                               '11B',
                                                               '6B',
                                                               '1B',
                                                               ),
                                               'ls_moll_flat': (
                                                                '8A',
                                                                None,
                                                                '10A',
                                                                '5A',
                                                                '12A',
                                                                '7A',
                                                                None,
                                                                '9A',
                                                                '4A',
                                                                '11A',
                                                                '6A',
                                                                '1A',
                                                                ),
                                               }, },
                }

tup_dicts_with_notes = (
    dict_cyrillic,
    dict_lat,
    dict_pitch_classes,
    dict_camelot,
    )

tup_names_of_notation = (
    'Кириллица',
    'Латиница',
    'Программный тип записи',
    'Колесо Камелота',
    )


# -- f --

def get_all_the_types_of_notation_of_the_key():
    # show all supported input
    for i, dict in enumerate(tup_dicts_with_notes):
        for key_0, val_0 in dict.items():
            for key_1, val_1 in val_0.items():
                for key_2, tup_notes in val_1.items():
                    assert len(tup_notes) == 12, 'Кол-во нот в списке-'
                    f'константе "{tup_names_of_notation[i], key_2}" '
                    'отличается от 12!'
                    print(f'{tup_names_of_notation[i]}: '
                          f'{key_2},    {tup_notes}')

    user_s_note = input('''
Введи ноту так, как в одном из предложенных
выше вариантов (без кавычек):
                         ''')

    def input_is_correct(note):
        # значения на случай, если не пройдём проверку
        # j - индекс ноты в любом из списков-констант
        flag, ls_results = False, []
        for i, dict in enumerate(tup_dicts_with_notes):
            # спускаемся на нужное кол-во уровней вложенности словарей
            for name_dict_sharp_or_flat, dict_sharp_or_flat in dict.items():
                for name_dict_dur_or_moll, dict_dur_or_moll in dict_sharp_or_flat.items():
                    for name_ls_notes, ls_notes in dict_dur_or_moll.items():
                        # если проверка пройдена,
                        if note in ls_notes:
                            # меняем значения
                            j = ls_notes.index(note)
                            # диезы или бемоли
                            sharp_or_flat = name_dict_sharp_or_flat
                            # мажор или минор
                            dur_moll = name_dict_dur_or_moll
                            # имя итогового списка нот
                            total_ls_notes = name_ls_notes
                            name_of_notation = tup_names_of_notation[i]
                            flag = True
                            ls_results.append((name_of_notation, sharp_or_flat, dur_moll, total_ls_notes, j))
        # вернём неизменённые исходные значение, если ввод не подошёл
        # или изменённые, если подошёл
        return flag, ls_results

    flag, ls_results_of_input = input_is_correct(user_s_note)

    assert flag, '''
    Введённая вами нота не совпадает ни с одним из предложенных вариантов.
    Для верности просто скопируйте её из предложенного списка и 
    вставьте в командную строку.
    '''

    ls_results_to_print = []
    ls_results_to_calc = []
    # для каждого списка нот, в котором нашлась введённая пользователем нота,
    # у нас есть набор данных: пары "ключ-значение"
    # эти "координаты" хранятся в кортежах (если их больше одного) в
    # списке ls_results_of_input
    for i in range(len(ls_results_of_input)):
        # извлекаем из кортежа "координаты"
        inputted_name_of_notation, inputted_sharp_and_flat, inputted_dur_and_moll, inputted_dur_or_moll, j = ls_results_of_input[i]
        # для каждого типа записи нот
        for l, name_of_notation in enumerate(tup_names_of_notation):
            # if inputted_name_of_notation != name_of_notation:
            # для минора или мажора
            for sharp_and_flat in tup_dicts_with_notes[l]:
                if inputted_sharp_and_flat == sharp_and_flat:
                    for dur_and_moll in tup_dicts_with_notes[l][inputted_sharp_and_flat]:
                        if inputted_dur_and_moll == dur_and_moll:
                            tup_with_notes = tup_dicts_with_notes[l][inputted_sharp_and_flat][inputted_dur_and_moll][inputted_dur_or_moll]
                            print(tup_dicts_with_notes[l][inputted_sharp_and_flat][inputted_dur_and_moll][inputted_dur_or_moll])
                            note = tup_with_notes[j]

                            ls_results_to_print.append(f'"{name_of_notation}": {inputted_dur_and_moll.replace("ls_", "")}, нота "{note}"')
                            ls_results_to_calc.append((name_of_notation, inputted_dur_and_moll, note))

    print(ls_results_to_print)

    return ls_results_to_calc


def shift_n_base_12(camelot_key, small_shift=0, shift=5):
    """функция, которая "прыгает" на заданный интервал от
    той ноты, которая задана в форме записи Колеса Камелота (без буквы)
    и позволяет по исходной ноте определить новую, в этой системе нотации

    Args:
        camelot_key (str): исходный номер ноты в системе
        нотации `Колесо Камелота`
        small_shift (int, optional): интервал, на
        который мы можем подвинуть трек,
        не транспонируя его, без ущерба для гармонии. Defaults to 0.
        base (int, optional): интервал, выраженный в числе сегментов `Колеса`.
          Defaults to 5.

    Returns:
        str: новый номер ноты в системе нотации `Колесо Камелота`
    """
    # разделим на время букву и номер ноты
    letter = camelot_key[-1].upper()
    camelot_key = int(camelot_key[:-1])

    camelot_key = (camelot_key + small_shift + shift) % 12
    camelot_key = 12 if camelot_key == 0 else camelot_key

    # соединим обратно в результат
    return f'{str(camelot_key)}{letter}'


def how_much_to_pitch_shift_the_second_track(first_key, second_key):
    first_letter = first_key[-1].upper()
    second_letter = second_key[-1].upper()

    # first_key = int(first_key[:-1])
    # second_key = int(second_key[:-1])

    if first_letter == second_letter:
        tup_avaible_keys = (-1, 0, 1, )
    else:
        tup_avaible_keys = (0, )

    for result_shift in (0, -1, +1, -2, +2, -3, +3, -4, +4, -5, +5, ):
        for avaible_key in tup_avaible_keys:
            if shift_n_base_12(second_key, avaible_key,
                               result_shift * -5)[:-1] == first_key[:-1]:
                if result_shift > 2:
                    print('''
Ниже приведено суммарное значение сдвига акапеллы относительно
инструментала. Однако менять высоту каждого трека больше, чем на
2 полутона не рекомендуется.
                          ''')
                if result_shift == 0:
                    print('\nМенять высоту акапеллы не требуется')
                elif result_shift < 0:
                    print('\nАкапеллу нужно '
                          f'опустить на столько полутонов:\n{result_shift}')
                elif result_shift > 0:
                    print('\nАкапеллу нужно '
                          f'поднять на столько полутонов:\n{result_shift}')
                return result_shift

    print('\nОтсутствует близкая по тону '
          'тональность для гарминического сведения')
    return '-'


def body():
    while True:
        user_answer = input('\nВыбери один вариант. Узнать ноту в других '
                            'видах записи ("1") или определить, на сколько '
                            'полутонов опустить либо поднять акапеллу '
                            'относительно инструментала (любая другая '
                            'клавиша): ')
        if user_answer == '1':
            print()
            get_all_the_types_of_notation_of_the_key()
        else:
            first_key = input('\nВведи тональность инструментала в системе'
                              ' "Колесо Камелота": ')
            second_key = input('\nВведи тональность акапеллы в системе'
                               ' "Колесо Камелота": ')
            how_much_to_pitch_shift_the_second_track(first_key, second_key)


if __name__ == "__main__":
    print('Приветствую, блендмейкер! Я твой скромный помощник.')
    body()
else:
    print('Пользовательская библиотека импортирована.')
