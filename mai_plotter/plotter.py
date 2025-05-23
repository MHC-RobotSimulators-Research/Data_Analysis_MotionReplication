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
    
    def filter_jpos(self, used_j): # will move it out to the main menu
        filtered_dfs = []
        jpos_name = []
        jvel_name = []
        for joint in used_j:
            jpos_name.append("jpos" + str(joint))
            jvel_name.append("jvel" + str( joint))

        # Filter and update the dataframes: only include jpos and jvel 
        # of selected joints
        for df in self.dfs:
            new_df = df[jpos_name + jvel_name]
            filtered_dfs.append(new_df)

        self.dfs = filtered_dfs
        return 
    
    def plot_one_jpos(self, df, id, filename, type):
        plt.clf()
        # line chart for one jpos
        joint_name = type + str(id-1)
        df = self.dfs[df-1]

        # color for interaction 
        if 'interact' in df.columns:
            # Iterate through the DataFrame and plot segments with the appropriate colors
            for i in range(1, len(df)):
                color = 'r' if df['interact'].iloc[i] == 1 else 'b'
                # Print values to debug
                #print(f"Index: {i}, Interaction: {df['interaction'].iloc[i]}, Color: {color}")
                plt.plot(df['time'].iloc[i-1:i+1], df[joint_name].iloc[i-1:i+1], color=color)
        else:
            # Plot the entire series with a single color (e.g., blue) if 'interaction' column does not exist
            plt.plot(df['time'], df[joint_name], color='blue')

        plt.xlabel(joint_name)
        plt.ylabel(joint_name)
        self.save_figure(filename=filename)

    def plot_all_jpos(self, df_index, filename, used_j, type):
        # line chart for all jpos
        joint_name = []
        for i in used_j:
            joint_name.append(type + str(i))
        df = self.dfs[df_index - 1]
        df_j = df[joint_name]
        df_j.plot()
        self.save_figure(filename=filename)

    def save_figure (self, filename):
        figure_format = ["png", "svg"]
        for form in figure_format:
            plt.savefig(filename + "." + form, format = form)
        plt.switch_backend('ps')
        plt.savefig(filename + ".eps", format='eps')

