import pandas as pd
import numpy as np
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
#load csv
dat = pd.read_csv('Task2_Shop_Data.csv')
#replace none values with 0
dat.replace('none', 0, inplace = True)
#change rating column data type from string to float
dat = dat.astype({"Rating": 'float64'})
dat.style.hide_index()

#manage input for filter
def getfilCol():
    repeat = True
    filterDict = {"S":"Subject", "T":"Textbook", "R":"Rating", "Q":"Quit"}
    while repeat:
        userInput = input("\n input filter type: ")
        userInput = userInput.capitalize()
        validInputs = ["S" ,"T", "R", "Q"]
        if userInput.isalpha():
            if userInput in validInputs:
                return(filterDict[userInput])
            else:
                print("\nInvalid input, please try again.\ninput must be the corresponding letter for one of below: \nTextbook(T)\nSubject(S)\nRating(R)\nQuit Program(Q)")
        else:
            print("\nInvalid input, please try again.\ninput must be the corresponding letter for one of below: \nTextbook(T)\nSubject(S)\nRating(R)\nQuit Program(Q)")
        
            
        

def filterDataBase():
    while True:

        print("\n\nDatabase Filter\nFilter by\nSubject(S)\nTextbook(T)\nRating(R)\nor quit the program(Q)")
        #get input from user for filter type
        filCol = getfilCol()
        #if user requests to quit, exit program
        if filCol == "Quit":
            print("\nclosing application")
            raise SystemExit(0)
        #sort by rating
        elif filCol == "Rating":
            sortedDat = dat.sort_values('Rating', ascending= False, inplace= False)
            sortedDat.replace(0.0, "none", inplace = True)
        #sort by search term
        else:
            filTerm = input("input {} filter: ".format(filCol))
            sortedDat = dat[pd.Series(dat[filCol]).str.contains(filTerm, case = False)].reset_index()
        print(sortedDat.to_string(index=False))
        continueLoop = input("continue/quit(c/q):")
        if continueLoop == "q":
            break
    
    
#display correct columns after filter

    
filterDataBase()
    
