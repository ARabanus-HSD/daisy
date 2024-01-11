import matplotlib.pyplot as plt
import pandas as pd

data_dir = "/home/arabanus/Desktop/intlsys_logs/"
m_1 = "logfile_deo_dose_53mm.txt"
m_2 = "logfile_rubicscube_1.txt"
m_3 = "logfile_rubicscube_zweite_messung.txt"
m_4 = "logfile_dose_zweite_messung.txt"
m_5 = "logfile_dose_dritte_messung.txt"

df_dose = pd.read_csv(data_dir + m_1, header=None)
df_cube = pd.read_csv(data_dir + m_2, header=None)
df_cube2 = pd.read_csv(data_dir + m_3, header=None)
df_dose2 = pd.read_csv(data_dir + m_4, header=None)
df_dose3 = pd.read_csv(data_dir + m_5, header=None)


# PLOTTING

fig = plt.figure(figsize=(16, 9), dpi=70)

axis1 = fig.add_subplot(5, 1, 1)
axis1.plot(df_dose, color="r")
#axis1.plot(df_empty, color="b")
axis1.legend(["dose"])
for i in range(9):
    axis1.axvline(x = 61 + i*61, color="g", label="rotation")

axis2 = fig.add_subplot(5, 1, 2)
axis2.plot(df_dose2, color="r")
#axis2.plot(df_empty, color="b")
axis2.legend(["dose 2"])
for i in range(9):
    axis2.axvline(x = 61 + i*61, color="g", label="rotation")

axis3 = fig.add_subplot(5, 1, 3)
axis3.plot(df_dose3, color="r")
#axis3.plot(df_empty, color="b")
axis3.legend(["dose 3"])
for i in range(9):
    axis3.axvline(x = 61 + i*61, color="g", label="rotation")

axis4 = fig.add_subplot(5, 1, 4)
axis4.plot(df_cube, color="r")
#axis4.plot(df_empty, color="b")
axis4.legend(["cube"])
for i in range(9):
    axis4.axvline(x = 61 + i*61, color="g", label="rotation")

axis5 = fig.add_subplot(5, 1, 5)
axis5.plot(df_cube2, color="r")
#axis5.plot(df_empty, color="b")
axis5.legend(["cube 2"])
for i in range(9):
    axis5.axvline(x = 61 + i*61, color="g", label="rotation")


plt.show()