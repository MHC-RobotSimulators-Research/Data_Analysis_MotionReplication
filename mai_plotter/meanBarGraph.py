import pandas as pd
import matplotlib.pyplot as plt

from define import *

class meanBarGraph:
    def __init__(self, dfs):
        self.dfs = dfs
        self.mean_column = []

    def create_mean_column(self, type, used_j):
        #create mean, jpos column and bar_color for positive mean = green, negative mean = orange
        jpos_column = []
        bar_color = []
        df_column = []
        for i in used_j:
            jpos = type + str(i)
            # plt.clf()
            # count mean
            for df in self.dfs:
                df_column.append(df[jpos])

            diff = pd.concat(df_column, axis=1)
            diff['max_difference'] = diff.apply(lambda x: x.max() - x.min() if x.max() > x.min() else x.min() - x.max(), axis=1)

            # Calculate the mean of the maximum differences across columns
            mean = diff['max_difference'].mean()

            if mean < 0:
                bar_color.append("orange")
            else:
                bar_color.append("g")

            self.mean_column.append(mean)
            jpos_column.append(jpos)

        # count the mean number of all means to represent the overal performance
        self.mean_error = sum(abs(mean) for mean in self.mean_column)/14
        # print("create mean column ",self.mean_column)
        return jpos_column, bar_color
        
    def plot_mean_bar_graph(self, type, used_j, filename):

        cols = self.create_mean_column(type, used_j)
        jpos_column = cols[0]
        bar_color = cols[1]
        #create pandas dataframe with above columns
        mean_bar = pd.DataFrame({"Mean Differences": self.mean_column, "Joint Position" if type == "jpos" else "Joint Velocity": jpos_column})
        # create bar plots        
        graph = mean_bar.plot(kind = "bar", x = "Joint Position" if type == "jpos" else "Joint Velocity", y = "Mean Differences", legend=False, color=bar_color)
        # Add a baseline at 0
        graph.axhline(0, color='gray', linestyle='--', linewidth=1)
        # Add labels and title
        plt.xlabel("Mean Differences")
        plt.ylabel( "Joint Position" if type == "jpos" else "Joint Velocity")
        plt.title("Mean Differences of " +  "Joint Position" if type == "jpos" else "Joint Velocity")

        #add overal mean in the right corner
        graph.text(0.95, 0.95, f"Mean Error: {self.mean_error:.2f}", transform=graph.transAxes, fontsize=12,
            verticalalignment='top', horizontalalignment='right', bbox=dict(boxstyle='round,pad=0.5', edgecolor='gray', facecolor='white'))
        self.save_figure(filename=filename)
        return
    
    def get_mean_error(self):
        return self.mean_error
    
    def get_mean_column(self):
        return self.mean_column
    
    def get_best_worst_j(self):
        best = max(self.mean_column)
        worst = min(self.mean_column)
        return self.mean_column.index(best), self.mean_column.index(worst)
    
    def save_figure (self, filename):
        figure_format = ["png", "svg"]
        for form in figure_format:
            plt.savefig(filename + "." + form, format = form)
        plt.switch_backend('ps')
        plt.savefig(filename + ".eps", format='eps')