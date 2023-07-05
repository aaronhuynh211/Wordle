import random
from colorama import init, Back, Fore

def color(currWord, word):
    colWord = ""
    for i in range(len(currWord)):
        colWord += Back.RESET
        if currWord[i] == word[i]:
            colWord += Back.GREEN + word[i]
        elif currWord[i] in word:
            colWord += Back.YELLOW + currWord[i]
        else:
            colWord += Back.RESET + currWord[i]
    return colWord

def updateK(corr,half,wrong):
    k = ["qwertyuiop","asdfghjkl","zxcvbnm"]
    k2 = ["","",""]
    for i in range(3):
        for letter in k[i]:
            k2[i] += Back.RESET
            if letter in corr:
                k2[i] += Back.GREEN + letter + Back.RESET + "  "
            elif letter in half: 
                k2[i] += Back.YELLOW + letter + Back.RESET + "  "
            elif letter in wrong:
                k2[i] += Back.RED + letter + Back.RESET + "  "
            else: 
                k2[i] += letter + Back.RESET + "  "
            #k2[i] += Back.RESET
    return k2
with open("words_5.txt") as f:
    words = [line.strip() for line in f]
    
word = random.choice(words)
words = set(words)
keeb = "qwertyuiopasdfghjklzxcvbnm"
corr = []
half = []
wrong = []
full = []
tries = 0
guess = []
status = True

while status and tries < 6:
    print("------------------------------")
    print("|\t    Wordle!\t     |")
    print("|                            |")
    for i in range(5):
        try:
            print("|            " + full[i] + (16-len(guess[i]))*" " +"|")
        except:
            print("|                            |")
    print("|                            |")
    print("|                            |")
    k = updateK(corr,half,wrong)
    for i in range(3):
        if i == 0:
            print("|"+ k[i][:len(k[i])-2] + "|")
        if i == 1:
            print("| "+ k[i] + "|")
        if i == 2:
            print("|    "+ k[i] + "   |")
    print("------------------------------")
    colWord = ""
    if tries < 6:
        currWord = input("Guess a word: ")
        if len(currWord) > 5:
            print("Invalid input: too long.")
        elif currWord not in words:
            print("Invalid input: not a word.")
        else:
            for i in range(len(currWord)):
                if currWord[i] == word[i]:
                    colWord += Back.GREEN + word[i] + Back.RESET
                    corr.append(word[i])
                elif currWord[i] in word:
                    colWord += Back.YELLOW + currWord[i] + Back.RESET
                    half.append(currWord[i])
                else:
                    colWord += Back.RESET + currWord[i] + Back.RESET
                    wrong.append(currWord[i])
            full.append(colWord)
            guess.append(currWord)
            tries += 1
    if currWord == word:
        status = False


print()
print("------------------------------")
print("|\t    Wordle!\t     |")
print("|                            |")
for i in range(6):
    try:
        print("|            " + full[i] + (16-len(guess[i]))*" " +"|")
    except:
        print("|                            |")
print("|                            |")
k = updateK(corr,half,wrong)
for i in range(3):
    if i == 0:
        print("|"+ k[i][:len(k[i])-2] + "|")
    if i == 1:
        print("| "+ k[i] + "|")
    if i == 2:
        print("|    "+ k[i] + "   |")
print("------------------------------")
colWord = ""
if status:
    print("Sorry! The word was: " + word)
else:

    print("You got " + word + " in " + str(tries) + " tries!")

    
