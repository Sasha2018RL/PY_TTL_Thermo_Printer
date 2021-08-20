import serial

from printer import Printer
from printer import bytecodes

ser = serial.Serial("/dev/serial0", 9600)

printer = Printer(ser)

printer.init()

printer.set_char_spacing(1)
printer.println('1 mm char spacing')
printer.reset()

printer.println('шрифт А font A')
printer.font_b()
printer.println('шрифт Б font B')
printer.font_a()

printer.en_double_height()
printer.println('Double height выс')
printer.en_double_width()
printer.println('2H 2W шир выс')
printer.ds_double_height()
printer.en_double_width()
printer.println('2 Width шир')
printer.reset_print_mode()

printer.print_margin('margin 1cm маргин 1', 10)

printer.underline_1px()
printer.println('1px underline подч')

printer.underline_2px()
printer.println('2px underline подч')

printer.ds_underline()
printer.println('no underline не подч')

printer.println('line spacing 0 межст')
printer.set_line_spacing(0)
printer.println('line spacing 2mm межстр')
printer.set_line_spacing(2)
printer.println('default line spacing стандарт')
printer.default_line_spacing()

printer.en_bold()
printer.println('Жирный режим BOLD')
printer.ds_bold()

printer.rotate_90()
printer.println('rotated перевернутый')
printer.rotate_back_90()

printer.println('left лвый край')
printer.align_center()
printer.println('center центр')
printer.align_right()
printer.println('right справа')
printer.align_left()

printer.en_invert()
printer.println('Инвертированный текст')
printer.ds_invert()

printer.print_and_feed('Отпечатать и промотать 1мм', 1)
printer.print_and_feed_lines('Отпечатать и промотать 3 строки', 3)
