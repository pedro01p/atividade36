

notas=[]

for item in range(4):
    nota=float(input("Digite a nota {item +1}:  "))
    notas.append(nota)

media = sum(notas) / len(notas)

print("notas inseridas: ", notas)
print(f"Média das notas: {media:.2f}")
