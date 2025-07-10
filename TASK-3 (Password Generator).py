import random

def generate_password(length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*"
    password = ""
    for i in range(length):
        password += random.choice(characters)
    return password

if _name_ == "_main_":
    length = int(input("Enter the length of the password: "))
    print("Generated password:", generate_password(length))
