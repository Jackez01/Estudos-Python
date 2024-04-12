#declaração
nome_completo = "Lucas Geraldi"

nome_completo_aspas = """Lucas
Geraldi"""

nome_completo_quebra = "Lucas \
  Geraldi"

nome = "Lucas"
sobrenome = "Geraldi"

#Formatação
print("Nome completo (1 forma):", nome_completo)
print("Nome completo (2 forma):" + nome_completo)
print("Nome completo (3 forma):" + "Lucas" + " Geraldi")
print("Nome completo (4 forma):" + "Lucas", "Geraldi")
print("Nome completo (5 forma):", nome_completo_aspas)
print("Nome completo (6 forma):", nome_completo_quebra)
print("Nome completo (7 forma): %s" %nome_completo)
print("Nome completo (8 forma): %s %s" % (nome, sobrenome))
print(f"Nome completo (9 forma): {nome} {sobrenome}")
print("Nome completo (10 forma): {} {}".format(nome,sobrenome))

nome_completo.upper()
nome[0]

nome_completo.count("a")

nome.encode()
nome.encode().decode()
nome.replace("b", "a")

telefone = "(19) 99157-1536"
telefone.replace("(", "").replace(")", "").replace("-", "")

"-".join("Lucas")
nome_completo.split(" ")
nome.strip("x")

nome_completo.startswith("Lu")
# ou pode fazer dessa forma
"Lu" in nome
# e para saber se algo nao esta 
"abc" not in nome



