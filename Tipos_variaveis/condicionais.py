#Exemplo de if
idade = 18
print("exemplo de comando if")
if idade >= 18: 
  print("Você é maior de idade")
elif idade >= 12:
  print("Você é um adolescente")
else:
  print("Você é menor de idade")

mensagem = "Pode tirar a carteira de habilitação" if idade >= 18 else "Você ainda não pode tirar habilitação"
print(mensagem)