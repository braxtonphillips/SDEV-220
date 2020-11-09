"""
Braxton Phillips
SDEV 220
Chapter 4 Excercise 4.15
Due Oct 31, 2020
"""

import random

#genertaes random number from 100 to 999
lottery = random.randint(100, 1000) 

# Prompt the user to enter a guess
guess = eval(input("Enter your lottery pick (three digits): "))

# Get digits from lottery
lotteryDigit1 = lottery // 100
lotteryDigit2 = (lottery % 100) // 10
lotteryDigit3 = lottery % 10
# Get digits from guess
guessDigit1 = guess // 100
guessDigit2 = (guess % 100) // 10
guessDigit3 = guess % 10
print("The lottery number is", lottery)

#assigning the lotteryDigits list for earier referencing
lottoNumbers = [lotteryDigit1, lotteryDigit2, lotteryDigit3]
if guess == lottery:
    print("Exact match: you win $15,000")
elif guessDigit1 in lottoNumbers and guessDigit2 in lottoNumbers and guessDigit3 in lottoNumbers:
    print("Match all digits: you win $7,500")
elif guessDigit1 in lottoNumbers or guessDigit2 in lottoNumbers or guessDigit3 in lottoNumbers:
    print("Match one digit: you win $2,000")
else:
    print("Sorry, no match")