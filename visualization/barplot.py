import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from readFiles import *
from define import *

class BarPlot:
    def lineGraph4(self, file_names, column_lists):
        n = len(column_lists) 
        column_lists = column_lists[1:n-1] 
        column_lists = column_lists.split(',') 

        dfs = readFiles2(file_names)
        df1 = dfs[0]
        df2 = dfs[1]

        # total_time_stamped = df1['time_stamped'].iloc[-1] - df1['time_stamped'].iloc[0]
        total_time_stamped = df1['time'].iloc[-1] - df1['time'].iloc[0]
        mean_list = []

        for i in range(len(column_lists)):

            column_name = column_lists[i]
            sub_df = pd.DataFrame()
            
            df1_column = df1[column_name]
            sub_df['df1'] = df1_column
            df2_column = df2[column_name]
            sub_df['df2'] = df2_column
            diff = df1_column - df2_column
            sub_df['diff'] = diff

            sum_diff = sub_df['diff'].sum()
            mean = sum_diff/total_time_stamped
            mean_list.append(mean)
        
        fig = plt.figure()
        ax = fig.add_axes([0,0,1,1])
        ax.bar(column_lists, mean_list)
        plt.axhline(y=0, color='black')

        plt.savefig('{}/barplot.eps'.format(SAVE_FIG_PATH))
        plt.savefig('{}/barplot.png'.format(SAVE_FIG_PATH))