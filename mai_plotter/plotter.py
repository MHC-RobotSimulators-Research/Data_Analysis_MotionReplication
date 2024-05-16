import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class plotter:
    def __init__ (self, offset, dfs):
        # plotter for 2 csv
        self.dfs = dfs

        # handle offset
        q = False
        # create offset_list
        offset_list = []*14
        if offset == True:
            while not q:
                offset_j = int(input("Enter the joint that you want to add offset or hit q if you want to stop: "))
                if offset_j != "q":
                    offset_index = offset_j - 1
                    offset_val = input("Enter the offset value of that joint: ")
                    offset_list[offset_index] = offset_val
                else: 
                    q = True

            self.regenerate_csv_offset()

    def regenerate_csv_offset(self, offset_list):
        for df in self.dfs: 
            for i in range(len(offset_list)):
                joint_name = "jpos" + str(i)
                new_column = df[joint_name].values - offset_list[i]
                df[joint_name] = new_column
        return
    
    def plot_one_jpos(self, df, id, filename, type):
        # line chart for one jpos
        joint_name = type + str(id-1)
        self.dfs[df-1].plot('time', joint_name)
        plt.xlabel(joint_name)
        self.save_figure(filename=filename)

    def plot_all_jpos(self, df_index, filename):
        # line chart for all jpos
        df_jpos = self.dfs[df_index - 1].iloc[:, 2:18]  # Select columns 2 to 17
        df_jpos.plot()
        self.save_figure(filename=filename)

    def save_figure (self, filename):
        figure_format = ["png", "svg", "eps"]
        for form in figure_format:
            plt.savefig(filename + "." + form, format = form)