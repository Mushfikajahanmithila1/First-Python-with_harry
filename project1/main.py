import random
'''
1 = snake
-1 = water
0 = gun

'''

computer = random.choice([1, -1, 0])
youstr = input("Enter your choice: ")
youdic = {"s": 1, "w": -1, "g": 0}
you = youdic[youstr]
reverse_dic = {1: "snake", -1: "water", 0: "gun"}

print(f"Your chose: {reverse_dic[you]}\nComputer chose: {reverse_dic[computer]}")

if(you == computer):
    print("It's a tie!")

else:
    if(computer == 1 and you == -1):
        print("You lose!")
    elif(computer == 1 and you == 0):
        print("You win!")
    elif(computer == 0 and you == 1):
        print("You lose!")
    elif(computer == 0 and you == -1):
        print("You win!")
    elif(computer == -1 and you == 0):
        print("You lose!")
    elif(computer == -1 and you == 1):
        print("You win!")
    else:
        print("Something went wrong!")