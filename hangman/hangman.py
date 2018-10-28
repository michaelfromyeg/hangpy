
import time
import random
import sys

category = 0
user_playing = True
hangman = (

"""
   _________
    |/        
    |              
    |                
    |                 
    |               
    |                   
    |___                 
    """,

"""
   _________
    |/   |      
    |              
    |                
    |                 
    |               
    |                   
    |___                 
    H""",

"""
   _________       
    |/   |              
    |   (_)
    |                         
    |                       
    |                         
    |                          
    |___                       
    HA""",

"""
   ________               
    |/   |                   
    |   (_)                  
    |    |                     
    |    |                    
    |                           
    |                            
    |___                    
    HAN""",


"""
   _________             
    |/   |               
    |   (_)                   
    |   /|                     
    |    |                    
    |                        
    |                          
    |___                          
    HANG""",


"""
   _________              
    |/   |                     
    |   (_)                     
    |   /|\                    
    |    |                       
    |                             
    |                            
    |___                          
    HANGM""",



"""
   ________                   
    |/   |                         
    |   (_)                      
    |   /|\                             
    |    |                          
    |   /                            
    |                                  
    |___                              
    HANGMA""",


"""
   ________
    |/   |     
    |   (_)    
    |   /|\           
    |    |        
    |   / \        
    |               
    |___           
    HANGMAN""")

def game_start():
 
    name = welcome()
    category, categories = select_category()

    print("Hello " + name + ". Welcome to HangPy! You have selected you would like to play '" + categories[category] + "'. Let's get to the action!") 

    choice = select_word(category)
    print("Selecting your word...")
    time.sleep(3)
    print("Okay! Your word has been selected.")

    temp_word, spaces = play_game(choice)

    print("Time to guess!")
    print(hangman[0])
    guess_word(choice,temp_word,spaces)

def welcome():
    print ("""
          _    _                   _____       
         | |  | |                 |  __ \      
         | |__| | __ _ _ __   __ _| |__) |   _ 
         |  __  |/ _` | '_ \ / _` |  ___/ | | |
         | |  | | (_| | | | | (_| | |   | |_| |
         |_|  |_|\__,_|_| |_|\__, |_|    \__, |
                              __/ |       __/ |
                             |___/       |___/ 
        """)
    name = input("Please enter your username: ").strip()
    nameCheck = 'N'
    while (nameCheck == 'N'):
        print("Your username is " + name + ".")
        nameCheck = input("Is this correct? (Y/N) ").strip()
        if (nameCheck.upper() == 'N'):
            print("Whoops! Let's try that one more time")
            name = input("Please enter your username: ")
    return name

def select_category():
    categories = ["Animals","Celebrities","Brands"]
    category = int(input("Select which category you would like to play: 1. Animals 2. Celebrities 3. Brands. (#) ")) - 1
    categoryCheck = 'N'
    while (categoryCheck == 'N'):
        print("Your category is " + categories[category] + ".")
        categoryCheck = input("Is this correct? (Y/N) ").strip()
        if (categoryCheck.upper() == 'N'):
            print("Whoops! Let's try that one more time")
            category = int(input("Select which category you would like to play: 1. Animals 2. Celebrities 3. Brands. (#) "))
    return category, categories

def select_word(category):
    words = [["fish","lion","fawn","otter","yak","dog","sheep","canary","ground hog","leopard"],
             ["Nick Carter","Christina Aguilera","Naomi Watts","George Shelley","Harrison Ford","Jeff Dunham","Samuel L. Jackson","Dwayne Wade","Bruce Willis","Miranda Kerr"],
             ["Walgreens","Johnson's","Humana Inc","ExxonMobil","American Airlines","Kraft","Pepsi","Coke","Dell","KFC"]]
    rand = random.randint(0, 9)
    return words[category][rand].lower()

def play_game(word):
    words = 1
    temp_word = list("")
    for i in range(0,len(word)):
        if word[i].isalpha():
            temp_word += "_"
        else:
            temp_word += " "
            words += 1
    print(" ".join(str(x) for x in temp_word))
    print("")
    if words == 1:
        print("The word has " + str(len(word)) + " characters.")
    if words > 1:
        print("There is more than one word. The phrase is " + str(words) + " words long. In total, it is " + str(len(word)) + " characters.")
    return temp_word, (words - 1)

def guess_word(word,temp,spaces):

    found_word = False
    good_guess = False
    wrong_answers = 0
    characters_remaining = len(word) - spaces

    while (not found_word):
        while(not good_guess):
            guess = input("Guess a letter:").lower()
            if (len(guess) != 1):
                print("Input one letter! Let's try that again.")
                continue
            else:
                break
        found_char = False
        for i in range(0,len(word)):
            if word[i] == guess:
                temp[i] = guess
                characters_remaining -= 1
                found_char = True
        print(" ".join(str(x) for x in temp))
        print("")

        if (characters_remaining <= 0):
            print("You won!")
            end_game()
            return ""

        if (not found_char):
            wrong_answers += 1
            print(hangman[wrong_answers])
            if (wrong_answers >= len(hangman) - 1):
                print("You lost!")
                end_game()
                return ""
                

def end_game():
    print("Thank you for playing!")
    play_again = input("Would you like to play again? (Y/N) ").strip()
    if (play_again.upper() == 'N'):
        print("Thank you for playing. Goodbye")
        user_playing = False
        time.sleep(5)
        sys.exit(0)
    if (play_again.upper() == 'Y'):
        print("Alright, well let's get started then.")
        user_playing = True
        return ""

while user_playing:
    game_start()