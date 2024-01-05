"""
vorbereitung der Trainingsdaten
jede messdatei hat eine dazugehörige Metadaten datei in folgendem Format:

{object}
{angle_size}
{hcsr04_distance}
{num_rot}
{measurement_number}
"""
import pandas as pd
import matplotlib.pyplot as plt
import os


def load_files_to_df(working_dir: str):
    files = [x[2] for x in sorted(os.walk(working_dir))]
    # print(files)
    dataframes = []
    for i in range(len(files[0])):
        df = pd.read_csv(working_dir + files[0][i], header=None)
        # df_header = df.head()
        # print(working_dir + files[0][i])
        dataframes.append(df)

    return dataframes

def norm_to_single_rotation(df):
    num_rot = 10
    angle_size = 360/60

    # removes not needed data from df

    

    # number of measurements per rot
    interval = int(df.shape[0]/num_rot)
    
    # split df into single full rotations
    # adjust interval so that graphs overlap
    df_1 = df.iloc[:interval]
    df_2 = df.iloc[interval:2*interval]
    df_3 = df.iloc[2*interval:3*interval]
    df_4 = df.iloc[3*interval:4*interval]
    df_5 = df.iloc[4*interval:5*interval]
    df_6 = df.iloc[5*interval:6*interval]
    df_7 = df.iloc[6*interval:7*interval]
    df_8 = df.iloc[7*interval:8*interval]
    df_9 = df.iloc[8*interval:9*interval]
    df_10 = df.iloc[9*interval:-1]

    df_1.reset_index(inplace=True)
    df_2.reset_index(inplace=True)
    df_3.reset_index(inplace=True)
    df_4.reset_index(inplace=True)
    df_5.reset_index(inplace=True)
    df_6.reset_index(inplace=True)
    df_7.reset_index(inplace=True)
    df_8.reset_index(inplace=True)
    df_9.reset_index(inplace=True)
    df_10.reset_index(inplace=True)
    
    # split dataframeinto num_rot

    # make new headers with: [object, angle size, hcsr04_distance]

    return df_1, df_2, df_3, df_4, df_5, df_6, df_7, df_8, df_9, df_10

def calculate_error():
    # compare scanned datapoints to ground truth
    pass

data_dir = "/home/arabanus/Desktop/intlsys_logs/"
all_files_as_dataframes = load_files_to_df(data_dir)
df = all_files_as_dataframes[-3]

# print(df)

single_rot_split = norm_to_single_rotation(df)
print(single_rot_split)

fig = plt.figure()

axis1 = fig.add_subplot(1, 1, 1)
axis1.plot(single_rot_split[0].iloc[:, 3], color="r")
axis1.plot(single_rot_split[1].iloc[:, 3], color="b")
axis1.plot(single_rot_split[2].iloc[:, 3], color="g")
axis1.plot(single_rot_split[3].iloc[:, 3], color="y")
axis1.plot(single_rot_split[4].iloc[:, 3], color="c")
axis1.plot(single_rot_split[5].iloc[:, 3], color="m")
axis1.legend(["first rot", "second rot", "third rot"])

plt.show()
