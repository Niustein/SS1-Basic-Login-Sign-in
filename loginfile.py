# Written by: Samuel Niu
# Date: September 22-23rd 2019
# A simple text-based implementation for login/registration
# Goals: back to basics. Input/Output. Read/Write.
# Additional Learning: Bcrypt/Encrpytion

import bcrypt


def gotoLogin(loginUsername, loginPassword):

    with open("accounts.txt", "r+") as compareCredentials:

        lineByLine = compareCredentials.readlines()
        for line in lineByLine:
            lineBreak = line.split(",")
            userCheck = lineBreak[0]
            newLineStrip = lineBreak[1][:-1] #remove newline character so checkpw functions correctly
            passCheck = newLineStrip

            if userCheck == loginUsername:
                    
                if(bcrypt.checkpw(loginPassword.encode('utf-8'),passCheck.encode('utf-8'))):
                    return True
            
    return False

def createAccount(desiredUsername, desiredPassword):
    
    with open("accounts.txt", "r+") as compareCredentials:
        
        lineByLine = compareCredentials.readlines()
        for line in lineByLine:
            lineBreak = line.split(",")
            userCheck = lineBreak[0]
            print(userCheck)
            if userCheck == desiredUsername:
                return False

        appendCredentials = open("accounts.txt", "a")
        hashed = bcrypt.hashpw(desiredPassword.encode('utf-8'), bcrypt.gensalt())

        userInfo = desiredUsername + ',' + hashed.decode('utf-8')

        appendCredentials.write(userInfo + "\n")

    return True

def main():
    print("Welcome to this basic account creation/login simulation\n")
    userChoice = 0

    createFileIfMissing = open("accounts.txt", "a+")
    createFileIfMissing.close

    while int(userChoice) != -1:
        userChoice = input("Type 1 to create an account, 2 to login to an account or -1 to exit\n")

        if int(userChoice) == -1:
            exit(0)

        if int(userChoice) == 1:

            desiredUsername = ""

            while desiredUsername.isalnum() == False:
                desiredUsername = input("Please Enter a Username (alphanumeric only)\n")

            desiredPassword = input("Please enter your desired password\n")

            if createAccount(desiredUsername, desiredPassword):
                print("Account successfully created!")
            else:
                print("Account could not be created, please try again")

        elif int(userChoice) == 2:

            loginUsername = input("Please enter your username\n")
            loginPassword = input("Please enter your password\n")
            if gotoLogin(loginUsername, loginPassword):
                print("Thank you for signing in: " + loginUsername)
                exit(0)
            else:
                print("Invalid login credentials, please try again")
                
            
            



if __name__ == "__main__":
    main()
