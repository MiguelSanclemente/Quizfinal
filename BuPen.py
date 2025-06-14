import re


def Library():
    print("""
        +------------------------------------+
        |                                    |
        |  Welcome to the Univalle library!  |
        |                                    |
        +------------------------------------+
         """)
    
    print("""
        +------------------------------------+
        | do you want to turn on the program?|
        |                                    |   
        | 1. yes                             |
        | 2. No                              |
        +------------------------------------+
         """)

    select = input("Please select an option (1 or 2): ")
    # This block uses match-case to handle the user's menu selection.
    # If the user selects "1", the program continues.
    # If the user selects "2", the program closes.
    # Any other input will show an error and ask again.
    match select:
        case "1":
            print(" inicialited successfully!")
            return True
        case "2":
            print("The univalle library program has been closed.")
            exit()
        case _:
            print("choose a valid answer")
            return Library()
          
def login(gmail, password):
    # Regular expression for institutional email:
    # Accepts emails with or without a dot before the @ (e.g., juan.perez@correounivalle.edu.co or juanperez@correounivalle.edu.co)
    model_gmail = r'^[a-zA-Z]+(\.[a-zA-Z]+)?@correounivalle\.edu\.co$'
    # Password must have at least one lowercase, one uppercase, one digit, one special character, and be at least 10 characters long.
    model_password = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&+=]).{10,}$'

    # Checks if both email and password match the required patterns.
    if re.match(model_gmail, gmail) and re.match(model_password, password):
        print("valid login.")
        return True
    else:
        print("invalid login, try again\n")
        return False

def second_login(code):
    print(f"""
    +---------------------------------------------+
    |                                             |
    |    verification code has been sent: {code}  |
    |    enter the generated code.                |
    |                                             |
    +---------------------------------------------+
""")
    verification_code = input("verification code: ")
    # Checks if the entered verification code matches the expected code.
    if verification_code == code:
        print("valid confirmation code")
        return True
    else:
        print("Invalid confirmation code, Try again\n")
        return False

if __name__ == "__main__":
    menu = Library()

    # If the user decides not to start the program, it closes automatically.
    if menu is False:
        print("The univalle library program has been closed.")
        exit() 

    # Main program loop: asks for credentials and OTP until successful login or user exits.
    while(menu):
        print("""     
    +---------------------------------------------------------------------------------------------------------+
    |   Enter your credentials to access the Univalle library system.                                         |
    +---------------------------------------------------------------------------------------------------------+
""")
        email = input("""Enter the institutional email:
                      example: juan.perez@correounivalle.edu.co """)
        password = input("""Enter password:
                         *At least one lowercase.
                         *At least one capital letter.
                         *At least one number. 
                         *At least one special character (@#$%^&+=).
                         """)

        # Calls login function to validate credentials.
        if login(email, password):
            otp = "202459394" # OTP CODE 

            # Calls second_login to validate OTP code.
            if second_login(otp):
                print("""
    +---------------------------------------------------------------------------------------------------------+
    |                         Welcome to the Univalle library system!                                         |
    |                         You have successfully logged in.                                                |       
    +---------------------------------------------------------------------------------------------------------+
                      """)
                break
            else:
                # If OTP fails, show the menu again.
                menu = Library()
                if menu is False:
                    print("The univalle library program has been closed.")
                    exit()
        else:
            # If login fails, show the menu again.
            menu = Library()
            if menu is False:
                print("The univalle library program has been closed.")
                exit()