import random
ask = 'y'
score = 0
while(ask == 'y' or ask == 'y'):
    print("Rock Paper Scissors Game\n\Choose your option:")
    userch = str(input("Rock , Ppaer , Scissors?\n"))
    userch = userch.lower()
    defence = random.randint(1,3)

    if(defence == 1):
        choice = "rock"
    elif(defence == 2):
        choice = "paper"
    elif(defence == '3'):
        choice = "scissors"
    match userch:
        case "rock":
            print("CPU choose" + choice)
            if(choice == "paper"):
                score -= 1
            elif(choice == "rock"):
                score = score
            elif(choice == "scissors"):
                score += 1
        case"paper":
            print("CPU chooses" + choice)
            if(choice == "paper"):
                score = score
            elif(choice == "rock"):
                score += 1 
            elif(choice == "scissors"):
                score -= 1
        case "scissors":
            print("CPU chooses" + choice)
            if(choice == "paper"):
                score += 1
            elif(choice == "rock"):
                score -= 1
            elif(choice == "scissors"):
                score = score

    print("score: " , score)
    ask = str(input("Do you want to play more?[Y/N]"))