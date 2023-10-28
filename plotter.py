import pandas as pd
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
        
    def overlay_all_jpos(self, id, filename):
        self.unify_shape()

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
    check.plot_one_jpos(4, graph_path + "one_pos.png")
    check.plot_all_jpos(graph_path + "all_jpos.png")
    check.overlay_one_jpos(5, graph_path + "overlay.png")

if __name__ == "__main__":
    main()
