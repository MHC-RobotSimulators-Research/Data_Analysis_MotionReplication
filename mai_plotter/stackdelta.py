import matplotlib.pyplot as plt

class stackdelta:
    def __init__(self, offset, df1, df2=None, df3=None):
        self.df1 = df1
        self.df2 = df2
        self.df3 = df3

    def stackdelta(self, filenames):
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