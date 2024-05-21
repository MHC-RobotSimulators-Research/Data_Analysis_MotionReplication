# Data_Analysis_MotionReplication
Author: Mai Bui (bui23m@mtholyoke.edu)

Data Analysis Motion Replication is a graphing tool designed to analyze and visualize differences between dynamic arrays of CSV files, ideally capturing the same motions or trajectories from two different robots: the physical Raven-II and AMBF (simulator robot). It features eight modes: two for modifying the CSVs (adding offsets and filtering) and six for graphing and quitting. This tool complements the Raven-II Standardized Controller, the source of the data input.

With this tool, you can easily identify which joints have the most differences, what the offsets are, how the joints move, and whether the ROS messages are lagging. This helps determine whether the differences are due to the ROS, robot, or controller and what adjustments should be made.

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

### Plot All Joints
Plot the movement over time of all joints in the selected CSV.

### Plot Overlay
Overlay two specified joints from the selected CSVs or the joints with the smallest and largest gaps between the CSVs.

### Plot Mean Bar Graph
View the averaged differences between all joints (excluding joints 3 and 11, which are zeros).

### Plot Bar Graph
Visualize the overall differences between the physical Raven-II and AMBF across different experiments, independent of the chosen CSVs, with options to add offsets and filters again.
