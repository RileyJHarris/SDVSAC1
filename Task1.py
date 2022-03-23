print("Textbook Value Calculator")
TotalValue = 0

def getAge():
    age = input("How old is your textbook? (years): ")
    if age.isnumeric() == False:
        print("invalid age input")
        age = getAge()
    return int(age)
        
def getInitValue():
    InitValue = input("How much did you buy your textbook for?: ")
    if InitValue.isnumeric() == False:
        print("invalid Price input")
        InitValue = getInitValue()
    return int(InitValue)

def getInput():
    global TotalValue
    age = getAge()
    InitValue = getInitValue()
    
    curValue = int(InitValue - (InitValue * (0.2 * age)))
    if curValue < 0:
        curValue = 0
    TotalValue += curValue
    print('Your book is valued at ${}'.format(curValue))
    print("Your total book collecction is worth ${}".format(TotalValue))
    repeat = input("would you like to value another book?(y/n): ")
    if repeat == "y":
        print('\n\n')
        getInput()

getInput()