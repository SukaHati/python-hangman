#This is hangman game.

import random #Used for number generation
from pathlib import Path #Used to check file existence

file = Path("wordlist.txt")
if file.is_file():
    file = open('wordlist.txt', 'r')
    contents = file.read()
    guessWord = contents.splitlines() #Try remove newline from the list
    file.close()
else:
    guessWord = ["balloon", "apple", "pineapple", "hexagon", "delicious", "durian"]

#This is for allowing only 1 character to be input and check the previously used character
def inputChar(message, alphabetList):
    getAlphaList = 'abcdefghijklmnopqrstuvwxyz' #this is collection of alphabet use for this game
    while True:
        userInput = input(message)
        if len(userInput) != 1 or userInput not in getAlphaList:
            print("Not alphabet!")
        elif userInput in alphabetList: #Check if the alphabet was input previously
            print("This alphabet was used!")
        else:
            return userInput
            break

#Display the guessing word
def displayWord(alphabetList):
    showWord = ""
    numList = 0
    length = len(alphabetList)
    for i in range(length):
        showWord = showWord + " " + alphabetList[numList] + " "
        numList += 1
    print(showWord)

#Asking for retry
def userRetry():
    acceptableChar = 'yYnN'
    while True:
        userInput = input("Retry (Y/N): ")
        if len(userInput) != 1 or userInput not in acceptableChar:
            print("Y or N only")
        elif userInput == 'Y' or userInput == 'y':
            return True
        else:
            return False

# Main program starts!
while True:
    a = random.choice(guessWord) #pick a word from guessWord
    b = []
    wordUsed = []
    num_list = 1
    num_lives = 5
    for t in a:
        b.insert(num_list,'_')
    d = ' '.join(b) + ' '
    print(d) #or just do this
    while True:
        arr_pos = 0
        user_input = inputChar("Input char: ", wordUsed)
        found_alpha = 0
        for t in a: #looping to search characters in the game
            if user_input == a[arr_pos]:
                del b[arr_pos] #delete current element in list
                b.insert(arr_pos,user_input)
                found_alpha += 1
            arr_pos += 1
        wordUsed.append(user_input) #Adding character to used characters
        displayWord(b)
        if found_alpha == 0:
            num_lives -= 1
            print("Alphabet not found")
        print("Lives: " + str(num_lives)) #str() to convert variable type to string
        if num_lives == 0: #trigger game over screen
            displayWord("< KABOOM >")
            print(f'The answer is: {a}')
            displayWord("GAME OVER")
            break
        arr_pos = 0
        if '_' not in b:
            displayWord("YOU ARE A WINNER!") #Generic winning screen
            break
    retry_cond = userRetry()
    if retry_cond == False:
        print("Thank you for playing")
        break
