string = input("Digite uma string para inverter: ")

reverse = ""

for i in range(len(string)):
    reverse += string[len(string) - 1 - i]

invertida_new = ""
for j in reverse:
    if j != ' ':
        invertida_new += j

print(f"String invertida sem espaços: {invertida_new}")
