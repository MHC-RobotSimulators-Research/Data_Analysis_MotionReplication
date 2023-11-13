import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class plotter:
    def __init__ (self, df1, df2=None):
        # plotter for 2 csv
        self.df1 = df1
        self.df2 = df2

    def regenerate_csv_offset(self, offset_list):
        for i in range(len(offset_list)):
            joint_name = "jpos" + str(i)
            print(joint_name)
            new_column = self.df2[joint_name].values - offset_list[i]
            self.df2[joint_name] = new_column
        return
    
    def plot_one_jpos(self, id, filename):
        # line chart for one jpos
        joint_name = "jpos" + str(id)
        self.df1.plot('time', joint_name)
        plt.xlabel(joint_name)
        plt.savefig(filename)

    def plot_all_jpos(self, filename):
        # line chart for all jpos
        df_jpos = self.df1[self.df1.columns[2:18]] 
        df_jpos.plot()
        plt.savefig(filename)

    def unify_shape(self):
        num_row1 = self.df1.shape[0] 
        num_row2 = self.df2.shape[0] 
        if num_row1<= num_row2:
            self.df2 = self.df2.iloc[:num_row1,:]
        else:
            self.df1 = self.df1.iloc[:num_row2,:]
    
    # overlay by time
    def overlay_one_jpos(self, id1, id2, filename):
        joint_name_1 = "jpos" + str(id1)
        joint_name_2 = "jpos" + str(id2)

        # Round 'time' column to 0.01
        self.df1['time'] = self.df1['time'].round(2)
        self.df2['time'] = self.df2['time'].round(2)

        # Merging
        merged_df = pd.merge(self.df1, self.df2, on='time', how='inner', suffixes=('_df1', '_df2'))

        if merged_df.empty:
            print("Merged dataframe is empty. Check your data or column names.")
            return

        # Plot first overlay 
        df1_joint = merged_df[joint_name_1 + '_df1']
        df2_joint = merged_df[joint_name_1 + '_df2']

        # Before plotting, clear the plot
        plt.clf()

        # Plotting the lines with different colors
        plt.plot(merged_df['time'], df1_joint, label="Phys2 - " + "joint " + str(id1+1), color='orange')
        plt.plot(merged_df['time'], df2_joint, label="Phys3 - "+ "joint " + str(id1+1) , color='green')


        # Fill the space between the lines with red color
        plt.fill_between(merged_df['time'], df1_joint, df2_joint, color='red', alpha=0.3, label="Best")

        # Plot the second overlay 
        df1_joint_2 = merged_df[joint_name_2 + '_df1']
        df2_joint_2 = merged_df[joint_name_2 + '_df2']

        # Plotting the lines
        plt.plot(merged_df['time'], df1_joint_2, label="Phys2 - " + "joint " + str(id2+1), color='orange', linestyle='dashed')
        plt.plot(merged_df['time'], df2_joint_2, label="Phys3 - "+ "joint " + str(id2+1), color='green', linestyle='dashed')

        # Fill the space between the lines with red color
        plt.fill_between(merged_df['time'], df1_joint_2, df2_joint_2, color='blue', alpha=0.3, label="Worst")

        # Adding title and labels
        plt.title("Overlay of joint position " + str(id1+1) + " and " + str(id2+1))
        plt.xlabel("Time (ms)")
        plt.ylabel("Joint Position (degrees)")

        # Move legend to the top right and outside of the graph
        plt.legend(loc='upper right', bbox_to_anchor=(1.15, 1))

        figure_format = ["png", "svg", "eps"]
        for form in figure_format:
            plt.savefig(filename + "." + form, format=form)

    # this is overlay by index
    # def overlay_one_jpos(self, id, filename):
    #     plt.clf()
    #     # make 2 dataframe the same size
    #     # self.unify_shape()
    #     # overlay one jpos from 2 different recording times
    #     joint_name = "jpos" + str(id)
    #     df1_joint = self.df1[joint_name].values
    #     df2_joint = self.df2[joint_name].values
    #     #id_arr = self.df1.index.values
    #     overlay_df = pd.DataFrame(
    #         {
    #         "df1": df1_joint,
    #         "df2": df2_joint }
    #     )
    #     # Plotting the lines
    #     plt.plot(overlay_df["df1"], label="df1")
    #     plt.plot(overlay_df["df2"], label="df2")
    #     # Fill the space between the lines with red color
    #     plt.fill_between(overlay_df.index, overlay_df["df1"], overlay_df["df2"], color='red', alpha=0.3)

    #     #overlay_df.plot()
    #     plt.title("Overlay " + joint_name)
    #     plt.xlabel("Time")
    #     plt.ylabel("Degree")
    #     figure_format = ["png", "svg", "eps"]
    #     for form in figure_format:
    #         plt.savefig(filename + "." + form, format = form)

    def lineGraph2(self, filenames):
        # Initialize y-axis limits to capture the range of all lines
        min_y, max_y = float('inf'), float('-inf')
        diff_list = []
        jpos_list = []

        # Iterate through each joint position
        for i in range(16):
            jpos = "jpos" + str(i)
            plt.clf()
            df1_column = self.df1[jpos]
            df2_column = self.df2[jpos]
            diff = df1_column - df2_column

            # Update y-axis limits based on the current line
            min_y = min(min_y, diff.min())
            max_y = max(max_y, diff.max())

            # Plot the line with a label
            diff.plot(label=jpos, color="orange")

            # Save the individual plots
            plt.savefig(filenames[i])

            diff_list.append(diff)
            jpos_list.append(jpos)

        # Create a combined plot for all joint positions
        plt.clf()
        for diff, jpos in zip(diff_list, jpos_list):
            diff.plot(label=jpos)

        # Set the same y-axis range for all lines
        plt.ylim(min_y, max_y)

        # Add a baseline at 0
        plt.axhline(0, color='gray', linestyle='--', linewidth=1)

        # Add legend
        plt.legend()

        # Save or show the plot
        plt.savefig(filenames[16])

    def mean_bar_graph(self, filename):

        #create mean, jpos column and bar_color for positive mean = green, negative mean = orange
        mean_column = []
        jpos_column = []
        bar_color = []
        for i in range(16):
            jpos = "jpos" + str(i)
            # plt.clf()
            # count mean
            df1_column = self.df1[jpos]
            df2_column = self.df2[jpos]
            diff = df1_column - df2_column
            mean = diff.mean()
            if mean < 0:
                bar_color.append("orange")
            else:
                bar_color.append("g")
            mean_column.append(mean)
            jpos_column.append(jpos)

        print(mean_column)
        #create pandas dataframe with above columns
        mean_bar = pd.DataFrame({"Mean Differences": mean_column, "Joint Position": jpos_column})
        # create bar plots        
        graph = mean_bar.plot(kind = "bar", x = "Joint Position", y = "Mean Differences", legend=False, color=bar_color)
        # Add a baseline at 0
        graph.axhline(0, color='gray', linestyle='--', linewidth=1)
        # Add labels and title
        plt.xlabel("Mean Differences")
        plt.ylabel("Joint Position")
        plt.title("Mean Differences of Joint Positions")

        #beside generating graph, also count the mean number of all means to represent the overal performance
        mean_error = sum(abs(mean) for mean in mean_column)/14
        #add overal mean in the right corner
        graph.text(0.95, 0.95, f"Mean Error: {mean_error:.2f}", transform=graph.transAxes, fontsize=12,
            verticalalignment='top', horizontalalignment='right', bbox=dict(boxstyle='round,pad=0.5', edgecolor='gray', facecolor='white'))
        figure_format = ["png", "svg", "eps"]
        for form in figure_format:
            plt.savefig(filename + "." + form, format = form)
        return