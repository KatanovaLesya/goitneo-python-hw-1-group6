#парсер
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

#додавання в словник
def add_contact(args, contacts):
    try:
        name, phone = args 
        if name in contacts:
            return f"The contact {name} exists in the dictionary. Please enter new name."
        contacts[name] = phone
    except ValueError:
        return "Need to enter: add  Name Phone"
    return "Contact added."

#змінити існуючий номер
def change_contact(args, contacts):
    try:
        name = args[0]
        new_phone = args[1]
    except IndexError:
        return "Need to enter: change Name NewPhone"
    phone = contacts.get(name)
    if phone == None:
        phone = 'Name is not found'
        return (phone)
    contacts[name] = new_phone
    return "Contact changed."

#дізнатися номер за імʼям
def user_phone(args, contacts):
    try:
        name = args[0]   
        phone = contacts.get(name)
    except IndexError:
        return "Need to enter: phone Name" 
    if len(args) > 1:
        return "Need to enter: phone Name" 
    if phone == None:
        phone = "Name is not found"
    return (phone)

#вивести список контактів
def all_contacts(contacts):
    list = contacts
    return (list)


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(user_phone(args, contacts))
        elif command == "all":
            print(all_contacts(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
