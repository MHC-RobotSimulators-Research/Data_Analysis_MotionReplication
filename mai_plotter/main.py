import plotter
import pandas as pd

def create_path(mode):
    csv_path = []
    for i in range(1,4):
        csv_path.append("raven_data/" + mode + "_phys" + str(i) + ".csv")
    for i in range(4,7):
        csv_path.append("raven_data/"+ mode + "_ambf" + str(i) + ".csv")

    return csv_path
def main():
    csv_path = create_path(mode = "leftarm_p5")
    print(csv_path)
    # initialize plotter object 
    df1 = pd.read_csv(csv_path[1])
    df2 = pd.read_csv(csv_path[2])
    print(csv_path[0] + ","  + csv_path[1])
    check = plotter.plotter(df1, df2)
    # save fig
    graph_path = "data_analysis/"
    # check.plot_one_jpos(2, graph_path + "one_pos.png")
    # check.plot_all_jpos(graph_path + "all_jpos.png")
    joint_l = [1,15]#list(range(0,16))
    offset_list = [0]*16
    offset_list[0] = offset_list[8] = 30
    offset_list[1] = 13
    offset_list[9] = 17
    offset_list[2] = offset_list[10] = -23
    # print(offset_list)
    # check.regenerate_csv_offset(offset_list)
    # for j in joint_l:
    #      check.overlay_one_jpos(j, graph_path + "jpos" + str(j) + "overlay_2" )
    check.overlay_one_jpos(joint_l[0],joint_l[1],  graph_path + "2overlay")
    check.mean_bar_graph(graph_path + "mean_bar_graph" + "new" )
    # stack_path = graph_path + "stack_delta/"
    # sp = []
    # for i in range (16):
    #     sp.append(stack_path + "j" + str(i) + ".png")
    # sp.append(stack_path + 'totalj.png')
    # check.lineGraph2(sp)

if __name__ == "__main__":
    main()