from define import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from meanBarGraph import meanBarGraph

class barplot:
    def __init__(self, title):
        all_csv = self.create_all_csv(title)
        self.all_mode_csv = all_csv[0]
        self.r = all_csv[1]
        self.title = title
        
    def create_path(self, mode):
        csv_path = []
        for i in range(1,4):
            csv_path.append(CSV_PATH + mode + "_p" + str(i) + ".csv")
        for i in range(1,4):
            csv_path.append(CSV_PATH + mode + "_a" + str(i) + ".csv")

        return csv_path
    
    def create_all_csv(self, object):

        all_mode_csv = []
        r = []
        if object == OBJECT[0]:
            r = [0,1,2]
        elif object == OBJECT[1]:
            r = [3,4,5]
        elif object == OBJECT[2]:
            r = [0,1,3]
        csv_path = []
        for m in MODE: 
            csv_path.append(self.create_path(mode = m))
        print(csv_path)

        for csv in csv_path:
            for path in csv:
                all_mode_csv.append(pd.read_csv(path)) 

        return all_mode_csv,r
    
    def add_offset(self, dfs):
        # create offset list 
        offset_choice = input("Do you want to add offset to the csv? (y/n)\n")
        
        if offset_choice == "y":
            offset_list = [0] * len(BOTH_J)
            offset_j = list(map(int, input(f"Which joint(s) do you want to add offset? ({', '.join(map(str, BOTH_J))})\n").split()))
            offset_v = list(map(float, input("What values of offset correspond to those joints? \n").split()))

            for _ in range(len(offset_j)):
                i = BOTH_J.index(offset_j[_])
                offset_list[i] = offset_v[_]

            # Applying the offset to the dataframe columns (just apply the offsets to the first 3)
            phys = [0,1,2]
            for i in range(len(dfs)):
                if i % 6 in phys:
                    for joint_index in range(len(BOTH_J)):
                        joint_name = f"jpos{BOTH_J[joint_index]}"
                        curr = dfs[i][joint_name]
                        dfs[i].loc[:, joint_name] = curr + offset_list[joint_index]

        elif offset_choice == "n":
            pass

        return dfs
    
    def filter_jpos(self, df):
        jpos_name = []
        jvel_name = []
        for joint in BOTH_J:
            jpos_name.append("jpos" + str(joint))
            jvel_name.append("jvel" + str(joint))

        # Filter and update the dataframes
        new_df = df[jpos_name + jvel_name]
        return new_df
    


    def data_prep_bar_plot(self, dfs_new, type):
        # all_mode_csv = 2d array with 
        # 3 rows: 3 modes
        # 6 columns: 3 phys, 3 ambf
        final_dfs = []
        # dfs is 1d array with 9 elements
        # 3 phys csv in two arm mode, 3 phys csv in left arm, 3 phys csv in right arm
        for i in range(len(dfs_new)):
            # for mode two arm
            if i % 6 in self.r:
                final_dfs.append(dfs_new[i])            

        # initialize plotter for 3 phys csv in two arm mode
        two_arm = meanBarGraph(final_dfs[0], final_dfs[1], final_dfs[2])
        print("2arm: ", final_dfs[0]['jpos4'])
        left_arm = meanBarGraph(final_dfs[3], final_dfs[4], final_dfs[5])
        print("leftarm: ", final_dfs[3]['jpos4'])
        right_arm = meanBarGraph(final_dfs[6], final_dfs[7], final_dfs[8])
        print("rightarm: ", final_dfs[6]['jpos4'])

        plotters = [two_arm, left_arm, right_arm]
        mean_list = []
        for p in range((len(MODE))):
            plotters[p].plot_mean_bar_graph(type, GRAPH_PATH + "mean_bar_graph" + MODE[p])
            mean = plotters[p].get_mean_error()
            # print(mean)
            mean_list.append(mean)

        return mean_list

    def draw_bar_plot(self):
        bar1_value = []
        bar2_value = []
        type = ["jpos", "jvel"]
        categories = MODE

        # filter all csv with chosen joints 
        filtered_dfs = []
        for df in self.all_mode_csv:
            filtered_dfs.append(self.filter_jpos(df))

        # add offsets
        final_dfs = self.add_offset(filtered_dfs)

        bar1_value = self.data_prep_bar_plot(final_dfs, type[0])
        print("jpos mean diff: ", bar1_value)
        bar2_value = self.data_prep_bar_plot(final_dfs, type[1])

        # Creating the positions for the bars on the x-axis
        x = np.arange(len(categories))

        # Width of each bar
        bar_width = 0.35

        # Clear the graph before plotting
        plt.clf()

        # Creating the bar plot
        plt.bar(x - bar_width/2, bar1_value, width=bar_width, label='JPos (rad)')
        plt.bar(x + bar_width/2, bar2_value, width=bar_width, label='JVel (rad/s)')

        # Adding labels, title, and legend
        plt.xlabel('Modes')
        plt.ylabel('Mean Error')
        plt.title(self.title)
        plt.xticks(x, categories)
        plt.legend()

        # Add counts above each column
        for i, val in enumerate(bar1_value):
            plt.text(i - bar_width/2, val + 0.0003, str(round(val, 2)), ha='center', va='bottom')

        for i, val in enumerate(bar2_value):
            plt.text(i + bar_width/2, val + 0.0003, str(round(val, 2)), ha='center', va='bottom')

        # Show plot
        figure_format = ["png", "svg", "eps"]
        for form in figure_format:
            plt.savefig(GRAPH_PATH + self.title + "." + form, format = form)
        return