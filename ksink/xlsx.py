#Valid dict_type values: 'records', 'dict', 'list', 'series', 'split', 'index'
#Example: get_xlsx_dict_using_pandas('records.xlsx', 0, str, 'records')
def get_xlsx_dict_using_pandas(file_name, sheet, dtype, dict_type):
    data_frame = pandas.read_excel(file_name, sheet_name=sheet, dtype=dtype)
    data_frame = data_frame.replace(numpy.nan, '', regex=True) #Make empty cells use "" instead of nan
    return data_frame.to_dict(dict_type)
