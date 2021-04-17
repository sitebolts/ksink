import os
#import pytest
import sys
sys.path.append('../src/')

print('Python version: {}'.format(sys.version))
print('Current directory: {}'.format(os.getcwd()))
print('List of files in the current directory: {}'.format(', '.join(os.listdir())))

from ksink.csv import create_csv_cell
create_csv_cell('Import test 1')
from ksink import csv
csv.create_csv_cell('Import test 2')
import ksink
ksink.csv.create_csv_cell('Import test 3')
print('Import tests passed!')


def test_csv_cell_generation():
  assert ksink.csv.create_csv_cell('A normal day') == '"A normal day"'
  assert ksink.csv.create_csv_cell('A "normal" day') == '"A ""normal"" day"'

def test_csv_row_generation():
  assert ksink.csv.create_csv_row(['Item name'], False) == '"Item name"'
  assert ksink.csv.create_csv_row(['Item name'], True) == '"Item name"\n'
  assert ksink.csv.create_csv_row(['Item name', 'Sales'], False) == '"Item name","Sales"'
  assert ksink.csv.create_csv_row(['Item name', 'Sales'], True) == '"Item name","Sales"\n'

  
#assert ksink.string.escape_string_for_xpath('It is normal') == '"It is normal"'
#assert ksink.string.escape_string_for_xpath('It is "normal"') == '\'It is "normal"\''
#assert ksink.string.escape_string_for_xpath("It isn't normal") == '"It isn\'t normal"'
#assert ksink.string.escape_string_for_xpath('It isn\'t "normal"') == 'concat("It isn\'t ", \'"\',"normal", \'"\',"")'

#print('Function tests passed!')

print('End of testing file.')







#from ksink import csv
#from ksink.csv import create_csv_cell
#from ksink.string import escape_string_for_xpath
#from ksink.file import save_file
#from ksink.file import get_element_value
