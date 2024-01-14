# uebung 09
import pandas as pd

# A1
working_dir = "/home/arabanus/Downloads/archive/"
filename = "pokemon.csv"

df = pd.read_csv(working_dir + filename)
# print(df.columns)
df_sorted_by_weight = df.sort_values(by=['weight_kg'])

# A1
# A) Wie schwer maximal sind die leichtesten 10% aller Pokemon (Gewicht steht unter "weight_kg")?
print(f"A1 a) Die leichtesten 10% aller Pokemon wiegen {df['weight_kg'].quantile(q=0.1, interpolation='higher')}kg")

# B) Wie schwer minimal sind die schwersten 10% aller Pokemon?
print(f"A1 b) Die minimal schwersten Pokemon der top 10% sind {df['weight_kg'].quantile(q=0.9,)}kg")

# C) Wie schnell maximal sind die langsamsten 10% aller Pokemon?
print(f"A1 c) Das maximal schnellste Pokemon der langsamsten 10% hat eine Geschw. von {df['speed'].quantile(q=0.1,)}")

# D) Wie schnell minimal sind die schnellsten 10% aller Pokemon?
print(f"A1 c) Das minimal schnellste Pokemon der schnellsten 10% hat eine Geschw. von {df['speed'].quantile(q=0.9,)}")

print(50*"-")

# Student scores
df1 = pd.DataFrame({
    'id':[101, 107, 133, 204, 304],
    'Name': ['Alex', 'Amy', 'Allen', 'Bran', 'Betty'],
    'subject_1_score':[8.2, 6.0, 8.8, 4.5, 7.5]})

df2 = pd.DataFrame({
    'id':[101, 107, 204, 634, 304],
    'Name': ['Alex', 'Amy', 'Bran', 'Bryce', 'Betty'],
    'subject_2_score':[8.6, 5.0, 9.2, 6.8, 6.2]})

# Merge student data
full_data = pd.merge_ordered(df1, df2)
full_data = full_data.set_index("Name")

for student_name in full_data.index:
    print("\n" + student_name)
    mean_score = full_data.loc[student_name,['subject_1_score', 'subject_2_score']].mean()
    print(f"Mean score: {mean_score}")

    missing_scores = full_data.loc[student_name,['subject_1_score', 'subject_2_score']].isnull().values.any()
    print(f"Missing scores?: {missing_scores}")