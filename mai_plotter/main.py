
import pandas as pd
from define import *
from plotter import plotter
from overlay import overlay
from meanBarGraph import meanBarGraph 
from barplot import barplot
import PIL
def init():
    # print csv files
    print("Here are a list of csv files:")
    for i in range(len(CSV_FILES_NAME)):
        print("\t["+str(i)+"] :"+str(CSV_FILES_NAME[i]))

def main():
    choice = 0
    while True:
        init()  # Show the list of CSVs
        try:
            num_csvs = int(input(f"How many CSVs do you want to analyze?\n"))
            if not (1 <= num_csvs <= MAX_FILES_INDEX):
                print(f"Invalid input. Please enter a number between 1 and {MAX_FILES_INDEX}.\n")
                continue

            while True:
                try:
                    csv_choices = input(f"Choose the CSVs to analyze (0, 1, 2, ..., {MAX_FILES_INDEX}):\n").split()
                    csv_indices = [int(choice) for choice in csv_choices]
                    if not all(0 <= idx <= MAX_FILES_INDEX for idx in csv_indices) and (len(csv_indices) == num_csvs):
                        print("Invalid input. Please enter valid CSV indices or enter the right amount of csvs.\n")
                        continue 

                    # Perform analysis with selected CSVs
                    csv_path = []
                    for i in csv_indices:
                        csv_path.append(OFFSET_PATH + CSV_FILES_NAME[i])
                    dfs = [0]*num_csvs
                    for i in range(num_csvs):
                        dfs[i] = (pd.read_csv(csv_path[i]))
                        
                    while choice!=7:
                        print("\nChoose an option:\n")
                        print("1. Add offsett\n")
                        print("2. Filter joints\n")
                        print("3. Plot one joint\n")
                        print("4. Plot all joints\n")
                        print("5. Plot overlay\n")
                        print("6. Plot mean bar graph\n")
                        print("7. Plot bar graph\n")
                        print("8. Quit\n")
                        choice = int(input("Enter a number between 1 and 8: \n"))

                        try:

                            if choice < 1 or choice > 8:
                                print("Invalid Input. Please enter a number between 1 and 8. \n")
                                continue
                            
                            # Simulating switch-case 
                            plot = plotter(False, dfs)
                            
                            # Add offset 
                            if choice == 1:
                                print("This will change the original csv we analyze: \n")
                                plot = plotter(True, dfs)
                                print("Offset added")

                            # Filter CSVs
                            if choice == 2:
                                if input("Do you want to filter the CSV? (y/n)\n").lower() == "y":
                                    print("This will change the original CSV we analyze\n")
                                    valid_choices = {"both arms": JOINTS[3], "left arm": JOINTS[0], "right arm": JOINTS[1], "sliding": JOINTS[2]}
                                    while True:
                                        joint_choices = input("Which joints do you want to filter? (both arms, left arm, right arm, sliding):\n").lower()
                                        if joint_choices in valid_choices:
                                            plot.filter_jpos(valid_choices[joint_choices])
                                            print("CSV filtered")
                                            break
                                        else:
                                            print("Invalid input. Please enter one of the following: both arms, left arm, right arm, sliding.\n")
                            
                            # Plot one joint
                            if choice == 3:
                                ans = input(f"Enter csv (1 to {num_csvs}), joint (1-16) and type (jpos, jvel) to plot\n").split()
                                plot.plot_one_jpos(int(ans[0]), int(ans[1]) +1, GRAPH_PATH + "One_Joint", type=ans[2])
                                print(f"Graph One_Joint plotted")
                            
                            # Plot all joints
                            if choice == 4:
                                ans = input(f"Enter csv 1 to {num_csvs} to plot and type (jpos/jvel/dac_vals): \n").split()
                                plot.plot_all_jpos(int(ans[0]), GRAPH_PATH + "All_Joints", ORIGINAL, ans[1])
                                print(f"Graph All_Joints plotted")

                            # Plot overlay
                            if choice == 5:
                                overlay_graph = overlay(dfs)
                                type = input("What type (jpos/jevel/dac_vals)? \n")
                                best_worst = input("Do you want to plot smallest and biggest gap joints between files? (y/n)\n")
                                if best_worst == "y":
                                    meanGraph = meanBarGraph(dfs)
                                    mean_column = meanGraph.create_mean_column(type, ORIGINAL)
                                    #print(*mean_column)
                                    joints = meanGraph.get_best_worst_j()    
                                elif best_worst == "n":
                                    joints = list(map(int, input("Which 2 joint you want to plot overlay?").split()))
                                overlay_graph.overlay_two_jpos(type, joints[0], joints[1], GRAPH_PATH + "Overlay_2_Joints")
                                print(f"Graph Overlay_2_Joints plotted")
                            
                            # Plot mean bar graph
                            if choice == 6:
                                mean_bar_graph = meanBarGraph(dfs)
                                type = input("Enter the type to plot (jpos/jvel/dac_vals):\n")
                                mean_bar_graph.plot_mean_bar_graph(type, ORIGINAL, GRAPH_PATH + "Mean_Bar_Graph")
                                print(f"Graph Mean_Bar_Graph plotted")

                            # Plot bar graph
                            if choice == 7:
                                object_to_draw = input(f"Enter the object to compare {' '.join(OBJECT)}:\n")
                                sliding = input("Do you want to plot rotation joints or sliding arms? (r/s)\n")
                                if sliding == "r":
                                    s = False
                                else:
                                    s = True
                                bar_plot = barplot(object_to_draw, s) 
                                bar_plot.draw_bar_plot()
                                print(f"Graph {object_to_draw} plotted")

                            # Quit
                            if choice == 8:
                                return

                        except ValueError:
                            print("Invalid Input. Please enter a valid choice number. \n")
                except ValueError:
                    print("Invalid Input. Please enter valid csv number. \n")

                
        except (ValueError, FileNotFoundError):
                print("Invalid input. Please enter valid numbers.\n")


if __name__ == "__main__":
    main()