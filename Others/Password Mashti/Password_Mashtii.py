"""Generate a password considering the following conditions:
    - At least 1 uppercase letter
    - At least 2 specific characters
    - Minimum length of 8
    - At least 3 unic numbers
"""


import random


# Define characters
up_letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
low_letter = "abcdefghijklmnopqrstuvwxyz"
nums = "1234567890"
specific_chars = "!&*-=~`()_+}{@#$%^|.>,<\:;/?"


def getLength():
    while(True):
        pass_length = int(input("Enter the length of the password: "))
        if(pass_length >= 8):
            break

        else:
            print("Invalid length for the password.\nTry again.")
            continue
    return pass_length


def generatePassword_2():
    newPass = ""
    length = getLength()

    # Numbers
    randNum = random.randint(3, length - 3)
    for k in range(randNum):
        gen_num = random.choice(nums)
        try:
            if (gen_num not in newPass):
                newPass += gen_num
        except:
            continue

    # Uppercase letters
    randNum = random.randint(1, length - len(newPass))
    for j in range(randNum):
        newPass += random.choice(up_letter)

    # Specific Characters
    randNum = random.randint(2, length - len(newPass))
    for i in range(randNum):
        newPass += random.choice(specific_chars)

    # lowercase letters
    for m in range(length - len(newPass)):
        newPass += random.choice(low_letter)

    return newPass


myVar = generatePassword_2()

# Randomly sorting the generated password.
Password = ''.join(random.sample(myVar, len(myVar)))
print(Password)
