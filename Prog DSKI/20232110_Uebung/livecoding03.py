# # bib für terminal sachen
# # path abfragen, verzeichnisse herstellen etc
# import os

# #%%
# # current working directory
# print("Result from print(os.getcwd()) (current working directory):")
# print(os.getcwd())

# #%%
# # files and folders in working dir
# print("Result from print(os.listdir()) (current working directory):")
# print(os.listdir())
# for filename in os.listdir():
#     if filename.endswith(".md"):
#         print(f"{filename} is a markdown file")

# #%%
# filename = "test.txt"
# # with ... as ... : macht so eine geschlossene temp. variable...(?)
# with open(filename, "w") as file:
#     file
    
# #%%
# # check if file exists, create or remove depending...
# file_results = "my_data.csv"
# print(os.path.exists(file_results))

# if os.path.exists(file_results):
#     print("file exists! \nremoved file!")
#     os.remove(file_results)
# else:
#     print("file does not exist \ncreating file!")
#     open(file_results, 'x')
    
#%%

user_input = input("input a number, I'll root it: ")

try:
    number = float(user_input)
    if number < 0:
        raise ValueError("please dont use negatives, i cant compute that.... :(")
    root = number ** 0.5
    print(f"the root of {number} is {root}")
except ValueError as msg:
    print(msg)

