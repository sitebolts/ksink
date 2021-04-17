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
