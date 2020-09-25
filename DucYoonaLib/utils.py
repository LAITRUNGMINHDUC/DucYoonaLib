import pandas as pd

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
    writer.close()

def convert_datafile_to_XLSX(folder_inputpath, folder_outputpath):
    import os
    import pathlib

    folder_inputpath = str(pathlib.Path(folder_inputpath).absolute())
    folder_outputpath = str(pathlib.Path(folder_outputpath).absolute())

    for fileitem in os.listdir(folder_inputpath):
        print (fileitem)

        # SET PATH
        input_filepath = os.path.join(folder_inputpath, fileitem)
        output_filepath = os.path.join(folder_outputpath, fileitem + '.xlsx')

        # START EXCEL DESKTOP
        excel = win32com.client.Dispatch('Excel.Application')
        excel.Visible = True
        excel.DisplayAlerts = False
        workbook = excel.Workbooks.Open(input_filepath)
        workbook.SaveAs(output_fileitem ,FileFormat=51) #FileFormat = 51 means: export XLSX
        workbook.Close()
        excel.Quit()

        # NOTE: This function will create new instance of Excel every-time 
        # --> Should be Optimize by creating CLASS object, then init Excel instance once, then pass it into parameter.
