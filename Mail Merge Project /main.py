#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


REPLACE = "[name]"

# First read names and save to list
with open("Input/Names/invited_names.txt") as name_file:
    names = name_file.readlines()

# Then read template
with open("Input/Letters/starting_letter.txt") as template_file:
    template = template_file.read()

for line in names:
    invitee = line.strip()
    with open(f"Output/ReadyToSend/invitation_for_{invitee}.txt", "w") \
            as invitation:
        # Replace [name] placeholder from template
        invitation_text = template.replace(REPLACE, invitee)
        invitation.write(invitation_text)
