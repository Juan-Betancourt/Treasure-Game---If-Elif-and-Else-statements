print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
from cProfile import run


print("\n\tWelcome to Treasure Island.")
print("\n\tYour mission is to find the treasure. There may be clues throughout the adventure.\n \n\tHINT: Gather everything you find along the way, it may be helpful.\n") 
print("\tAlong your adventure, you have the opportunity to utilize powerful magic throughout your experience.\n")
print("\tYou only have 3 lives throughout your adventure\n\n")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
#---Player Table---
player_life_count = True
player_life_count = 3
magic_spell = 2
while player_life_count > 0:

#---LEVEL 1---
    stage1 = (input("\n\tYou come up to a path that splits left or right; do you go Left or Right?\n\n")).lower()
    if stage1 == "right":
        right_path1 = input("\n\tYou come to a house; however, you see a castle in the distance. Do you dare to go the distance or select the place on the right? Type House or Distance\n\n").lower()
        
#---HOUSE---
        if right_path1 == "house":
            player_life_count -= 1
            print("\n\tUnfortunately, there is an empty chest in the house, and the ghost consumes your soul\n \n\tYou're Dead!!!\n")
            print(f"\n\tYou currenty have {player_life_count} life remaining.\n\n")
            if player_life_count >= 1:
                try_again = input("\n\tDo you want to try again? Yes or No\n\n").lower()
                if try_again == "no":
                    break
            if player_life_count == 0:
                print("\n\tThank you for playing; reset the game if you want to start the adventure again.\n")
                try_again = input("\n\tDo you want to try again? Yes or No\n\n").lower()
                if try_again == "yes":
                    player_life_count = 3

#---CASTLE---
        if right_path1 == "distance":
            castle1 = input("\n\tAs you walk up to a gate, you see a code that requires a four-digit pin? Will you attempt to open it or use your magic ability? Type Attempt or Magic\n\n").lower()

#---Magic Ability---
            if castle1 == "magic":
                magic_spell -= 1
                if magic_spell == -1:
                    print("\n\tYou ran out of magic spells\n")
                if magic_spell <= 1:
                    print(f"\n\tYou currently have {magic_spell} spells left use it wisely.\n\n \n\tYou have successfully opened the gates, and you feel the hollowing wind pass you as you walk through the gates. The following numbers appear before you, 7684. It's essential to keep the first number in mind for the chest found reflecting the moon\n")
                    level_one = input("\n\tDo you go towards the pier or woods? Type pier or woods\n\n").lower()
#---Level One - Pier Magic---
                    if level_one == "pier":
                        pier = input("\n\tThere is a dock near by, do you swim or utilize your magic ability? Type Swim or Magic Wand\n\n").lower()
                        if pier == "swim":
                            print("\n\tAs you attempt to swim across a shark approaches you and attacks leaving you to bleed out and\n \n\tYou're Dead!!!\n\n")
                            player_life_count -= 1
                            if player_life_count == 0:
                                print("\n\tThank you for playing; If you want to start the adventure again reset the game.\n\n")
                            elif print(f"\n\tYou currenty have {player_life_count} life remaining.\n\n"):
                                if player_life_count >= 1:
                                    try_again = input("\n\tDo you want to try again? Yes or No\n").lower()
                                if player_life_count == 0:
                                    print("\n\tThank you for playing; reset the game if you want to start the adventure again.")
                                    try_again = input("\n\tDo you want to try again? Yes or No\n").lower()
                                    if try_again == "yes":
                                        player_life_count = 3

                        if pier == "magic wand":
                            print("\n\tYou use your magic wand and glide over the water leading to safe passage.\n\n")
                            pier_response = input("There is a something in the distance, do you approach it? Yes or No\n\n").lower()
                            if pier_response == "yes":
                                print("\n\tAs you get closer, there is an alter that contains a scribe. There are several numbers but what is essential is a number that stands out 8. Eight is the third number in the set; continue your journey.\n\n")
                            if pier_response == "no":
                                print("\n\tYou wait.... And, an alligator steps inland and snaps its jaw around your leg dragging you in.\n \n\tYou're Dead!!!\n\n")
                                print(f"\n\tYou currenty have {player_life_count} life remaining.\n")
                                if player_life_count >= 1:
                                    try_again = input("\n\tDo you want to try again? Yes or No\n\n").lower()
                                if player_life_count == 0:
                                    print("\n\tThank you for playing; reset the game if you want to start the adventure again.")
                                    try_again = input("\n\tDo you want to try again? Yes or No\n\n").lower()
                                    if try_again == "yes":
                                        player_life_count = 3

#---Level One - Magic Woods---          
                    if level_one == "woods":
                        woods = input("\n\tThere is a carving on one of the wood trees; will you have a look and read the numbers? Yes or No\n\n").lower()
                        if woods == "yes":
                            print("\n\tThe following number is vital to the chest found reflecting the moon. The second number is 6. Continue your journey.\n\n")
                        if woods == "no":
                            print("\n\tYou lose the opportunity to a vital piece of the treasure.\n\n")
                            player_life_count -= 1
                            if player_life_count == 0:
                                print("\n\tThank you for playing; If you want to start the adventure again reset the game.\n")
                            elif print(f"\n\tYou currenty have {player_life_count} life remaining.\n"):
                                if player_life_count >= 1:
                                    try_again = input("\n\tDo you want to try again? Yes or No\n").lower()
                                elif print("\n\tYou attempt the code; however, the numbers are incorrect and the hollowing wind picks you up and sends you to your death.\n"):
                                    player_life_count -= 1
                                    if player_life_count == 0:
                                        print("\n\tThank you for playing; If you want to start the adventure again reset the game.\n")
                                    else:
                                        print(f"\n\tYou currenty have {player_life_count} life remaining.\n")
                                        if player_life_count >= 1:
                                            try_again = input("\n\tDo you want to try again? Yes or No\n").lower()
                                        if player_life_count == 0:
                                            print("\n\tThank you for playing; reset the game if you want to start the adventure again.\n\n")
                                            try_again = input("\n\tDo you want to try again? Yes or No\n").lower()
                                            if try_again == "yes":
                                                player_life_count = 3
                        
                
#---CASTLE ATTEMPT---
            if castle1 == "attempt":
                castle_key1 = input("\n\tPlease insert the four digit pin?\n \n\tHint: The first number is the most common outcome number on a dice, || followed by one down from the first number to find the second number || then, two up from the second number to find the third || divided by 2 on the third number.\n\n")
                castle_key_conv = int(castle_key1)
                if castle_key_conv == 7684:
                    print("\n\tYou have opened the gates and you feel the hollowing wind pass you as you walk through the gates.The following numbers appear before you, 7684. It's essential to keep the first number in mind for the chest found reflecting the moon\n\n")
                    level_one = input("\n\tDo you go towards the pier or woods? Type pier or woods\n\n").lower()
                elif print("\n\tYou have entered the incorrect four-digit pin?\n\n"):
                    player_life_count -= 1
                    if player_life_count == 0:
                        print("\n\tThank you for playing; If you want to start the adventure again reset the game.\n\n")
                    elif print(f"\n\tYou currenty have {player_life_count} life remaining.\n"):
                        if player_life_count >= 1:
                            try_again = input("\n\tDo you want to try again? Yes or No\n").lower()
                        if player_life_count == 0:
                            print("\n\tThank you for playing; reset the game if you want to start the adventure again.\n")
                            try_again = input("\n\tDo you want to try again? Yes or No\n").lower()
                            if try_again == "yes":
                                player_life_count = 3
    
#---Level One - Pier---
                if level_one == "pier":
                    pier = input("\n\tThere is a dock near by, do you swim or utilize your magic ability? Type Swim or Magic Wand\n\n").lower()
                    if pier == "swim":
                        print("\n\tAs you attempt to swim across a shark approaches you and attacks leaving you to bleed out and\n \n\tYou're Dead!!!\n\n")
                        player_life_count -= 1
                        if player_life_count == 0:
                            print("\n\tThank you for playing; If you want to start the adventure again reset the game.\n\n")
                        elif print(f"\n\tYou currenty have {player_life_count} life remaining.\n\n"):
                            if player_life_count >= 1:
                                try_again = input("\n\tDo you want to try again? Yes or No\n").lower()
                            if player_life_count == 0:
                                print("\n\tThank you for playing; reset the game if you want to start the adventure again.")
                                try_again = input("\n\tDo you want to try again? Yes or No\n").lower()
                                if try_again == "yes":
                                    player_life_count = 3

                    if pier == "magic wand":
                        print("\n\tYou use your magic wand and glide over the water leading to safe passage.\n\n")
                        pier_response = input("There is a something in the distance, do you approach it? Yes or No\n\n").lower()
                        if pier_response == "yes":
                            print("\n\tAs you get closer, there is an alter that contains a scribe. There are several numbers but what is essential is a number that stands out 8. Eight is the third number in the set; continue your journey.\n\n")
                        if pier_response == "no":
                            print("\n\tYou wait.... And, an alligator steps inland and snaps its jaw around your leg dragging you in.\n \n\tYou're Dead!!!\n\n")
                            print(f"\n\tYou currenty have {player_life_count} life remaining.\n")
                            if player_life_count >= 1:
                                try_again = input("\n\tDo you want to try again? Yes or No\n\n").lower()
                            if player_life_count == 0:
                                print("\n\tThank you for playing; reset the game if you want to start the adventure again.")
                                try_again = input("\n\tDo you want to try again? Yes or No\n\n").lower()
                                if try_again == "yes":
                                    player_life_count = 3

#---Level One - Woods---          
                if level_one == "woods":
                    woods = input("\n\tThere is a carving on one of the wood trees; will you have a look and read the numbers? Yes or No\n\n").lower()
                    if woods == "yes":
                        print("\n\tThe following number is vital to the chest found reflecting the moon. The second number is 6. Continue your journey.\n\n")
                    if woods == "no":
                        print("\n\tYou lose the opportunity to a vital piece of the treasure.\n\n")
                        player_life_count -= 1
                        if player_life_count == 0:
                            print("\n\tThank you for playing; If you want to start the adventure again reset the game.\n")
                        elif print(f"\n\tYou currenty have {player_life_count} life remaining.\n"):
                            if player_life_count >= 1:
                                try_again = input("\n\tDo you want to try again? Yes or No\n").lower()
                            elif print("\n\tYou attempt the code; however, the numbers are incorrect and the hollowing wind picks you up and sends you to your death.\n"):
                                player_life_count -= 1
                                if player_life_count == 0:
                                    print("\n\tThank you for playing; If you want to start the adventure again reset the game.\n")
                                else:
                                    print(f"\n\tYou currenty have {player_life_count} life remaining.\n")
                                    if player_life_count >= 1:
                                        try_again = input("\n\tDo you want to try again? Yes or No\n").lower()
                                    if player_life_count == 0:
                                        print("\n\tThank you for playing; reset the game if you want to start the adventure again.\n\n")
                                        try_again = input("\n\tDo you want to try again? Yes or No\n").lower()
                                        if try_again == "yes":
                                            player_life_count = 3
                                        
      
#---LEVEL 1---
    elif stage1 == "left":
        crossroads = input("\n\tAfter walking some distance, you run into a crossroad with a park on the right and the moon shining light to an object on the left.\n \n\tWill you go towards the light or park? Type Light or Park\n").lower()
        
#---Level 1 Park---
        if crossroads == "park":
            park_response = input("\n\tYou arrive at the park where there are objects all around you\n \n\tDo you start counting these objects and move deeper into the park? Yes or No\n\n").lower()
            if park_response == "no":
                print("\n\t Thank you for playing\n")
            elif park_response == "yes":
                playground = ['horse', 'camel', 'eagle', 'mouse', 'tiger']
                insects = ['larva','flies','midge','aphid','ants']
                grounds = input("\n\tDo you want view what toys are on the playground? Yes or No\n").lower()
                if grounds == "yes":
                    print(playground,insects)
                hint = input("\n\tDo you need a hint?\n").lower()
                if grounds == "no":
                    print("\n\tYou waited to long and ghost appear to devour you\n")
                    player_life_count -= 1
                    if player_life_count == 0:
                        print("\n\tThank you for playing; If you want to start the adventure again reset the game.\n")
                    else:
                        print(f"\n\tYou currenty have {player_life_count} life remaining.\n")
                        if player_life_count >= 1:
                            try_again = input("\n\tDo you want to try again? Yes or No\n").lower()
                        if player_life_count == 0:
                            print("\n\tThank you for playing; reset the game if you want to start the adventure again.\n\n")
                            try_again = input("\n\tDo you want to try again? Yes or No\n").lower()
                            if try_again == "yes":
                                player_life_count = 3
                if hint == "yes":
                    print("\n\tIn each set focus on the number that repeats itself\n")
                    hint2 = input("\n\tStill need help? It will cost you a life\n").lower()
                    if hint2 =="yes":
                        play_count = len(playground)
                        insect_count = len(insects)
                        print (f"\n\tThink of the total number in each word or set {play_count}, {insect_count}\n \n\tRemember that number as it's the last one of all.\n")
                        player_life_count -= 1
                if hint == "no":
                    answer = input("\n\tWhat is the number?\n")
                    answer_conver = int(answer)
                    if answer_conver == 5:
                        print(f"\n\tYou got the right number {answer}\n \n\tRemember that number as it's the last one of all.\n")
                    else:
                        print("\n\tTry again\n")
                        player_life_count -= 1
                        if player_life_count == 0:
                            print("\n\tThank you for playing; If you want to start the adventure again reset the game.\n")
                        else:
                            print(f"\n\tYou currenty have {player_life_count} life remaining.\n")
                            if player_life_count >= 1:
                                try_again = input("\n\tDo you want to try again? Yes or No\n").lower()
                            if player_life_count == 0:
                                print("\n\tThank you for playing; reset the game if you want to start the adventure again.\n\n")
                                try_again = input("\n\tDo you want to try again? Yes or No\n").lower()
                                if try_again == "yes":
                                    player_life_count = 3
                        
#---Treasure---
        if crossroads == "light":
            print("\n\tYou go left and in the distance you see the light of the moon reflecting on a chest but requires a four digit code.\n")
        left_path1 = input("\n\tDo you dare open the chest?\n\n").lower()
        if left_path1 == "yes":
            attempt_code1 = input("\n\tAlong the way there have been numbers that correlate with the special padlock infront of you, please enter the four-digit code carefully?\n\n")
            attempt_code1_conver = int(attempt_code1)
            if attempt_code1_conver == 7685:
                print("\n\tYou have opened the chest and found the treasure, hurry take it all before some else shows up.\n\n") 
                print("\n\tCONGRATS, You WON!!!!\n\n")
                break
            else:
                print(f"\n\tYou have failed to open the chest succesfully and poison darts hit your body killing you.\n")
                player_life_count -= 1
                if player_life_count == 0:
                    print("\n\tThank you for playing; If you want to start the adventure again reset the game.\n")
                else:
                    print(f"\n\tYou currenty have {player_life_count} life remaining.\n")
                    if player_life_count >= 1:
                        try_again = input("\n\tDo you want to try again? Yes or No\n\n").lower()
                        if try_again == "no":
                            print("\n\tThank you for playing\n\n")
                            break
#---Reset Game---
                    if player_life_count == 0:
                        print("\n\tThank you for playing; reset the game if you want to start the adventure again.\n")
                        try_again = input("\n\tDo you want to try again? Yes or No\n").lower()
                        if try_again == "yes":
                            player_life_count = 3
                        if try_again == "no":
                            print("\n\tThank you for playing\n\n")
                            break