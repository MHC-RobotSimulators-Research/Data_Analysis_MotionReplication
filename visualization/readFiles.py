import pandas as pd
import matplotlib.pyplot as plt
import os
from define import *

#only used for method 1 (line plot)
def readFiles1(file_names, column_lists):
    result = list()
    print(file_names)
    print(column_lists)

    n = len(file_names) 
    file_names = file_names[1:n-1] 
    file_names = file_names.split(',')

    n = len(column_lists) 
    column_lists = column_lists[1:n-1] 
    column_lists = column_lists.split(',') 

    for index, file in enumerate(file_names):
        print(file)

        #read file and extract specific columns
        file_name = file_names[index]
        # column_list = column_lists[index]
        csv_file_path = os.path.join(CSV_FILES_PATH, file_name)
        
        # df = pd.read_csv(csv_file_path, usecols=column_lists)
        df = pd.read_csv(csv_file_path)
        df['time'] = df['time'].div(10**9)

        # df=df.iloc[:20]
        # df = df.sort_values('index')
        # print(df)

        result.append(df)

        # df_view = df.copy(deep=True)
        # for i in range(1, len(column_lists)):
        #     # if df_view.columns[i] == 'index':
        #     #     continue
        #     df_view.rename(columns={ df.columns[i]: file_name.split('.')[0]+' '+df_view.columns[i]}, inplace=True)
        # print(df_view)
        # result.append(df_view)

    return result


def readFiles2(file_names):
    result = list()

    n = len(file_names) 
    file_names = file_names[1:n-1] 
    file_names = file_names.split(',')
    print(file_names[0])

    for index, file in enumerate(file_names):
        print(file)

        #read file and extract specific columns
        file_name = file_names[index]
        csv_file_path = os.path.join(CSV_FILES_PATH, file_name)

        #read file
        df = pd.read_csv(csv_file_path)

        # df['index'] = df['index'].div(10**9)

        result.append(df)
    return result