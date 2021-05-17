import random

def game(comp,you):
    if comp==you:
        return None
    elif comp=="s":
        if you=="p":
            return False
        elif you=="r":
            return True
    elif comp=="p":
        if you=="r":
            return False
        elif you=="s":
            return True
    elif comp=="r":
        if you=="p":
            return True
        elif you=="s":
            return False

print("Computer turn :")
ran=random.randint(1,3)
if ran==1:
    comp="r"
elif ran==2:
    comp="p"
elif ran==3:
    comp="s" 

you=input("Players turn : Rock(r) Paper(p) or sessor(s) : ")
a=game(comp,you)

print(f"Computer choose {comp}")
print(f"You choose {you}")


if a==None:
    print("Game is TIE !!!")
elif a:
    print("You WIN!!!!")
else:
    print("You LOSE !!!!") 