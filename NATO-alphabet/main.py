import pandas as pd

df = pd.read_csv('nato_phonetic_alphabet.csv')

# print(df)
# Loop through rows of a data frame
# for (index, row) in df.iterrows():
#     # #Access index and row
#     # #Access row.student or row.score
#     print(row.letter)
#     print(row.code)

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
nato_dict = {row.letter:row.code for (index, row) in df.iterrows()}
# print(nato_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def print_NATO_codes():
    word = input("Enter a word: ").upper()
    try:
        codes = [nato_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        return False
    else:
        print(codes)
        return True


while not print_NATO_codes():
    continue
