import pandas as pd 
import os 
import multiprocessing as mp 

def multiprocessing_function_dataframe(func, arr_args):
    pool = mp.Pool()
    df_result = pool.map(func, arr_args)
    df_result = pd.concat(df_result)    
    pool.close()
    pool.join()
    return df_result

def multiprocessing_function_general(func, arr_args):
    pool = mp.Pool()
    pool.map(func, arr_args)    
    pool.close()
    pool.join()

def singlecore_processing_function_dataframe(func, arr_args):
    df_result = pd.DataFrame()
    for args in arr_args:
        df_result = df_result.append(func(args))
    return df_result
    
def singlecore_processing_function_general(func, arr_args):
    for args in arr_args:
        func(args)


def read_xlsx_file(arg):
    filename, sheet_name, folderpath = arg
    print (filename)
    if (sheet_name != ''):
        df = pd.read_excel(folderpath + filename, sheet_name= sheet_name)
    else:
        df = pd.read_excel(folderpath + filename)
    return df 

def multiprocessing_read_xlsx_files(folderpath, sheet_name):
    arr_args = list()
    list_files = os.listdir(folderpath)
    for file_item in list_files:
        if ('xlsx' in file_item):
            arg = (file_item, sheet_name, folderpath)
            arr_args.append(arg)

    df = multiprocessing_function_dataframe(func = read_xlsx_file, arr_args= arr_args)
    return df

def read_datafile(arg):
    folderpath, filepath, filetype, sheet_name = arg
    print (filepath)

    if filetype == 'CSV' and 'csv' in filepath.lower():
        df = pd.read_csv(folderpath + filepath, engine='python', encoding='utf-8')
    if filetype == 'XLSX' and 'xlsx' in filepath.lower():
        if (sheet_name != ''):
            df = pd.read_excel(folderpath + filename, sheet_name= sheet_name)
        else:
            df = pd.read_excel(folderpath + filename)
    return df

def multiprocessing_read_datafiles(folderpath, sheet_name='', filetype='XLSX'):
    list_files = os.listdir(folderpath)
    arr_args = [(folderpath, filepath, filetype, sheet_name) for filepath in list_files]
    df = multiprocessing_function_dataframe(func = read_datafile, arr_args= arr_args)
    return df