

data = {}

def add_contact(name, phone):
    data[name] = phone
    print("Contact added")

def change_contact(name, phone):
    if name not in data:
        print("Contact not found")
        return
    data[name] = phone
    print("Contact changed")

def show_contact(name):
    if name not in data:
        print("Contact not found")
        return
    print(f"{data[name]}")

def show_all():
    for name, phone in data.items():
        print(f"{name}: {phone}")


