import random

def confirmList():
    
    confirm = input("Do you want to create list: ")

    if confirm == " ":
        print("try again please")
        confirm = input("Do you want to create list: ")

    elif confirm == "y":
        createList()
    
    elif confirm == "n":
        print("okay, youy can fuck off then.")

    
    
def createList(): 
    print("ok!")  


confirmList()