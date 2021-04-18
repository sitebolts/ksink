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


def remove_numbered_words(original_words):
    if (type(original_words) == list):
        cleaned_words = [word for word in original_words if bool(regex.search(r'\d', word)) == False]
        return cleaned_words

    elif (type(original_words) == str):
        cleaned_words = ' '.join([word for word in original_words.split(' ') if bool(regex.search(r'\d', word)) == False])
        return cleaned_words

    else:
        raise Exception('Unknown variable type: Expected original_words to be a str or list, but it was {}'.format(str(type(original_words))))


def contains_numbered_words(words):    
    if (type(words) == list):
        for word in words:
            if (bool(regex.search(r'\d', word)) == True):
                return True
        return False

    elif (type(words) == str):
        for word in words.replace('\r\n', ' ').replace('\n', ' ').split(' '):
            if (bool(regex.search(r'\d', word)) == True):
                return True
        return False

    else:
        raise Exception('Unknown variable type: Expected original_words to be a str or list, but it was {}'.format(str(type(original_words))))


#Trims a string until it's no longer than X bytes in UTF8
#Surely there's a better way to do this?
def trim_string_to_x_bytes(string, max_bytes, character_encoding):
    string = string[:max_bytes]

    while (len(string.encode(character_encoding)) > max_bytes):
        string = string[:-1]

    return string
