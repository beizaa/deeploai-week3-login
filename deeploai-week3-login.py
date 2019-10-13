# LOGIN SYSTEM

# Start with a home page . E.g. Hello there! This is my lovely homepage.

print("""        __________________________________________________


          Hello there! This is my lovely homepage

          _____________________________________________""")

username_password_matches = {'beyza': '123', 'ayse':'234'}  # to store data



# Sign Up section
def signup():
    a =10000
    print("---------------Here is the sign up section------------")
    while a > 0:
        username = input("Please enter a username(It should be unique): ")  # Set a user name (should be unique)
        if username not in username_password_matches:
            password = input("Hello, {}. Please enter your password: ".format(username)) #If passwords match and username is unique then
            confirmation = input("""Your username is {},
and your password is {}. If these info is True please enter 'True',  
and otherwise enter 'False': """.format(username, password))
            a-=1
            if confirmation == 'True':
                print("Your account is set")
                username_password_matches[username] = password  # Store this information to log in next time.
                break
            elif confirmation == 'False':
                print("Try again")
                continue
        else:
            print("This name is already taken, try again.")
            continue

# Sign in section
def signin():
    print("-----Sign in Section-----")
    count = 10000
    while count > 0:
        signin_username = input("What is your username?: ")  # What is your username?
        signin_password = input("What is your password?: ")  # What is your password?
        if signin_username in username_password_matches and username_password_matches[signin_username] == signin_password:
            print("You have successfully logged in!!!")  # If username and pasword match then you can log in.

            break
        else:
            print(
                "It is not a valid username, your further attempts are forbidden.")  # Note: If person can't login, do not let him to see your home page.
            break
        count -= 1


# Do you have an account ? Yes or No If yes: Sign in If no: Sign up.
a = 1000
while a > 0:
    b = input("Do you have an account?: ")
    if b == "Yes":
        signin()
        break
    elif b == "No":
        signup()
        break
    else:
        print("Please enter 'Yes' or 'No'.")

# Recommended elements to build this project

#    Lists
#    Dictionary
#    Loops
#    Input
#    Functions
#    Comparison operators

# Reminder
