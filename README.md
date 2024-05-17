# Data_Analysis_MotionReplication
Author: Mai Bui (bui23m@mtholyoke.edu)

Data Analysis Motion Replication is a graphing tool that analyze and visualize the differences between dynamic
array of CSVs files: ideally doing the same motions or trajectories and from 2 different robot: physical Raven-II
and AMBF (simulator robot). It has 8 modes: 2 modes for changing the csvs (add offsets and filter csvs) and 5 modes
for graphing and quit. This is used along with the Raven-II Standardized Controller, which is the source of the data
input. 

Thanks to this tool, we easily find which joint has most differences and what is the offsets are. How the joints movement
looks like and if the ROS message sends are lagging or not, whichever cause the differences: ROS, robot or controller. And 
how much should we change.

The user will see all of the existed csvs, have option to pick how many csvs they want to analyze and pick those csvs. All of 
the chosen csvs will then be used to analyze by all mode instead of the plot bar graph which will basically analyze all of the 
csvs to have a big picture summarized. 

## Add offset
This will add an offset into a joint and change the currently analyzed csv of that specific columns. 

## Add filter
This will provide option of which types of joints you want to analyze: sliding joints, rotation joints, left arms, right arms, with or without joint 3 and joint 11 default to 0.

## Plot one joint
Plot movement over time of one given joint in given csv. 

## Plot all joints
Plot movement over time of all joints in given csv.

## Plot overlay
This will overlay 2 either given joints of a given csvs or smallest and biggest gap joints between given csvs.

## Plot mean bar graph
View the averaged differences between all the joints.

## Plot bar graph
The overall differences between physical Raven-II and AMBF in different experiments. 
