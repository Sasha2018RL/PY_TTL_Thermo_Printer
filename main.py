from time import sleep

import serial

from printer import Printer
from printer import bytecodes

ser = serial.Serial("/dev/serial0", 9600)

printer = Printer(ser)

sleep(4)
printer.en_bold()
printer.print_and_feed_lines("Не ответивший на это сообщение любит пЭнисы", 3)