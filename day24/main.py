from pathlib import Path
home = str(Path.home())

with open(home + "/Desktop/new_file.txt") as file:
    contents = file.read()
    print(contents)

# with open("new_file.txt", mode="a") as file:
#     file.write("\nNew text.")
