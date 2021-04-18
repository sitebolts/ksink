def create_csv_cell(string):
    if (string == None):
        return '""'

    string = str(string)
    
    return ('"' + string.replace('"', '""') + '"')


#Converts an array of strings into a valid CSV row
def create_csv_row(cell_strings, include_newline):
    if (isinstance(cell_strings, list) == False):
        raise Exception("The first value passed to create_csv_row must be a list.")

    if (isinstance(include_newline, bool) == False):
        raise Exception("The second value passed to create_csv_row must be a bool.")
    
    row_string = ",".join([create_csv_cell(cell_string) for cell_string in cell_strings])

    if (include_newline == True):
        row_string += '\n'
    
    return row_string


#Auto-detect whether a CSV file is UTF-8 or UTF-16 and return the opened file
#TODO: Make this more generic and support more character encodings
def open_utf8_or_utf16_csv_file(filename, newline):
    try:
        csv_file = open(filename, newline=newline, encoding='utf-8')
        csv_reader = csv.reader(csv_file, delimiter='\t', quotechar='"')
        for exhaust in enumerate(csv_reader):
            break #Only one iteration is needed
        csv_file.seek(0)
        return csv_file
    except UnicodeError:
        pass

    try:
        csv_file = open(filename, newline=newline, encoding='utf-16')
        csv_reader = csv.reader(csv_file, delimiter='\t', quotechar='"')
        for exhaust in enumerate(csv_reader):
            break #Only one iteration is needed
        csv_file.seek(0)
        return csv_file
    except UnicodeDecodeError:
        pass

    raise Exception("Could not read CSV file: Unsupported character encoding")
