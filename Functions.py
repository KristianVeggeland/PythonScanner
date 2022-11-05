import random

def confirmList():
    
    confirm = input("Do you want to create list: ")

    if confirm == " ":
        print("try again please")
        confirm = input("Do you want to create list: ")

    elif confirm == "y":
        lengthOfList()
    
    elif confirm == "n":
        print("okay, youy can fuck off then.")

def lengthOfList():
    length = input("Length of list: ")
    integerLength = int(length)
    return integerLength

def inputName():
    name = input("Name: ")
    return name

def createListInFileFormat(listOfId, listOfName):
    length = len(listOfId)
    
    f = open("ListOfnames.txt", "w")

    for x in range(length):
        f.write(str(listOfId[x]) + ", " + str(listOfName[x]) + "\n")



def createList(): 
    print("ok!") 

    length = lengthOfList()

    listOfId = [None] * length
    listOfName = [None] * length

    number = 1

    for i in range(length):
        listOfId[i] = number
        listOfName[i] = inputName()
        number += 1
    
    print("***********************")
    for x in range(length):
        print("Number: " + str(listOfId[x]) + " Name: " + str(listOfName[x]))
    print("***********************")

    createListInFileFormat(listOfId, listOfName)

    





