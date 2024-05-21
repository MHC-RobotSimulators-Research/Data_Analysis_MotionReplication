from define import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from meanBarGraph import meanBarGraph

class barplot:
    def __init__(self, title, sliding):
        all_csv = self.create_all_csv(title)
        self.all_mode_csv = all_csv[0]
        self.r = all_csv[1]
        self.title = title
        self.sliding = False
        if sliding:
            self.used_j = SLIDING_J
        else:
            self.used_j = BOTH_J

        # self.save_offset_csv() # will move it out to the main menu

    def save_offset_csv(self):  # will move it out to the main menu        
        original_j = BOTH_J + SLIDING_J
        original_j.sort()
        self.used_j = original_j
        offset_dfs = self.add_offset(self.all_mode_csv)

        count = 0
        m = 0
        p = [0,1,2]
        for df in range(len(offset_dfs)):
            if count == 6:
                m += 1
                count = 0
            if df % DF_PER_MODE in p:
                phys_ambf = "_p"
            else:
                phys_ambf = "_a"
            order = df % NUM_CSV + 1
            offset_dfs[df].to_csv(OFFSET_PATH + MODE[m] + "_" + phys_ambf + str(order) + ".csv", index=False)
            count += 1

    def create_path(self, mode): # will move it out to the main menu
        csv_path = []
        for i in range(1,4):
            csv_path.append(OFFSET_PATH + mode + "__p" + str(i) + ".csv")
        for i in range(1,4):
            csv_path.append(OFFSET_PATH + mode + "__a" + str(i) + ".csv")

        return csv_path
    
    def create_all_csv(self, object): # will move it out to the main menu

        all_mode_csv = []
        r = []
        if object == OBJECT[0]:
            r = [0,1,2]
        elif object == OBJECT[1]:
            r = [3,4,5]
        elif object == OBJECT[2]:
            r = [2,3,4]
        csv_path = []
        for m in MODE: 
            csv_path.append(self.create_path(mode = m))

        for csv in csv_path:
            for path in csv:
                all_mode_csv.append(pd.read_csv(path)) 

        return all_mode_csv,r
    
    def add_offset(self, dfs): # will move it out to the main menu
        # create offset list 
        offset_choice = input("Do you want to add offset to the csv? (y/n)\n")
        
        if offset_choice == "y":
            offset_list = [0] * len(self.used_j)
            offset_j = list(map(int, input(f"Which joint(s) do you want to add offset? ({', '.join(map(str, self.used_j))})\n").split()))
            offset_v = list(map(float, input("What values of offset correspond to those joints? \n").split()))

            for _ in range(len(offset_j)):
                i = self.used_j.index(offset_j[_])
                offset_list[i] = offset_v[_]

            # Applying the offset to the dataframe columns (just apply the offsets to the first 3)
            phys = [0,1,2]
            for i in range(len(dfs)):
                if i % 6 in phys:
                    for joint_index in range(len(self.used_j)):
                        joint_name = f"jpos{self.used_j[joint_index]}"
                        curr = dfs[i][joint_name]
                        dfs[i].loc[:, joint_name] = curr + offset_list[joint_index]

        elif offset_choice == "n":
            pass

        return dfs
    
    def filter_jpos(self, dfs): # will move it out to the main menu
        filter_choice = input("Do you want to filter the csv? (y/n) \n")
        if filter_choice == "y":
            filtered_dfs = []
            jpos_name = []
            jvel_name = []
            for joint in self.used_j:
                jpos_name.append("jpos" + str(joint))
                jvel_name.append("jvel" + str(joint))

            # Filter and update the dataframes
            for df in dfs:
                new_df = df[jpos_name + jvel_name]
                filtered_dfs.append(new_df)
        elif filter_choice == "n":
            filtered_dfs = dfs
    
        return filtered_dfs

    def data_prep_bar_plot(self, dfs_new, type):
        # dfs_new is 1D 21 elements after add offsets, filter:
        # 2arm: 3 phys, 3 ambf
        # 0arm: 3 phys, 3 ambf
        # 1arm: 3 phys, 3 ambf
        # cube: 3 phys, 3 ambf

        final_dfs = []
        # final_dfs is 1d array with 9 elements
        # 3 phys csv in two arm mode, 3 phys csv in left arm, 3 phys csv in right arm
        for i in range(len(dfs_new)):
            # for mode two arm
            if i % DF_PER_MODE in self.r:
                final_dfs.append(dfs_new[i])            

        # initialize plotter for 3 phys csv in each mode
        two_arm = meanBarGraph(final_dfs[:3])
        left_arm = meanBarGraph(final_dfs[3:6])
        right_arm = meanBarGraph(final_dfs[6:9])
        cube = meanBarGraph(final_dfs[9:12])

        plotters = [two_arm, left_arm, right_arm, cube]
        mean_list = []
        for p in range((len(MODE))):
            plotters[p].plot_mean_bar_graph(type, self.used_j, GRAPH_PATH + "mean_bar_graph" + MODE[p])
            mean = plotters[p].get_mean_error()
            mean_list.append(mean)

        return mean_list

    def draw_bar_plot(self):
        bar1_value = []
        bar2_value = []
        type = ["jpos", "jvel"]

        categories = ["Both", "Left", "Right", "Both"]
        # categories = ["Two_arm", "Left_arm", "Right_arm", "Two_arm"]
        # Modify the first three categories with D_I and leave the last one with D_II
        # plot(xdata,ydata, xlabel=L"\mathscr{Temperature\hspace{0.6}(°C)}",ylabel=L"\mathscr{Density\hspace{0.6}(g/cm^3)}")
        #  plot(1:5,1:5, xlabel=L"Temperature $\mathfrak{K} \hspace{0.6}(C)$",ylabel=L"Density $\mathfrak{Density} \hspace{0.6} (g/cm^3)$")

        # filter all csv with chosen joints 
        filtered_dfs = self.filter_jpos(self.all_mode_csv)

        # add offsets
        final_dfs = self.add_offset(filtered_dfs)

        bar1_value = self.data_prep_bar_plot(final_dfs, type[0])
        # print("bar1 (jpos): ", bar1_value)
        bar2_value = self.data_prep_bar_plot(final_dfs, type[1])
        # print("bar2 (jvel): ", bar2_value)
        # Creating the positions for the bars on the x-axis
        x = np.arange(len(categories))

        # Width of each bar
        bar_width = 0.35

        # Clear the graph before plotting
        plt.clf()

        # Creating the bar plot
        if self.used_j == BOTH_J: 
            label1 = 'JPos (rad)'
            label2 = 'JVel (rad/s)'
            pos = 0.0003
        else:
            label1 = "JPos (m)"
            label2 = "JVel (m/s)"
            pos = 0.000002

        plt.bar(x - bar_width/2, bar1_value, width=bar_width, label=label1)
        plt.bar(x + bar_width/2, bar2_value, width=bar_width, label=label2)

        # Adding labels, title, and legend
        plt.xlabel('Modes')
        plt.ylabel('Mean Error')
        plt.title(self.title)
        plt.xticks(x, categories)
        plt.legend()

        # add y limit
        # if self.used_j == BOTH_J:
        #     ylim = 0.12
        # elif self.used_j == SLIDING_J:
        #     ylim = 0.002
        
        # plt.ylim(0, ylim)

        # Add counts above each column
        for i, val in enumerate(bar1_value):
            plt.text(i - bar_width/2, val + pos, str(round(val, 2)), ha='center', va='bottom')
        for i, val in enumerate(bar2_value):
            plt.text(i + bar_width/2, val + pos, str(round(val, 2)), ha='center', va='bottom')

        # Show plot
        figure_format = ["png", "svg"]
        filename = GRAPH_PATH + self.title
        for form in figure_format:
            plt.savefig(filename + "." + form, format = form)
        plt.switch_backend('ps')
        plt.savefig(filename + ".eps", format='eps')
        return