

import random

 

options = ["Kivi", "Paber", "Käärid"]

 

user_choice = input("Kivi, Paber, või Käärid: ")

computer_choice = random.choice(options)

 

print("Sa valisid: ", user_choice)

print("Arvuti: ", computer_choice)

 

if user_choice == computer_choice:

    print("Viik!")

elif user_choice == "Rock" and computer_choice == "Scissors":

    print("Sa võitsid!")

elif user_choice == "Paper" and computer_choice == "Rock":

    print("Sa võitsid!")

elif user_choice == "Käärid" and computer_choice == "Paper":

    print("Sa võitsid!")

else:

    print("Sa kaotasid!")