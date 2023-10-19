import os
import pandas as pd
from scipy.io import arff as sp

# Aufgabe 1
directory = "/home/arabanus/Documents/HSD/daisy/IntlSys/IntlSys_uebung/20231019_Praktikum/"
xlsx_file = "Pumpkin_Seeds_Dataset.xlsx"
arff_file = "Pumpkin_Seeds_Dataset.arff"

xlsx_path = os.path.join(directory, xlsx_file)
arff_path = os.path.join(directory, arff_file)

data, meta = sp.loadarff(arff_path) # meta reads in the different columns

df_arff = pd.DataFrame(data)

df_xlsx = pd.read_excel(xlsx_path)


print(df_arff)
print(df_xlsx)


# Aufgabe 2: sind die dataframes identisch?
if df_xlsx.equals(df_arff):
    print("Diese Dataframes sind gleich")
else:
    print("Diese Columns sind nicht gleich")
    print(df_xlsx.compare(df_arff, keep_equal=True))


# # Concatenate dataframes df_arff and df_xlsx, dropping the 'Class' column from both
# df_comparison = pd.concat([df_arff.drop(columns=["Class"]), df_xlsx.drop(columns=["Class"])])
# # Reset the index of the concatenated dataframe and drop the old index
# df_comparison = df_comparison.reset_index(drop=True)

# # Group the concatenated dataframe by its columns
# df_comparison_gpby = df_comparison.groupby(list(df_comparison.columns))

# # Get the index of records that are unique (present in only one of the dataframes)
# # x[0] represents the first element of each group, and len(x) == 1 checks if it's unique
# idx_unique = [x[0] for x in df_comparison_gpby.groups.values() if len(x) == 1]

# # Print the unique records based on their index
# print(df_comparison.reindex(idx_unique))
