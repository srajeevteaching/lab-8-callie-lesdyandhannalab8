#Programmers: Callie Walker, Lesdy Galvez, Hanna Magan
#Date: 11/11/21
#Lab Number: 8
#
#
import random
names_file = open("names.txt", "r")

nameList = []
def readLine(file,list):
    for line in file:
        list.append(line)
        #print(list)


def getName(list):
    name = random.choice(list)
    list.remove(name)
    #print(list)
    return name

def main():
    readLine(names_file, nameList)
    startName = "First name is "
    randomName = random.choice(nameList)
    nameList.remove(randomName)
    print(randomName)
    while len(nameList) > 0:
        userInput = input("Pick another name? ")
        userInput.strip().lower()
        if (userInput == "yes"):
            print(getName(nameList))
            if (len(nameList) == 0):
                print("No more names available")
                break
        elif(userInput == "quit"):
            print("Finished")
            break
    #print(nameList)
main()
names_file.close()
#could creat while loop while length>0 and userInput == yes
