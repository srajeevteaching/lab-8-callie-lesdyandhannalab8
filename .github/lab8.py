import random
names_file = open("names.txt", "r")

nameList = []
def readLine(file,list):
    for line in file:
        print(line)
        list.append(line)


def getName(list):
    name = random.choice(list)
    list.remove(name)
    return name

def main():
    readLine(names_file, nameList)
    getName(nameList)
    for i in nameList:
        getName(nameList)
        userInput = input("More names? ")
        userInput.strip().lower()
        print(getName(nameList))
        if (userInput != "quit"):
            getName(nameList)
        if(len(nameList) == 0):
            print("No more names available")
    print(nameList)
main()
names_file.close()