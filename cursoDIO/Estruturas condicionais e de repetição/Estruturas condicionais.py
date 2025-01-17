saldo=30000
saque = float(input("Qual o valor você gostaria de sacar ?"))

if saque <= saldo:
    print("Realizando o saque")
else:
    print("Saldo insuficiente, digite outro valor")


idade=input("Digite a sua idade ")


idade=int(idade)

if idade <18 and idade <16:
    print("Não pode ir para festas")
elif idade >=16 and idade <18:
    print("Pode ir para a festa apenas com a autorização dos seus pais")
else:
    print("Pode ir para as festas")
