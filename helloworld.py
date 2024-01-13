x = float(input("ingresa un numero "))
y = float(input("ingresa otro numero "))
def sum(x,y):
    sum = (x+y)%2
    if sum == 0:
        print("par")
    else:
        print("impar")  
sum(x,y)