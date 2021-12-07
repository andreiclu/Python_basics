def add_new_number_in_phonebook():
    contact = input("Write a phone number: ")
    with open("phonebook.txt", "a") as f:
        f.write(contact + '\n')


def show_phonebook():
    with open("phonebook.txt") as f:
        for line in f:
            line = line.strip()
            print(line)

while True:
    choice = int(input('Choose one from this options: 1. Input a new phone number 2. Show Phonebook: And 0 to stop the program'))

    if choice == 1:
        add_new_number_in_phonebook()
    elif choice == 2:
        show_phonebook()
    elif choice ==0:
        break
    else:
        print("Wrong choice!")
