with open("Input/Names/invited_names.txt") as names:
    names_list = names.readlines()
    names_list = [name.strip() for name in names_list]
    # print(names_list)

with open("Input/Letters/starting_letter.txt") as temp:
    temp_letter = temp.read()

for name in names_list:
    letter_name = f"letterFor{name}".strip()
    newletter = temp_letter.replace("[name]",name)
    with open(f"Output/ReadyToSend/{letter_name}.txt",'w') as mail:
        mail.write(newletter)