#Kivi-paber-käärid mäng. 
#Arvuti mõtleb välja ühe variandi - kivi, paber või käärid. Arvuti küsib kasutaja valikut. Programm ütleb, kes võitis.
#Täienda programmi nii, et mängitakse seni, kuni kasutaja ei taha enam mängi

from random import randint

list = ["rock", "paper", "scissors"]

r = "rock"
p = "paper"
s = "scissors"

while True:

    player = input("rock, paper, scissors:")
    computer = random.choice(list)

    if computer == player:
        print("You have a draw!")
    elif computer == r and player == s or computer == s and player == p or computer == p and player == r:
        print("Computer won!!")
    elif player == r and computer == s or player == s and computer == p or player == p and computer== r:
        print("Player won!!")
    else:
        print("Continue?: ")

if input == "Jes":
