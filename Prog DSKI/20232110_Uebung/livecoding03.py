# bib für terminal sachen
# path abfragen, verzeichnisse herstellen etc
import os

# current working directory
print("Result from print(os.getcwd()) (current working directory):")
print(os.getcwd())

# files and folders in working dir
print("Result from print(os.listdir()) (current working directory):")
print(os.listdir())
for filename in os.listdir():
    if filename.endswith(".md"):
        print(f"{filename} is a markdown file")


filename = "test.txt"
# with ... as ... : macht so eine geschlossene temp. variable...(?)
with open(filename, "w") as file:
    file