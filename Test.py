from Functions import *


# ********************************************************************** Testing functions with small program ***************************************************************
def whatDoYoWant():
    print("What do you want?" + "\n")
    answer  = getNewAnswer()

    while int(answer) != 5:
        if int(answer) == 1:
            launchNewFile()
            answer  = getNewAnswer()
        elif int(answer) == 2:
            launchDeleteFile()
            answer  = getNewAnswer()
        
        
    print("Program terminated, off you go now!") 


# **************************************************************** Supporting functions for testing program *********************************************************************    
def getNewAnswer():
    answer = input("press 1 for creating list and 2 if you want to delete one" + "\n" "and 5 if you wish to terminate ")
    check = checkIfAnswerIsLegal(answer)
    print(check)
    holder = 0
    while holder == 0:
        if check == 0:
            answer = input("press 1 for creating list and 2 if you want to delete one" + "\n" "and 5 if you wish to terminate ")
            check = checkIfAnswerIsLegal(answer)
        elif check == 1:
            holder = 1
        

    return answer


def checkIfAnswerIsLegal(answer):
    oba = 0
    if answer.isdigit(): 
        oba = 1
        return oba
    else:
        oba = 0
        return oba
    


whatDoYoWant()