saldo= 1000
limite = 500

print(saldo is limite) #não ocupa a mesma regiao de memoria
print(saldo is not limite)

saldo = 1000
limite =1000
print("--------------------------------")
print(saldo is limite) #não ocupa a mesma regiao de memoria
print(saldo is not limite)

