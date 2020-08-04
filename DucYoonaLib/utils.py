def safe_division(x, y):
    return x/y if y != 0 else 0

def standardize_string(my_str):
    for char in INVALID_CHARACTERS:
        if char in my_str:
            my_str = my_str.replace(char, '---')
    my_str = my_str.strip().upper()
    return my_str

def export_excel(df, filepath, sheet_name='DATA'):
	import pandas as pd
	writer = pd.ExcelWriter(filepath, date_format='YYYY-MM-DD', datetime_format='YYYY-MM-DD')
	df.to_excel(writer, sheet_name= sheet_name, index = False)