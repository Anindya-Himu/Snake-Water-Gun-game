import random
computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice: ")
youDict = {"s":1, "w":-1, "g":0}
reverseDict = {1: "Snake", -1:"Water", 0:"Gun"}

you = youDict[youstr]

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

if(computer==you):
    print("It's a draw")
else:
    # if (computer==-1 and you ==1): 
    #     print("You Win!")
    # elif(computer ==-1 and you==0):
    #     print("You Lose")
    # elif(computer ==1 and you==-1):
    #     print("You Lose!")
    # elif(computer ==-1 and you==0):
    #     print("You Win!")
    # elif(computer==0 and you ==-1):
    #     print("You Win!")
    # elif(computer==0 and you ==1):
    #     print("You Lose!")
    # else:
    #     print("Something went wrong!")

    if((computer - you)== -1 or (computer - you)== 2):
        print("You Lose!")
    else:
        print("You Win!")

# So basically we can just write the program just like this and reduce a lot of lines. But by doing this,it will lose it's readability
# and we have to explain why we have done that to examiner. So it's not recommandable,but we can also do this!!