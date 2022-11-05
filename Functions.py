import random
import os

def launch():
    confirm = confirmList()

    if confirm > 0:
        print("Okay, off you go!")
    else:
        fileName = createList()
        readList(fileName)


def confirmList():
    
    confirm = input("Do you want to create list: ")

    returner = 0

    if confirm == " ":
        print("try again please")
        confirm = input("Do you want to create list: ")

    elif confirm == "y":
        return returner
    
    elif confirm == "n":
        returner  += 1
        return returner

def lengthOfList():
    length = input("Length of list: ")
    integerLength = int(length)
    return integerLength

def inputName():
    name = input("Name: ")
    return name

def creatFileName():
    fileName = input("File Name: ")
    fileName += ".txt"
    return fileName

def createListInFileFormat(listOfId, listOfName, fileName):
    length = len(listOfId)
    name = fileName
    print("name: " + name)

    f = open(name, "x")

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

    fileName = creatFileName()

    createListInFileFormat( listOfId, listOfName, fileName)

    return fileName


def readList(nameOfFile):
    f = open(nameOfFile, "r")
    print(f.read())

launch()
    


    





