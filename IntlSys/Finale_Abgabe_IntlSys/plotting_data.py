import matplotlib.pyplot as plt
import pandas as pd

path = "/home/arabanus/Desktop/intlsys_logs/"

file_a = "logfile_nothing_ear_5deg-steps.txt"
file_b = "logfile_nothing_ear_2_pulldown_5deg-steps.txt"


input_file_a = path + file_a
input_file_b = path + file_b

df_no_pulldown = pd.read_csv(input_file_a, header=None)

df_pulldown = pd.read_csv(input_file_b, header=None)

df_1 = df_no_pulldown.iloc[:143]
df_2 = df_pulldown.iloc[:143]



plt.plot(df_1[0], df_1[2], 'r')
plt.plot(df_2[0], df_2[2], 'g')
# plt.plot(df_3[0], df_3[2], 'b')
plt.show()


