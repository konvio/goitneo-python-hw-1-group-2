import contacts

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def main():
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ").strip().lower()
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            if len(args) != 2:
                print("Invalid command.")
                continue
            contacts.add_contact(*args)
        elif command == "change":
            if len(args) != 2:
                print("Invalid command.")
                continue
            contacts.change_contact(*args)
        elif command == "phone":
            if len(args) != 1:
                print("Invalid command.")
                continue
            contacts.show_contact(*args)
        elif command == "all":
            contacts.show_all()
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()