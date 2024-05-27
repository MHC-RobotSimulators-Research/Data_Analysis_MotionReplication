# Data_Analysis_MotionReplication
Author: Mai Bui (bui23m@mtholyoke.edu)

Data Analysis Motion Replication is a graphing tool designed to analyze and visualize differences between dynamic arrays of CSV files, ideally capturing the same motions or trajectories from two different robots: the physical Raven-II and AMBF (simulator robot). It features eight modes: two for modifying the CSVs (adding offsets and filtering) and six for graphing and quitting. This tool complements the Raven-II Standardized Controller, the source of the data input.

With this tool, you can easily identify which joints have the most differences, what the offsets are, how the joints move, and whether the ROS messages are lagging. This helps determine whether the differences are due to the ROS, robot, or controller and what adjustments should be made.

This tool is developed and thoroughly tested on macOS Sonoma 14.4.1 with Python 3.9. Key libraries include pandas 1.5.3, numpy 1.24.2, matplotlib 3.5.2, and PIL 9.1.1. Users may need to modify the code as needed. To access the tool, navigate to the mai_plotter folder and run main. All graphs are saved inside data_analysis folder. 

## Usage
1. View all available CSVs.
2. Select the number of CSVs to analyze.
3. Choose specific CSVs for analysis.
4. Use the modes to modify and graph the data as needed.

## Modes

### Add Offset
Add an offset to a joint and modify the corresponding columns in the currently analyzed CSV.

### Add Filter
Choose which types of joints to analyze: sliding joints, both arms' rotational joints, left arm rotational joints, or right arm rotational joints.

### Plot One Joint
Plot the movement over time of one specified joint in the selected CSV.
![One_Joint](https://github.com/MHC-RobotSimulators-Research/Data_Analysis_MotionReplication/assets/83102564/9b570a1d-c3f5-4ee5-89e7-c3bc8061076f)


### Plot All Joints
Plot the movement over time of all joints in the selected CSV.
![All_Joints](https://github.com/MHC-RobotSimulators-Research/Data_Analysis_MotionReplication/assets/83102564/e06adb10-28c9-4f11-8902-3f575ad7ac44)

### Plot Overlay
Overlay two specified joints from the selected CSVs or the joints with the smallest and largest gaps between the CSVs.
![Overlay_2_Joints](https://github.com/MHC-RobotSimulators-Research/Data_Analysis_MotionReplication/assets/83102564/e8bd7334-3af4-4db1-9939-206df2520cdf)

### Plot Mean Bar Graph
View the averaged differences between all joints (excluding joints 3 and 11, which are zeros).
![Mean_Bar_Graph](https://github.com/MHC-RobotSimulators-Research/Data_Analysis_MotionReplication/assets/83102564/170989f3-824a-45ff-8358-b4f88040b55c)

### Plot Bar Graph
Visualize the overall differences between the physical Raven-II and AMBF across different experiments, independent of the chosen CSVs, with options to add offsets and filters again.
![AMBF_AMBF](https://github.com/MHC-RobotSimulators-Research/Data_Analysis_MotionReplication/assets/83102564/cdc6f20f-ecba-42fa-86be-e096631d3052)
