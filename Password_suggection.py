import string
import random

def password_check(password):
    #Store Issue in this list
    issue = []

    if (len(password)<8):
        issue.append("Password Length less then 8")
    if not ((any(i.islower() for i in password))):
        issue.append("No lowercase found")
    if not ((any(i.isupper() for i in password))):
        issue.append("No upperercase found")
    if not ((any(i.isdigit() for i in password))):
        issue.append("No Digit found")
    if not (any(i in string.punctuation for i in password)):
        issue.append("No special charator found")
    return issue

def generate_password():
    data = "abcdefghijklmnopqrstuvwxyz1234567890~!@#$%^&*"

    return "".join(random.choice(data) for i in range(0,8))

def main():
    password = input("Enter Strong Password:")
    issue=password_check(password)

    if not issue:
        print("Strong passeord great Job!")
    else:
        for i in issue:
            print(f"Should Contain:{i}")
        print(f"Week Password Entered, Suggection password is:{generate_password()}")

main()