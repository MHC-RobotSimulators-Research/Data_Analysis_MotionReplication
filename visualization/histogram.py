import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from readFiles import *

class Histogram:

    #Doesn't take column name as input
    def lineGraph2(self, file_names):
        dfs = readFiles2(file_names)
        df1 = dfs[0]
        df2 = dfs[1]

        num=0
        for i in range(0,len(df1.columns)):
            if df1.columns[i] == 'time':
                continue

            sub_df1 = pd.DataFrame()
            sub_df2 = pd.DataFrame()
            sub_diff = pd.DataFrame()

            column_name = df1.columns[i]
            df1_column = df1.iloc[:,i]
            sub_df1['df1'] = df1_column
            sub_df1['type'] = 'df1'
            sub_df1['time'] = df1['time']

            df2_column = df2[column_name]
            sub_df2['df2'] = df2[column_name]
            sub_df2['type'] = 'df2'
            sub_df2['time'] = df2['time']

            diff = df1_column - df2_column
            sub_diff['diff'] = diff
            sub_diff['type'] = 'diff'
            sub_diff['time'] = df1['time']

            result = pd.concat([sub_df1, sub_df2, sub_diff], ignore_index=True, sort=False)

            # plt.ylabel(column_name)
            sns.displot(data=result, x='time', hue="type", element="step")
            fig = plt.figure()
            fig.set_tight_layout(True)
            
            save_name_png = 'histogram_' + column_name + '.png'
            save_path_png = os.path.join(SAVE_FIG_PATH, save_name_png)
            plt.savefig(save_path_png)
            save_name_eps = 'histogram_' + column_name + '.eps'
            save_path_eps = os.path.join(SAVE_FIG_PATH, save_name_eps)
            plt.savefig(save_path_eps)

            num=num+1
        

    #Take column name as input
    def lineGraph3(self, file_names, column_lists):
        n = len(column_lists) 
        column_lists = column_lists[1:n-1] 
        column_lists = column_lists.split(',')
        
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
            sub_df1['time'] = df1['time']

            df2_column = df2[column_name]
            sub_df2['df2'] = df2_column
            sub_df2['type'] = 'df2'
            sub_df2['time'] = df2['time']

            diff = df1_column - df2_column
            sub_diff['diff'] = diff
            sub_diff['type'] = 'diff'
            sub_diff['time'] = df1['time']

            result = pd.concat([sub_df1, sub_df2, sub_diff], ignore_index=True, sort=False)
            
            plt.ylabel(column_name)
            sns.displot(data=result, x='time', hue="type", element="step")

            fig = plt.figure()
            fig.set_tight_layout(False)
            plt.tight_layout()

            save_name_png = 'histogram_' + column_name + '.png'
            save_path_png = os.path.join(SAVE_FIG_PATH, save_name_png)
            plt.savefig(save_path_png)
            save_name_eps = 'histogram_' + column_name + '.eps'
            save_path_eps = os.path.join(SAVE_FIG_PATH, save_name_eps)
            plt.savefig(save_path_eps)

            num=num+1
