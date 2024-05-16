from os import listdir
from os.path import isfile, join
NUM_CSV = 3

GRAPH_PATH = "data_analysis/"
CSV_PATH = "raven_data/the_good_stuff/"
OFFSET_PATH = "offset_fixed/"
CSV_FILES_NAME = [f for f in listdir(OFFSET_PATH) if isfile(join(OFFSET_PATH, f))]
MAX_FILES_INDEX = len(CSV_FILES_NAME) - 1
MODE = ["2arm", "0arm", "1arm", "cube"]
DF_PER_MODE = 6
OBJECT = ["PHYS_PHYS", "AMBF_AMBF", "PHYS_AMBF"]

LEFT_J = [0,1,4,5,6,7]
RIGHT_J = [8,9,12,13,14,15]
SLIDING_J = [2,10]
BOTH_J = [0,1,4,5,6,7,8,9,12,13,14,15]
ORIGINAL = [0,1,2,4,5,6,7,8,9,10,12,13,14,15]

