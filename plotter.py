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

def main():
    check = plotter(pd.read_csv("test_trials/test_trial_2_rs.csv"))
    check.plot_one_jpos(3,"data_analysis/one_pos.png")
    # check.plot_all_jpos("all_jpos.png")
    check2 = plotter(pd.read_csv("test_trials/test_trial_1_rs.csv"), pd.read_csv("test_trials/test_trial_2_rs.csv"))
    check2.overlay_one_jpos(4, "data_analysis/overlay.png")
if __name__ == "__main__":
    main()
