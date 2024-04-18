def saudacao(nome):
  print(f"Olá, {nome}!")

print("\n chamando a função saudacao:")
saudacao("Alice")
saudacao("Bob")

# função com retorno
def quadrado(numero):
  resultado = numero ** 2
  return resultado

print("\n Chamando função quadrado:")
resultado_quadrado = quadrado(5)
print("Resultado da função quadrado:", resultado_quadrado)

#função com multiplos parametros
def soma(numero1, numero2):
  resultado = numero1 + numero2 
  return resultado

print("\n Chamando a função soma:")
numero1 = 20
numero2 = 50
resultado_soma = soma(numero1, numero2)
print("A soma entre no numero %s e %s é %s " % (numero1, numero2, resultado_soma))