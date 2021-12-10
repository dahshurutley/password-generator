# Password Creators/Checker

import string 
import random
import time 
import sys


passContents = []

def userChoice():

    print("Welcome to the Password Generator!...Enter 'N' to close \n")
    userInput = input("Please enter 'A' for Password Generation: ").upper()
    choices = ['A', 'B', 'N']

    def restart(): 

        restarter = input("Enter 'N' To Close Program, Enter 'A' to Genertate a New Password: ").upper()
        
        if restarter == 'A':
            print("Generating New Password...\n")
            time.sleep(1)
            passGenerator()

        elif restarter  == 'N':
            print("Closing Program...")
            time.sleep(1)
            sys.exit()

        else:
            print("Unregestered Response? Restarting Program...")
            time.sleep(1)
            userChoice()
            
    def userEntry():

        if userInput == "A":
            print("Entering Password Generator...")
            time.sleep(2)
            passGenerator()

        elif userInput == "N":
            print("Closing Program...")
            time.sleep(2)
            sys.exit()

        else:
            print("Unregestered Response? Closing Program...")
            time.sleep(1)
            sys.exit()


    if userInput not in choices or len(userInput) > 1:
        print("Unregestered Response? Restarting Program...\n")
        time.sleep(1)
        userChoice()

    def passGenerator():
        lenDetermine = random.randint(1,2)
        gen = 0
        while gen <= lenDetermine:

            gen += 1 
            passContents.append(random.choice(string.ascii_lowercase))
            passContents.append(random.choice(string.ascii_uppercase))
            passContents.append(random.choice(string.digits))
            passContents.append(random.choice(string.punctuation))
        
        print(f"The Generated Password Is: {''.join(passContents)}")
        time.sleep(1)
        passContents.clear()
        restart()
        userChoice()

    userEntry()
    
userChoice()

    



