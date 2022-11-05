from Functions import *

def whatDoYoWant():
    print("What do you whant?" + "\n")
    answer  = getNewAnswer()

    while int(answer) != 5:
        if int(answer) == 1:
            launchNewFile()
            answer  = getNewAnswer()
        elif int(answer) == 2:
            launchNewFile()
            answer  = getNewAnswer()
        
    print("Program terminated, off toy go now!")        
    
def getNewAnswer():
    answer = input("press 1 for creating list and 2 if you want to delete one" + "\n" "and 5 if you wish to terminate ")
    return answer


whatDoYoWant()