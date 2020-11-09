"""
Braxton Phillips
SDEV 220
Chapter 8 Exercise 8.3
Due Nov 7, 2020
"""

def readPassword(testPhrase): #function carries out password eval
    passLetters = 0
    passDigits = 0

    for values in testPhrase:
        if (values >= 'a' and values <= 'z') or (values >= 'A' and values <= 'Z'):#checks for characters across all captalized and lowercased values
            passLetters += 1
        elif values >= '0' and values <= '9':
            passDigits += 1
            passLetters += 1
    if len(testPhrase) == passLetters and passDigits >= 3 and len(testPhrase) >= 9: #evaluates phrases 
        print("Valid password!")
    else:
        print("Invalid password.")

userPW=input("Enter password for validation. Password must have at least nine characters, three of which must be digits.")
readPassword(userPW) #calls function