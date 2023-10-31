import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from readFiles import *

class Histogram:

    #Doesn't take column name as input
    def lineGraph2(file_names):
        dfs = readFiles2(file_names)
        df1 = dfs[0]
        df2 = dfs[1]

        print(len(df1.columns))
        num=0
        for i in range(1,len(df1.columns)):
            if df1.columns[i] == 'index':
                continue

            sub_df1 = pd.DataFrame()
            sub_df2 = pd.DataFrame()
            sub_diff = pd.DataFrame()

            column_name = df1.columns[i]
            df1_column = df1.iloc[:,i]
            sub_df1['df1'] = df1_column
            sub_df1['type'] = 'df1'
            sub_df1['index'] = df1['index']

            df2_column = df2[column_name]
            sub_df2['df2'] = df2[column_name]
            sub_df2['type'] = 'df2'
            sub_df2['index'] = df2['index']

            diff = df1_column - df2_column
            sub_diff['diff'] = diff
            sub_diff['type'] = 'diff'
            sub_diff['index'] = df1['index']

            result = pd.concat([sub_df1, sub_df2, sub_diff], ignore_index=True, sort=False)

            plt.ylabel(column_name)
            # sns.displot(data=result, x='time', hue="type", element="step")
            num=num+1
        print(num)


    #Take column name as input
    def lineGraph3(file_names, column_lists):
        dfs = readFiles2(file_names)
        df1 = dfs[0]
        df2 = dfs[1]

        num=0
        for i in range(len(column_lists)):

            sub_df1 = pd.DataFrame()
            sub_df2 = pd.DataFrame()
            sub_diff = pd.DataFrame()

            column_name = column_lists[i]

            df1_column = df1[column_name]
            sub_df1['df1'] = df1_column
            sub_df1['type'] = 'df1'
            sub_df1['index'] = df1['index']

            df2_column = df2[column_name]
            sub_df2['df2'] = df2_column
            sub_df2['type'] = 'df2'
            sub_df2['index'] = df2['index']

            diff = df1_column - df2_column
            sub_diff['diff'] = diff
            sub_diff['type'] = 'diff'
            sub_diff['index'] = df1['index']

            result = pd.concat([sub_df1, sub_df2, sub_diff], ignore_index=True, sort=False)

            plt.ylabel(column_name)
            # sns.displot(data=result, x='time', hue="type", element="step")
            num=num+1
        print(num)
