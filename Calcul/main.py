## FONCTIONS
# Addition
def add(x,y):
    return (x+y)
# Subtraction
def sub(x,y):
    return (x-y)
# Multiplication
def mul(x,y):
    return (x*y)

# Divison
def div(x,y):
    try:
        x/y
    except ZeroDivisionError:
        print("Division by zero is not allowed, try again!")
        print()


# MAIN
while exit != True:
    # Calculator
    print("Veuillez entrer deux nombre")
    x = int(input())
    y = int(input())
    print("Que souhaitez vous faire avec: add, sup, div, mul")
    resultat = input()
    if resultat =="add":
        result =  add(x,y)
    elif resultat == "sup":
        result = sub(x,y)
    elif resultat == "div":
        result = div(x,y)
    elif resultat == "mul":
        result = mul(x,y)

    print(result)
    print("Voulez vous continuez ? oui, non")
    continu = input()
    if continu == "oui":
        exit = False
    else:
        exit = True
