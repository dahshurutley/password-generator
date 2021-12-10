import random
import string
import time
import sys 


passContents = []

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

def restart():

    a = input("Do you want to generate another password Y/N?: ").upper()

    if a == "Y":
        passGenerator() 

    if a == "N":
        print("Closing")
        time.sleep(1)
        sys.exit()

passGenerator()

    


