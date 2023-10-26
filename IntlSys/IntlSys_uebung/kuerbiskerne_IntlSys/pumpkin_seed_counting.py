import os
import pandas as pd
from scipy.io import arff as sp

# Aufgabe 1
directory = "/home/arabanus/Documents/HSD/daisy/IntlSys/IntlSys_uebung/kuerbiskerne_IntlSys/"
xlsx_file = "Pumpkin_Seeds_Dataset.xlsx"
arff_file = "Pumpkin_Seeds_Dataset.arff"

xlsx_path = os.path.join(directory, xlsx_file)
arff_path = os.path.join(directory, arff_file)

data, meta = sp.loadarff(arff_path) # meta reads in the different columns

df_arff = pd.DataFrame(data)

df_xlsx = pd.read_excel(xlsx_path)

# print(df_arff)
# print(df_xlsx)


# # Aufgabe 2: sind die dataframes identisch?
# if df_xlsx.equals(df_arff):
#     print("Diese Dataframes sind gleich")
# else:
#     print("Diese Columns sind nicht gleich")
#     print(df_xlsx.compare(df_arff, keep_equal=True))


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


isequal = df_arff == df_xlsx

# kleine Zwischenaufgabe!
# finden sie heraus ob in der in jeder
# split into colums:
# access single column



def entry_comparison(input_dataframe1, input_dataframe2):
    """Input: pandas dataframe
    this function iterates through each column, skips if all values are True
    if there are any false values it checks each entry
    Output:
    numb
    
    """
    isequal = input_dataframe1 == input_dataframe2
    
    false_entry_counter = 0
    column_counter = 0
    for column in range(len(isequal.axes[1])):
        single_column = isequal.iloc[:, column]
        column_counter = column_counter + 1
        if single_column.all() == True:
            print(f"In column No. {column_counter}, everything is True")
        else:
            print(f"In column No. {column_counter}, there are False entries")
            row_counter = 0
            for entry in range(single_column.shape[0]):
                entries = single_column.iloc[entry]
                row_counter = row_counter + 1
                if entries == False:
                    false_entry_counter = false_entry_counter + 1
                    print(f"False in row {row_counter}")
                else:
                    print("nothing is wrong!")
            return false_entry_counter, single_column.shape
           

a1, a2 = entry_comparison(df_arff, df_xlsx)
print(f"{a1}/{a2} entries are false")
            
                
            