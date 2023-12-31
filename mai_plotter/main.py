
import pandas as pd
from define import *
from plotter import plotter
from overlay import overlay
from meanBarGraph import meanBarGraph 
from barplot import barplot

def create_path(mode):
    csv_path = []
    for i in range(1,4):
        csv_path.append(OFFSET_PATH + mode + "__p" + str(i) + ".csv")
    for i in range(1,4):
        csv_path.append(OFFSET_PATH + mode + "__a" + str(i) + ".csv")

    return csv_path

def main():

    choice = 0
    # show menu
    mode = input("Choose mode to analyze (0arm - left arm, 1arm - right arm, 2arm, cube) or 'q' to quit\n")
    if mode != "q": 
        csv_path = create_path(mode = mode)
        # initialize df
        csv_choices = input("Choose csv to analyze (1,2,3: phys; 4,5,6: ambf)\n").split()
        csv1, csv2, csv3 = map(int, csv_choices)
        df1 = pd.read_csv(csv_path[csv1-1])
        df2 = pd.read_csv(csv_path[csv2-1])
        df3 = pd.read_csv(csv_path[csv3-1])
    else:
        return
    
    while choice!=8:
        print("\nChoose an option:\n")
        print("1. Plot one joint\n")
        print("2. Plot all joints\n")
        print("3. Add offset\n")
        print("4. Plot overlay\n")
        print("5. Plot mean bar graph\n")
        print("6. Plot bar graph\n")
        print("7. Quit\n")
        choice = int(input("Enter a number between 1 and 7: \n"))

        try:

            if choice < 1 or choice > 7:
                print("Invalid Input. Please enter a number between 1 and 7. \n")
                continue
            
            # Simulating switch-case 
            plot = plotter(False, df1, df2, df3)
            # Plot one joint
            if choice == 1:
                ans = input("Enter csv (1,2,3), joint (1-16) and type(jpos, jvel) to plot\n").split()
                plot.plot_one_jpos(int(ans[0]) + 1, int(ans[1]) + 1, "One_Joint", type=ans[2])
            
            # Plot all joints
            if choice == 2:
                df = int(input("Enter csv (1,2,3) to plot: \n"))
                plot.plot_all_jpos(df, GRAPH_PATH + "All_Joints")

            # Add offset 
            if choice == 3:
                print("This will change the original csv we analyze: \n")
                plot = plotter(True, df1, df2, df3)

            # Plot overlay
            if choice == 4:
                overlay_graph = overlay(df1, df2, df3)
                graph_type = int(input("Enter type of graph you want plot" + "(1: plot 1 joint over index, 2: plot 1 joint over time, 3: plot 2 joints over time) \n"))
                if graph_type == 1:
                    overlay_graph.overlay_one_jpos_index()
                elif graph_type == 2:
                    overlay_graph.overlay_one_jpos_time()
                else:
                    type = input("What type (jpos/jevel)? \n")
                    best_worst = input("Do you want to plot best and worst joints? (y/n)\n")
                    if best_worst == "y":
                        
                        meanGraph = meanBarGraph(df1, df2, df3)
                        mean_column = meanGraph.create_mean_column(type, ORIGINAL, "Best_Worst_overlay")
                        print(*mean_column)
                        joints = meanGraph.get_best_worst_j()    
                    elif best_worst == "n":
                        joints = list(map(int, input("Whhich 2 joint you want to plot overlay?").split()))
                    overlay_graph.overlay_two_jpos(type, joints[0], joints[1], GRAPH_PATH + "Overlay_2_Joints_" + mode)
            
            # Plot mean bar graph
            if choice == 5:
                mean_bar_graph = meanBarGraph(df1, df2, df3)
                type = input("Enter the type to plot (jpos/jvel):\n")
                mean_bar_graph.plot_mean_bar_graph(type, GRAPH_PATH + "Mean_Bar_Graph")

            # Plot bar graph
            if choice == 6:
                object_to_draw = input("Enter the object to compare (AMBF_AMBF/ PHYS_AMBF/ PHYS_PHYS):\n")
                sliding = input("Do you want to plot rotation joints or sliding arms? (r/s)\n")
                if sliding == "r":
                    s = False
                else:
                    s = True
                bar_plot = barplot(object_to_draw, s) 
                bar_plot.draw_bar_plot()

            if choice == 7:
                return

        except ValueError:
            print("Invalid Input. Please enter a valid number. \n")


if __name__ == "__main__":
    main()