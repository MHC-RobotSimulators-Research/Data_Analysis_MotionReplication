import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class plotter:
    def __init__ (self, df1, df2=None):
        # plotter for 2 csv
        self.df1 = df1
        self.df2 = df2

    def plot_one_jpos(self, id, filename):
        # line chart for one jpos
        joint_name = "jpos" + str(id)
        self.df1.plot('time', joint_name)
        plt.savefig(filename)

    def plot_all_jpos(self, filename):
        # line chart for all jpos
        df_jpos = self.df1[self.df1.columns[0:17]] 
        df_jpos.set_index('time', inplace=True)
        df_jpos.plot()
        plt.savefig(filename)

    def unify_shape(self):
        num_row1 = self.df1.shape[0] 
        num_row2 = self.df2.shape[0] 
        if num_row1<= num_row2:
            self.df2 = self.df2.iloc[:num_row1,:]
        else:
            self.df1 = self.df1.iloc[:num_row2,:]

    def overlay_one_jpos(self, id, filename):
        # make 2 dataframe the same size
        self.unify_shape()
        # overlay one jpos from 2 different recording times
        joint_name = "jpos" + str(id)
        df1_joint = self.df1[joint_name].values
        df2_joint = self.df2[joint_name].values
        #id_arr = self.df1.index.values
        overlay_df = pd.DataFrame(
            {
            "df1": df1_joint,
            "df2": df2_joint }
        )
        overlay_df.plot()
        plt.savefig(filename)

    def lineGraph2(self, filenames):
        for i in range(16):
            jpos = "jpos" + str(i)
            #plt.clf()
            df1_column = self.df1[jpos]
            df2_column = self.df2[jpos]
            diff = df1_column - df2_column
            graph = diff.plot(color = "orange")
            
            # Add a baseline at 0
            graph.axhline(0, color='gray', linestyle='--', linewidth=1)
            plt.savefig(filenames[i])

    def mean_bar_graph(self, filename):

        #create mean, jpos column and bar_color for positive mean = green, negative mean = orange
        mean_column = []
        jpos_column = []
        bar_color = []
        for i in range(16):
            jpos = "jpos" + str(i)
            plt.clf()
            # count mean
            df1_column = self.df1[jpos]
            df2_column = self.df2[jpos]
            diff = df1_column - df2_column
            mean = diff.mean()
            if mean < 0:
                bar_color.append("orange")
            elif mean > 0:
                bar_color.append("g")
            else:
                bar_color.append("b")
            mean_column.append(mean)
            jpos_column.append(jpos)

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
        plt.savefig(filename)
        return

def create_path(i):
    return "2023-10-28 17_54_29/test_mai_trial" + str(i) + ".csv"

def main():
    csv_path = []
    for i in range(0,4):
        csv_path.append(create_path(i))
    # initialize plotter object 
    check = plotter(pd.read_csv(csv_path[0]), pd.read_csv(csv_path[3]))
    # save fig
    graph_path = "data_analysis/"
    check.plot_one_jpos(2, graph_path + "one_pos.png")
    check.plot_all_jpos(graph_path + "all_jpos.png")
    check.overlay_one_jpos(2, graph_path + "overlay.png")
    check.mean_bar_graph(graph_path + "mean_bar_graph.png")
    
if __name__ == "__main__":
    main()
