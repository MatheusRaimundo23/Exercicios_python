#Cadastro
nome= input("digite seu nome:")
Sobrenome=input("digite seu sobrenome:")
Idade = int(input("Digite sua idade:"))
Maior_Idade = bool
if (Idade >= 18):
  print("Maior de idade");
  Maior_Idade = True
else:
    print("Menor de idade");
    Maior_Idade = False
Ano_nascimento=input("digite seu ano nascimento")
Altura_metros=input("digite sua Altura metros")   
print("nome:", nome)
print("Sobrenome:",Sobrenome)
print("Idade:", Idade)
print("Altura_metros:", Altura_metros)
print("maior de idade?:",Maior_Idade)
