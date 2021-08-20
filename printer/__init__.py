import printer.bytecodes


class Printer:
    def __init__(self, serial):
        self.serial = serial

    def print(self, string):
        self.serial.write(string.encode('utf8'))

    def println(self, string):
        self.print(string + '\r\n')

    def send_command(self, command, params=None):
        if params is None:
            params = []
        cmd = []
        n_index = 0
        for byte in command:
            if byte == bytecodes.n:
                if isinstance(params, list):
                    if len(params) <= n_index:
                        byte = 0
                    else:
                        byte = params[n_index]
                else:
                    byte = params
                n_index += 1

            cmd.append(byte)
        print(cmd)
        self.serial.write(cmd)

    def init(self):
        self.reset()
        self.send_command(bytecodes.b_set_ru_lang)

    def reset(self):
        print('reset')
        self.send_command(bytecodes.b_reset)

    def set_char_spacing(self, spacing=0.125):
        points = self.__mm_to_points__(spacing)
        print(f'char_spacing: {spacing} mm ({points})')
        self.send_command(bytecodes.b_char_spacing)

    def reset_print_mode(self):
        self.send_command(bytecodes.b_print_mode_reset)
        print('reset print mode')

    def font_b(self):
        self.send_command(bytecodes.b_print_mode_font_b)
        print('set font B')

    def font_a(self):
        self.reset_print_mode()

    def en_double_height(self):
        self.send_command(bytecodes.b_print_mode_times_higher)
        print('double height')

    def ds_double_height(self):
        self.reset_print_mode()

    def en_double_width(self):
        self.send_command(bytecodes.b_print_mode_2width)
        print('double width')

    def ds_double_width(self):
        self.reset_print_mode()

    def print_margin(self, text, margin=1):
        self.send_command(bytecodes.b_print_pos, self.__mm_to_points__(margin))
        self.println(text)
        print(f'margin set to {margin}')

    def underline_1px(self):
        self.send_command(bytecodes.b_underline_1pt)
        print('underline 1pt')

    def underline_2px(self):
        self.send_command(bytecodes.b_underline_2pt)
        print('underline 2pt')

    def ds_underline(self):
        self.send_command(bytecodes.b_underline_none)
        print('underline disabled')

    def default_line_spacing(self):
        self.send_command(bytecodes.b_set_line_spacing_default)
        print('line spacing set to 3.75 mm (default)')

    def set_line_spacing(self, spacing):
        self.send_command(bytecodes.b_set_line_spacing, self.__mm_to_points__(spacing))
        print(f'line spacing set to {spacing} mm')

    def en_bold(self):
        self.send_command(bytecodes.b_set_bold_printing_mode, 1)
        print('bold mode enabled')

    def ds_bold(self):
        self.send_command(bytecodes.b_set_bold_printing_mode, 0)
        print('bold mode disabled')

    def print_and_feed(self, line, feed_mm=1):
        self.print(line)
        self.send_command(bytecodes.b_print_and_feed, self.__mm_to_points__(feed_mm))
        print(f'{line} + feed {feed_mm}')

    def rotate_90(self):
        self.send_command(bytecodes.b_rotate_90, 1)
        print('rotated for 90 deg')

    def rotate_back_90(self):
        self.send_command(bytecodes.b_rotate_90, 0)
        print('disabled rotation for 90 deg')

    def align_left(self):
        self.send_command(bytecodes.b_align_left)
        print('aligned left')

    def align_center(self):
        self.send_command(bytecodes.b_align_center)
        print('aligned center')

    def align_right(self):
        self.send_command(bytecodes.b_align_right)
        print('aligned right')

    def print_and_feed_lines(self, text, lines=3):
        self.print(text)
        self.send_command(bytecodes.b_print_and_feed_lines, lines)
        print(f'{text} + {lines} feed')

    def en_invert(self):
        self.send_command(bytecodes.b_inverted, 1)
        print('enabled white on black')

    def ds_invert(self):
        self.send_command(bytecodes.b_inverted, 0)
        print('enabled black on white')

    def __mm_to_points__(self, mm):
        points = int(mm / 0.125)
        print(f'{mm} mm = {points}')
        if points > 255:
            return self.__to_two_bytes__(points)

        return points

    @staticmethod
    def __to_two_bytes__(wrong_bytes):
        if wrong_bytes > 255:
            h_byte = int(wrong_bytes / 255)
            l_byte = wrong_bytes - h_byte * 255
            return l_byte, h_byte
        return wrong_bytes, 0
