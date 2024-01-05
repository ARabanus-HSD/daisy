import matplotlib.pyplot as plt
import pandas as pd

data_dir = "/home/arabanus/Desktop/"
m_1 = "23_Messungen.xlsx"

df_dose = pd.read_excel(data_dir + m_1, header=None)


# PLOTTING

fig = plt.figure()

axis1 = fig.add_subplot(3, 1, 1)
axis1.plot(df_dose.loc[:, 0], color="r")
axis1.set_yticklabels("")

axis2 = fig.add_subplot(3, 1, 2)
axis2.plot(df_dose.loc[:, 1], color="r")
axis2.set_yticklabels("")

axis3 = fig.add_subplot(3, 1, 3)
axis3.plot(df_dose.loc[:, 2], color="r")
axis3.set_yticklabels("")

plt.show()