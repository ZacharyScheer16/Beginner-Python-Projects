from cryptography.fernet import Fernet

pwd = input("What is the master password: ")



def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = (line.rstrip())
            user, passw = data.split("|")
            print("User: " ,user, "Password: ", passw)

def add():
    account_name = input("account name: ")
    password = input("Password: ")

    # Open the file in 'append' mode ('a')
    with open('passwords.txt', 'a') as f:
        # Write the account name, the separator, the password,
        # AND THE NEWLINE CHARACTER (\n)
        f.write(account_name + "|" + password + "\n")



while True:
    mode = input("Would you like to add a new password or view existing (view/add), press q to quit: ").lower().strip()

    if mode == "q":
        print("Goodbye!")
        break

    if mode == "view":
        view() # <-- FIX: Call the completed view function
    elif mode == "add":
        add()  # <-- FIX: Call the completed add function
    else:
        print("Invalid Mode. Please enter 'view', 'add', or 'q'.")
        # The loop will automatically start over and ask for the mode again.