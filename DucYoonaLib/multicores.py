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