import pandas as pd
import os


def load_files_to_df(working_dir: str):
    files = [x[2] for x in sorted(os.walk(working_dir))]
    dataframes = []
    for i in range(len(files[0])):
        df = pd.read_csv(working_dir + files[0][i])
        df_header = df.head()
        # print(working_dir + files[0][i])
        dataframes.append(df)

    return dataframes, df_header

def norm_to_single_rotation():
    # header = f"{object}, {angle_size}, {hcsr04_distance}, {num_rot}, {measurement_number},"
    
    # split dataframeinto num_rot

    # make new headers with: [object, angle size, hcsr04_distance]

    pass

def calculate_error():
    # compare scanned datapoints to ground truth


    pass

data_dir = "/home/arabanus/Desktop/intlsys_logs/"

all_files_as_dataframes = load_files_to_df(data_dir)

for i in range(len(all_files_as_dataframes)):
    working_df = all_files_as_dataframes[i]
    print(all_files_as_dataframes[i])
    print(50*'-')

