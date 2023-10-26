import pumpkin_seed_counting as besser_als_all_func_von_pandas
import os
import pandas as pd
from scipy.io import arff as sp

# LOAD INPUT SHIT
directory = "/home/arabanus/Documents/HSD/daisy/IntlSys/IntlSys_uebung/kuerbiskerne_IntlSys/"
xlsx_file = "Pumpkin_Seeds_Dataset.xlsx"
arff_file = "Pumpkin_Seeds_Dataset.arff"

xlsx_path = os.path.join(directory, xlsx_file)
arff_path = os.path.join(directory, arff_file)

data, meta = sp.loadarff(arff_path) # meta reads in the different columns

df_arff = pd.DataFrame(data)

df_xlsx = pd.read_excel(xlsx_path)


# einzeiler für Dalia
a= besser_als_all_func_von_pandas(df_arff, df_xlsx)
print(f"{a[0]}/{a[1]} entries are false")