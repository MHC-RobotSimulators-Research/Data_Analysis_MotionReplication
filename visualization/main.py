from define import *
from readFiles import *
from lineplot import *
from histogram import *
from barplot import *
import sys

def main():
    if sys.argv[1] == '1':
        print("method1")
        file_names = sys.argv[2]
        column_lists = sys.argv[3]

        print(file_names)
        print(column_lists)

        lineplot = LinePlot()
        lineplot.lineGraph1(file_names, column_lists)

    elif sys.argv[1] == '2':
        print("method2")
        histogram = Histogram()

        if len(sys.argv) == 2:
            file_names = sys.argv[2]
            histogram.lineGraph2(file_names)
        
        else:
            file_names = sys.argv[2]
            column_lists = sys.argv[3]
            histogram.lineGraph3(file_names, column_lists)

    else:
        file_names = sys.argv[2]
        column_lists = sys.argv[3]

        barplot = BarPlot()
        barplot.lineGraph4(file_names, column_lists)

if __name__ == "__main__":
    main()
