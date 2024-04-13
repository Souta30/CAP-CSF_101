################################
# Tashi Tenzin
# First ELECTRICAL
# 02220097
################################
# REFERENCES
# @CHAT_GPT
################################
# SOLUTION
# Your Solution Score:50169
# Put your number here
# CAP-CSF_101/input_7_cap1.txt
################################

# One of the way to read a input file in function read_input()
def read_input(FILENAME): # we should calla function (parameter:FILENAME)
    LIST = [] #optimizing a new list in order to store a data
    with open(FILENAME, 'r') as READ:# a new way to read an input file
        for WAY in READ:#we should use for loop
            opponent_choice, outcome = WAY.split()
            LIST.append((opponent_choice, outcome))
    return LIST # we should be able to Return a function again

# Calling a second function in order to calculate the score in ()
def calculate_score(ROUNDS):
    Score1 = 0
    for choice_of_opponent, outcomes in ROUNDS:
        if outcomes == 'X': # If the opponent got X, the player should be defeated
            if choice_of_opponent == 'A':
                Score1 += 3  # SO if the opponent chose rock, player should get scissor to get defeat
            elif choice_of_opponent == 'B':
                Score1 += 1  # SO if the opponent chose paper, player should get rock to get defeat
            elif choice_of_opponent == 'C':
                Score1 += 2  # SO if the opponent chose scissor, player should get paper to get defeat
        elif outcomes == 'Y':  #if the opponent got Y, the player should get draw with the opponent
            if choice_of_opponent == 'A':
                Score1 += 4  # SO if the opponent chose rock, player should get rock to get draw
            elif choice_of_opponent == 'B':
                Score1 += 5  # SO if the opponent chose paper, player should get paper to get draw
            elif choice_of_opponent == 'C':
                Score1 += 6  # SO if the opponent chose scissor, player should get scissor to get draw
        elif outcomes == 'Z':  # if the opponent got Z, the player should be get victory over the opponent
            if choice_of_opponent == 'A':
                Score1 += 8  # SO if the opponent chose rock, player should get paper to win
            elif choice_of_opponent == 'B':
                Score1 += 9  # SO if the opponent chose paper, player should get scissor to get defeat
            elif choice_of_opponent == 'C':
                Score1 += 7  # SO if the opponent chose scissor, player should get rock to get defeat
    print("The total score is:", Score1) #outcomes : your total score is evaluted as score1

#Now runnint the fuction that wa scalled earlier
FILENAME = "CAP-CSF-_101/input_7_cap1.txt" # Now inputiing a Specified file
calculate_score(read_input(FILENAME))