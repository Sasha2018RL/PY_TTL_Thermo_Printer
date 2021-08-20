n = -1  # placeholder

b_reset = [27, 64]
b_char_spacing = [27, 32, n]  # отступ слева перед символом, n*0.125mm
b_print_mode_reset = [27, 33, 0]  # сброс всех настроек ниже
b_print_mode_font_b = [27, 33, 1]  # font b
# b_print_mode_bold = [27, 33, 8]  # жирный режим - отдельной командой
b_print_mode_times_higher = [27, 33, 16]  # двойная высота
b_print_mode_2width = [27, 33, 32]  # двойная ширина
b_print_pos = [27, 36, n, n]  # абсолютное начало строки. (n1 + n2*255) * 0.125mm
b_underline_none = [27, 45, 0]  # убрать подчеркивание
b_underline_1pt = [27, 45, 1]  # подчеркивание 1pt
b_underline_2pt = [27, 45, 2]  # подчеркивание 2pt
b_set_line_spacing_default = [27, 50]  # стандартное (3.75мм) расстояние между строками
b_set_line_spacing = [27, 51, n]  # установить межстрочный интервал n*0.125mm
b_set_bold_printing_mode = [27, 69, n]  # установить (1) или отключить (0) жирный режим
b_overlapping_mode = [27, 71, n]  # режим печати поверх (1/0), не понятно зачем
b_print_and_feed = [27, 74, n]  # отпечатать буфер, и прокрутить бумагу на n*0.125mm
b_rotate_90 = [27, 86, n]  # переворот на 90 градусов (0/1)
b_align_left = [27, 97, 0]  # выравнивание по левому краю
b_align_center = [27, 97, 1]  # выравнивание по центру
b_align_right = [27, 97, 2]  # выравнивание по правому краю
b_print_and_feed_lines = [27, 100, n]  # апечатать буфер, и прокрутить на n строк
b_set_ru_lang = [27, 116, 6]  # установить WCP1251
b_inverted = [29, 66, n]  # инвертированный режим 1/0
