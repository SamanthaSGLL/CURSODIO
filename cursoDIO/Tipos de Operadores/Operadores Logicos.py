#Operadores Logicos

saldo=5000
saque=250
limite=200

condicao=saldo>=200 and saque<limite

print(condicao)

condicao=saldo>=200 or saque<limite

print(condicao)

condicao=not saldo>=200 or saque<limite

print(condicao)

condicao = saldo>= 200  and not saque<limite

print(condicao)