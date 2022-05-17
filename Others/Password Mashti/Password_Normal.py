import random


def generatePassword():

    #Predefined characters
    default_chars = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!&*-=~`()_+}{@#$%^|.>,<\:;/?'

    # length of the password
    pass_length = int(input("Enter the length of the password: "))

    newPass = ""
    for i in range(pass_length):
        newPass += random.choice(default_chars)

    return newPass


# number of passwords
num_pass = int(input("Enter the number of passwords to be generated: "))

for k in range(num_pass):
    print(generatePassword())
