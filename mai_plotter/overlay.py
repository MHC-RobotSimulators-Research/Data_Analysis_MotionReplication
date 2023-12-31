import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class overlay:
    def __init__(self, df1, df2=None, df3=None):
        self.df1 = df1
        self.df2 = df2
        self.df3 = df3
        self.df = [self.df1, self.df2, self.df3]
     # overlay by time
    def overlay_two_jpos(self, type, id1, id2, filename):
        # Round 'time' column to 0.01
        for df in self.df:
            df['time'] = df['time'].round(2)

        # Merge df1 and df2 first
        merged_df_first = pd.merge(self.df1, self.df2, on='time', suffixes=('_df1', '_df2'))

        # Then merge df3 with the previously merged DataFrame
        merged_df = pd.merge(merged_df_first, self.df3, on='time', suffixes=('', '_df3'), how='inner')


        if merged_df.empty:
            print("Merged dataframe is empty. Check your data or column names.")
            return
        # Before plotting, clear the plot
        plt.clf()

        # create labels for first and second joint 
        j1 = " Left Joint " + str(id1+1)
        j2 = " Left Joint " + str(id2+1)
        if id1+1 > 7:
            j1 = " Right Joint " + str(id1 + 1 -7)
        if id2+1 > 7:
            j2 = " Right Joint " + str(id2 + 1 -7)
        #Plot first, second overlay
        self.overlay_one_jpos_time(type, merged_df=merged_df, id=id1, color = "red", label="Most consistent -" + j1)
        self.overlay_one_jpos_time(type, merged_df=merged_df, id=id2, color = "blue", label="Least consistent -" + j2)

        # Adding title and labels
        plt.title(f"Overlay of {j1} and {j2}")
        plt.xlabel("Time (ms)")
        plt.ylabel("Joint Position (degrees)")

        # Move legend to the top right and outside of the graph
        plt.legend(loc='upper right', bbox_to_anchor=(1, 1))

        figure_format = ["png", "svg", "eps"]
        for form in figure_format:
            plt.savefig(filename + "." + form, format=form)

    # overlay by time, with joint position = id, filling color = color, label of the graph = label
    def overlay_one_jpos_time(self, type, merged_df, id, color, label):

        joint_name = type + str(id)
        # Calculate min, max, and mean
        total_in_3 = merged_df[[joint_name + '_df1', joint_name + '_df2', joint_name]]
        min_joint =  merged_df['min_joint'] = total_in_3.min(axis=1)
        max_joint = merged_df['max_joint'] = total_in_3.max(axis=1)
        mean_joint = merged_df['mean_joint'] = total_in_3.mean(axis=1)
        # Plotting the lines with different colors
        plt.plot(merged_df['time'], min_joint, color='orange')
        plt.plot(merged_df['time'], max_joint, color='green')
        plt.plot(merged_df['time'], mean_joint, color='yellow' )

        # Fill the space between the lines with red color
        plt.fill_between(merged_df['time'], min_joint, max_joint, color=color, alpha=0.3, label=label)

    # this is overlay by index
    def overlay_one_jpos_index(self, type, id, filename):
        plt.clf()
        
        # make 2 dataframe the same size
        # self.unify_shape()
        # overlay one jpos from 2 different recording times
        joint_name = type + str(id)
        df1_joint = self.df1[joint_name].values
        df2_joint = self.df2[joint_name].values
        #id_arr = self.df1.index.values
        overlay_df = pd.DataFrame(
            {
            "df1": df1_joint,
            "df2": df2_joint }
        )
        # Plotting the lines
        plt.plot(overlay_df["df1"], label="df1")
        plt.plot(overlay_df["df2"], label="df2")
        # Fill the space between the lines with red color
        plt.fill_between(overlay_df.index, overlay_df["df1"], overlay_df["df2"], color='red', alpha=0.3)

        #overlay_df.plot()
        plt.title("Overlay " + joint_name)
        plt.xlabel("Time")
        plt.ylabel("Degree")
        figure_format = ["png", "svg", "eps"]
        for form in figure_format:
            plt.savefig(filename + "." + form, format = form)
