import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from readFiles import *
from define import *

class LinePlot:
    #concatenate multiple dataframes and ignore the fact that they may have overlapping indexes
    def joinDataFrames(self, dataframes):
        df = dataframes[0]
        for i in range(1, len(dataframes)):
            df = pd.concat([df, dataframes[i]], ignore_index=True, sort=False)

        print("\n After concatenate:")
        print(df)
        print("\n")


    def lineGraph1(self, file_names, column_lists):
        print(file_names)
        print(column_lists)

        result = readFiles1(file_names, column_lists)
        self.joinDataFrames(result)

        df1 = result[0]
        df2 = result[1]

            # df = result[i]
            # plt.plot(df.iloc[:,0], df.iloc[:,1])
            # plot = sns.kdeplot(data=df, x='time', y=column_list[1], ax=ax, label=file_name)
            # plt.set(xlabel='Time', ylabel='Position', title='DataFrame Plot')
            # plt.show()

        fig, ax = plt.subplots(figsize=(10, 3))
        sns.lineplot(x='time', y=df1.columns[1], data=df1)
        plt.title(df1.columns[1].split(" ")[0])
        plt.xlabel('Time')
        plt.ylabel('Position')
        # plt.show()

        fig, ax = plt.subplots(figsize=(10, 3))
        sns.lineplot(x='time', y=df2.columns[1], data=df2)
        plt.title(df2.columns[1].split(" ")[0])
        plt.xlabel('Time')
        plt.ylabel('Position')
        # plt.show()

        # fig, ax = plt.subplots(figsize=(10, 3))
        a=sns.lineplot(x='time', y=df1.columns[1], data=df1, label=df1.columns[1])
        b=sns.lineplot(x='time', y=df2.columns[1], data=df2, label=df2.columns[1])
        # plt.show()

        plt.figure(figsize=(10,3))
        # plt.xlim(left=0, right=None)
        # plt.ylim(bottom=0, top=2)
        line = b.get_lines()
        print(line[0].get_ydata())
        print(line[1].get_ydata())
        plt.plot(line[0].get_xdata(),line[0].get_ydata(), color='red', label='trial_1')
        plt.plot(line[0].get_xdata(),line[1].get_ydata(), color='green', label='trial_2')

        plt.fill_between(line[0].get_xdata(), line[0].get_ydata(), line[1].get_ydata(), color='red', where=(line[0].get_ydata()>=line[1].get_ydata()), alpha=.5, label="Positive", interpolate=True)
        plt.fill_between(line[0].get_xdata(), line[0].get_ydata(), line[1].get_ydata(), color='green', where=(line[0].get_ydata()<line[1].get_ydata()), alpha=.5, label="Negative", interpolate=True)
        plt.legend()
        # plt.show()
        
        plt.savefig('{}/lineplot.eps'.format(SAVE_FIG_PATH))
        plt.savefig('{}/lineplot.png'.format(SAVE_FIG_PATH))