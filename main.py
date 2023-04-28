int loginID = 0;

def option1():
    print("Option 1 selected")

def option2():
    print("Option 2 selected")

def option3():
    print("Option 3 selected")

def exit_program():
    print("Exiting...")
    quit()

options = {
    '1': option1,
    '2': option2,
    '3': option3,
    '4': exit_program,
}

while True:
    print("Main Menu")
    print("1. Option 1")
    print("2. Option 2")
    print("3. Option 3")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice in options:
        options[choice]()
    else:
        print("Invalid choice. Please try again.")
