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
    fileAmount = findFileAmount()
    if fileAmount == 0:
        print("No files found in this directory. " + "\n") 
    elif fileAmount == 1:
        name = findFileName() 
        decisionOnFile(name)
    elif fileAmount > 1:
        Files = getListOfFiles()
        handleListOfFiles(Files)
        

def findFileName():
    files = os.listdir()

    name = " "

    for x in range(len(files)):
        if  ".txt" in str(files[x]):
            name = str(files[x])
    
    return name

    


def findFileAmount():
    listOfFiles = os.listdir()

    counter = 0

    for i in range(len(listOfFiles)):
        if ".txt" in str(listOfFiles[i]):
            print("JEFFF")
            counter = counter + 1
            print(str(counter))


    if counter == 0:
        print("No .txt files are in this directory.")
        return 0

    elif counter == 1:
        return 1

    elif counter > 1:
        return 2


def getListOfFiles():
    fileList = os.listdir()
    counter = 0

    for x in range(len(fileList)):
        if ".txt" in str(fileList[x]):
            counter += 1 
    
    listOfWantedFiles = [None] * counter

    helper = 0

    for x in range(len(fileList)):
        if ".txt" in str(fileList[x]):
            listOfWantedFiles[helper] = str(fileList[x])
            helper += 1
    
    return listOfWantedFiles


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


def deleteAllFiles(filelist):
    list = filelist
    for x in range(len(list)):
        deleteFile(str(list[x]))
    print("All .txt files deleted successfully")

def deleteOnApproval(fileList):
    for x in range(len(fileList)):
        print("File is called: " + str(fileList[x]))
        answer = input("Do you wish to delete this? y for yes and n for no: ")
        if answer != "y" or answer != "n":
            print("Answer " + str(answer) + " is illogical and is not valid" + "\n")
            print("File is called: " + str(fileList[x]))
            answer = input("Do you wish to delete this? y for yes and n for no: ")
        elif answer == "y":
            deleteFile(str(fileList[x]))
        elif answer == "n":
            print("Okay, moving on then")


def handleListOfFiles(fileList):
    print("It seems that this directory contains multiple text files" + "\n")
    answer = input("We can remove all of them at once or if you wish we can show you them one at the time."
                     + "\n" + "0 for delete all and 1 for one at them time or 2 if you wish to cancel: ")
    if answer == "0":
        deleteAllFiles(fileList)
    

    elif int(answer) == 1:
        deleteOnApproval(fileList)
        

    elif int(answer) == 2:
        print("okay my bad")


    else:
        print("Answer given is illogical. ")
        answer = input("We can remove all of them at once or if you wish we can show you them one at the time."
                     + "\n" + "0 for delete all and 1 for one at them time or 2 if you wish to cancel: ")

# ********************************************************************* view all lists functions ****************************************************************

def launchViewLists():
    answer = input("0 for view and for 1 all")

    if(int(answer) == 0):
        viewSingleList()
    elif(int(answer) == 1):
        viewAllLists()
    else:
        answer = input("0 for view and 1 for all")   
     

def viewSingleList():
    fileList = os.listdir()
    
    counter = 0

    for x in range(len(fileList) ):
        if ".txt" in str(fileList[x]):
            counter += 1
    
    if(counter == 0):
        print("No lists found.")
    elif(counter == 1):
        for x in range(counter):
            if ".txt" in str(fileList[x]):
                f = open(fileList[x])
                print(f.read())
           
    else:
        print("There are more than one list found.")
        print("We will therefore print out all the names of the list so that you can chose.")
        for x in range(len(fileList)):
            if ".txt" in str(fileList[x]):
                print( str(fileList[x]) + "\n")

        answer = input("Give your list to us.")

        for x in range(len(fileList)):
            if (str(fileList[x]) == answer):
                f = open(fileList[x])
                print(f.read())
                
        

def viewAllLists(): 
        fileList = os.listdir()
        print("ff")
        counter = 0

        for x in range(len(fileList)):
            if ".txt" in str(fileList[x]):
                counter += 1
        print(str(counter) + "\n")



        if(counter == 0):
            print("No lists found.") 
        else:
            for x in range(len(fileList)):
                if ".txt" in str(fileList[x]):
                    f = open(fileList[x])
                    print(f.read())
                
