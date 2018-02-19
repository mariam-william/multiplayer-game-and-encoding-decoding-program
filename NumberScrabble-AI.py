import random
from random import randint

y=[1,2,3,4,5,6,7,8,9]
x=[]
z=[]

print("                            Number Scrabble Game")
print("           Every Player Should Choose 3 Numbers to Make 15 and Win!")
print(" ")
print("Enter 1 for One Player. Enter 2 for 2 players")

while True:
    try:
        m=int(input("Enter the number: " ))
    except Exception as e:
        print (" You should enter only 1 or 2.")
        continue
    if m<1 or m>2:
        print(" You should enter only 1 or 2.")
        continue
    break
if m==1:
    print(y , "Every player should pick a number from the list.")
    p1=input("Player 1, enter your name: ")
    while True:
        try:
            a1=int(input(p1+", pick a number: "))
        except Exception as e:
            print (p1+ ", You should pick an integer number from the list.")
            continue
        if a1 not in y:
            print("This number is picked before or not in the list. pick another number fron the list.")
            continue
        break
    
    y.remove(int(a1))
    comp=random.choice(y)
    y.remove(comp)
    print("Computer: ",comp)
    print("The remaining numbers:",y, ", pick a number",p1)
    z.append(comp)
    
    while True:
        try:
            a2=int(input(p1+": " ))
        except Exception as e:
            print (p1+ ", You should pick an integer number from the list.")
            continue
        if a2 not in y:
            print("This number is picked before or not in the list. pick another number fron the list.")
            continue
        break
    
    y.remove(int(a2))
    comp=random.choice(y)
    y.remove(comp)
    z.append(comp)
    print("Computer: ",comp)
    print("The remaining numbers:",y, ", pick a number",p1)
    
    while True:
        try:
            a3=int(input(p1+": " ))
        except Exception as e:
            print (p1+ ", You should pick an integer number from the list.")
            continue
        if a3 not in y:
            print("This number is picked before or not in the list. pick another number fron the list.")
            continue
        break

    while y > x:
        if a1+a2+a3 == 15:
            print (p1+" Wins!")
            break

        y.remove(int(a3))
        comp=random.choice(y)
        y.remove(comp)
        print("Computer: ",comp)
        z.append(comp)
        
        if z[0]+z[1]+z[2]==15:
            print("You Lose!")
            break
        print("The remaining numbers:",y, ", pick a number",p1)

        while True:
            try:
                a4=int(input(p1+": " ))
            except Exception as e:
                print (p1+ ", You should pick an integer number from the list.")
                continue
            if a4 not in y:
                print("This number is picked before or not in the list. pick another number fron the list.")
                continue
            break
        y.remove(int(a4))
        if (a1+a2+a4==15 or a2+a3+a4==15 or a1+a3+a4==15):
            print(p1+" Wins!")
            break
        
        comp=random.choice(y)
        y.remove(comp)
        print("Computer: ",comp)
        z.append(comp)
        if z[0]+z[1]+z[3]==15 or z[1]+z[2]+z[3]==15 or z[0]+z[1]+z[3]==15:
            print("You Lose!")
            break
        print("The remaining numbers:",y, ", pick a number",p1)
        
        while True:
            try:
                a5=int(input(p1+": " ))
            except Exception as e:
                print (p1+ ", You should pick an integer number from the list.")
                continue
            if a5 not in y:
                print("This number is picked before or not in the list. pick another number fron the list.")
                continue
            break
        
        y.remove(int(a5))
        if (a1+a2+a5==15 or a1+a3+a5==15 or a1+a4+a5==15 or a2+a3+a5==15 or a2+a4+a5==15 or a3+a4+a5==15):
            print(p1+" Wins!")
            break
        
        print("Game is draw. Play again!")

if m==2:
    p1=input("Player 1, enter your name: ")
    p2=input("Player 2, enter your name: ")

    #The list of the numbers.
    print(y , "Every player should pick a number from the list.")

    #Player1 plays.
    while True:
        try:
            a1=int(input(p1+", pick a number: " ))
        except Exception as e:
            print (p1+ ", You should pick an integer number from the list.")
            continue
        if a1 not in y:
            print("This number is picked before or not in the list. pick another number fron the list.")
            continue
        break
    y.remove(int(a1))

    #Player2 plays.
    while True:
        try:
            b1=int(input(p2+", pick a number: "))
        except Exception as e:
            print (p2+ ", You should pick an integer number from the list.")
            continue
        if b1 not in y:
            print("This number is picked before or not in the list. pick another number fron the list.")
            continue
        break
    y.remove(int(b1))
    print("The remaining numbers:",y, ", pick a number",p1)

    #player1 plays again.
    while True:
        try:
            a2=int(input(p1+": " ))
        except Exception as e:
            print (p1+ ", You should pick an integer number from the list.")
            continue
        if a2 not in y:
            print("This number is picked before or not in the list. pick another number fron the list.")
            continue
        break
    y.remove(int(a2))
    print("The remaining numbers:",y, ", pick a number",p2)

    #playe2 's turn.
    while True:
        try:
            b2=int(input(p2+": " ))
        except Exception as e:
            print (p2+ ", You should pick an integer number from the list.")
            continue
        if b2 not in y:
            print("This number is picked before or not in the list. pick another number fron the list.")
            continue
        break
    y.remove(int(b2))
    print("The remaining numbers:",y, ", pick a number",p1)

    #player1 's turn.
    while True:
        try:
            a3=int(input(p1+": " ))
        except Exception as e:
            print (p1+ ", You should pick an integer number from the list.")
            continue
        if a3 not in y:
            print("This number is picked before or not in the list. pick another number fron the list.")
            continue
        break
    y.remove(int(a3))

    #start to check if any player wins.
    while y > x:
        if a1+a2+a3 == 15:
            print (p1+" Wins!")
            break
        print("The remaining numbers:",y, ", pick a number",p2)
    
        while True:
            try:
                b3=int(input(p2+": " ))
            except Exception as e:
                print (p2+ ", You should pick an integer number from the list.")
                continue
            if b3 not in y:
                print("This number is picked before or not in the list. pick another number fron the list.")
                continue
            break
        y.remove(int(b3))
    
        if b1+b2+b3 == 15:
            print (p2+" Wins!")
            break
        print("The remaining numbers:",y, ", pick a number",p1)

        while True:
            try:
                a4=int(input(p1+": " ))
            except Exception as e:
                print (p1+ ", You should pick an integer number from the list.")
                continue
            if a4 not in y:
                print("This number is picked before or not in the list. pick another number fron the list.")
                continue
            break
        y.remove(int(a4))
    
        if (a1+a2+a4==15 or a2+a3+a4==15 or a1+a3+a4==15):
            print(p1+" Wins!")
            break
        print("The remaining numbers:",y, ", pick a number",p2)
  
        while True:
            try:
                b4=int(input(p2+": " ))
            except Exception as e:
                print (p2+ ", You should pick an integer number from the list.")
                continue
            if b4 not in y:
                print("This number is picked before or not in the list. pick another number fron the list.")
                continue
            break
        y.remove(int(b4))
     
        if (b1+b2+b4==15 or b1+b3+b4==15 or b2+b3+b4==15):
            print(p2+" Wins!")
            break
        else:
            print("The remaining numbers:",y, ", pick a number",p1)

        while True:
            try:
                a5=int(input(p1+": " ))
            except Exception as e:
                print (p1+ ", You should pick an integer number from the list.")
                continue
            if a5 not in y:
                print("This number is picked before or not in the list. pick another number fron the list.")
                continue
            break
        y.remove(int(a5))
        
        if (a1+a2+a5==15 or a1+a3+a5==15 or a1+a4+a5==15 or a2+a3+a5==15 or a2+a4+a5==15 or a3+a4+a5==15):
            print(p1+" Wins!")
            break

        print("Game is draw. Play again!")
