def calcul(a, b):
    c = a * b
    return c

if __name__ == '__main__':
    a = int(input("entrer un entier : "))
    b = int(input("entrer un entier : "))
    print("resultat du calcul ",a," x ",b," : ",calcul(a,b))