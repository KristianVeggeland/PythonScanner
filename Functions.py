import os

# ******************************************************************* Functions for creating list file ************************************************************************

def launchNewFile():
    confirm = confirmList()

    if confirm > 0:
        print("Okay, off you go!")
    else:
        fileName = createList()
        readList(fileName)


def confirmList():
    
    confirm = input("Do you want to create list: ")

    returner = 0

    if confirm == "y":
        return returner
    
    elif confirm == "n":
        returner  += 1
        return returner

    else:
        print("try again please")
        confirm = input("Do you want to create list: ")


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


# ******************************************************************* Functions for deleting file ************************************************************************


def launchDeleteFile():
    print("So you wan to delete a list?, well here it is. " + "\n")
    fileName = findFile()
    fileName = handleFile(fileName)

    if fileName == "N":
        decisionOnFile(fileName)
    else:
        print("Xlosing shop")


def findFile():
    listOfFiles = os.listdir()

    fileName = " "

    for x in range(len(listOfFiles)):
        if ".txt" in str(listOfFiles[x]):
            fileName = str(listOfFiles[x])
    
    return fileName


def handleFile(fileName):
    if fileName == " ":
        print("No list files found in this directory, of you go")
        fileName = "N"
        return fileName 
    else:
        return fileName


def decisionOnFile(fileName):
    decision = input("Do you want to remove this file: " + str(fileName) + " ")
    if decision == "y":
        deleteFile(fileName)
    else:
        print("Okay, of you go then.")


def deleteFile(fileName):
    if os.path.exists(fileName):
        os.remove(fileName)
        print("File deleted successfully")
    else:
        print("File not found in directory, dont know what else to tell you chief.")  








