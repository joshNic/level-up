"""The following is an example of modeling the uber signup
form using object oriented concepts
"""
import re

UBER_USERS = []

class SignUp(object):
    """
    This class registers a new uber driver to our UBER_USERS list
    """
    def __init__(self, firstName, lastName, phoneNumber, email, password):
        self.firstName = firstName
        self.lastName = lastName
        self.phoneNumber = phoneNumber
        self.email = email
        self.password = password

    def register(self):

        # add new driver to the list if all criterion is met
        UBER_USERS.append({
            "firstName": self.firstName, "lastName": self.lastName,
            "phoneNumber": self.phoneNumber, "email": self.email,
            "password": self.password})

        print("Rider Successfully registered")


class Authentication(SignUp):
    """This class checks and verifies the user data supplied before
    the user is registered it takes SignUp as parent class
    """

    def __init__(self, firstName, lastName,
                 phoneNumber, email, password):
        SignUp.__init__(self, firstName, lastName,
                        phoneNumber, email, password)
        self.firstName = Authentication.check_name(firstName)
        self.lastName = Authentication.check_name(lastName)
        self.phoneNumber = Authentication.check_phone_number(phoneNumber)
        self.email = Authentication.check_email_contains(email)
        self.password = Authentication.check_password(password)

    # Method to verify user supplied data
    def verify(self):
        # check if all fields have been checked
        if self.firstName and self.lastName and self.phoneNumber and self.email and self.password:

            # check if the phone number or email supplied matches any data already in the list
            user = [rider for rider in UBER_USERS if rider.get(
                "email") == self.email or rider.get("phoneNumber") == self.phoneNumber]
            if user:
                print("Sorry rider already exixts")

            # if there are no matches found in the list then that is a new user and we add to the list
            else:
                self.register()
        else:
            print("Rider not registered please check above details and try agin")

    @staticmethod
    # Method that checks the data passed to the name field
    def check_name(name):

            # Character set and passed as argument in compile method
        regex = re.compile(r'[@_!#$%^&*()123456789<>?/\|}{~:]')
        if len(name) == 0:
            print("Please First Name and Last Name is a required field")

        # Use the search method to check if supplied name contains any special characters
        elif (regex.search(name) != None):
            print(
                "First Name and Last Name can not contain any special characters or numbers")

        # if all criterion is met return name object
        else:
            print("name all good")
            return name

    @staticmethod
    # Method that checks email address supplied by the user
    def check_email_contains(email):
        if len(email) < 6:
            print("email is too short try agin")
        elif "@" not in email:
            print("Email must contain @ character try again")
        elif "." not in email:
            print("Email must conatin . character try again")
        elif email.startswith("@") or email.startswith("."):
            print("Email can not start with @ or . character try agin")
        elif "@." or ".@" in email:
            print("Email can not conatin @ and . next to each other please try agin")
        else:
            print("All good")
            return email

    @staticmethod
    # Method to check supplied password
    def check_password(password):
        if len(password) < 6:
            print("password can not be less than 6 characters try again.")
        elif len(password) == 0:
            print("Password field can not be empty")
        else:
            print("Password all good")
            return password

    @staticmethod
    # Method to check the supplied phone number
    def check_phone_number(phoneNumber):
        if not phoneNumber.isdigit():
            print("Phone number can only contain numbers please try again.")
        else:
            if len(phoneNumber) < 10:
                print("phoneNumber can not be less than 10 digits try again.")
            elif len(phoneNumber) == 0:
                print("phoneNumber field can not be empty")
            else:
                print("phoneNumber all good")
                return phoneNumber

if __name__ == '__main__':
    
    # Get user input
    firstName = input("Enter first name: ")
    lastName = input("Enter last name: ")
    phoneNumber = input("Enter phone number: ")
    email = input("Enter email: ")
    password = input("Enter password: ")

    # Create Authentication object
    test = Authentication(firstName, lastName, phoneNumber, email, password)
    # call the verify method on the data supplied
    test.verify()
