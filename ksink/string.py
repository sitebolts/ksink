import regex
import ctypes
from PIL import ImageFont

#https://stackoverflow.com/a/47461052/1741346
def escape_string_for_xpath(s):
    if '"' in s and "'" in s:
        return 'concat(%s)' % ", '\"',".join('"%s"' % x for x in s.split('"'))
    if '"' in s:
        return "'%s'" % s
    return '"%s"' % s
	

def find_whole_word(needle, haystack, ignore_case):
    if (ignore_case == True):
        return bool(regex.search(regex.compile(r'\b({0})\b'.format(needle), flags=regex.IGNORECASE), haystack))
    else:
        return bool(regex.search(regex.compile(r'\b({0})\b'.format(needle)), haystack))


def remove_numbers_from_string(string):
    return ''.join([i for i in string if not i.isdigit()])
	
	
#Example: get_pil_text_size('Hello world', 12, 'times.ttf')
def get_pil_text_size(text, font_size, font_name):
    font = ImageFont.truetype(font_name, font_size)
    size = font.getsize(text)
    return size


#Example: get_windows_text_size('Hello world', 12, 'Times New Roman')
def get_windows_text_size(text, font_size, font_name):
    class SIZE(ctypes.Structure):
        _fields_ = [("cx", ctypes.c_long), ("cy", ctypes.c_long)]

    hdc = ctypes.windll.user32.GetDC(0)
    hfont = ctypes.windll.gdi32.CreateFontA(font_size, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, font_name)
    hfont_old = ctypes.windll.gdi32.SelectObject(hdc, hfont)

    size = SIZE(0, 0)
    ctypes.windll.gdi32.GetTextExtentPoint32A(hdc, text, len(text), ctypes.byref(size))

    ctypes.windll.gdi32.SelectObject(hdc, hfont_old)
    ctypes.windll.gdi32.DeleteObject(hfont)

    return (size.cx, size.cy)
