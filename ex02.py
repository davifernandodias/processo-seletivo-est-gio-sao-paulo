n = int(input("escreve n: "))
a, b = 0, 1
pertence = False # inicializando false!!!!

for n in range(n + 1): 
    if a == n:
        pertence = True
        break
    a, b = b, a + b

if pertence:
    print(f"O número {pertence} pertence à sequência de fibonacci.")
else:
    print(f"O número {pertence} NÃO pertence à sequência de fibonnacci.")
