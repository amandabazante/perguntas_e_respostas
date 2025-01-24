print("Qual a capital do Brasil? a) Brasilia b) Rio de Janeiro c) São Paulo d) Recife")
resposta = input("Escolha a alternativa correta: ")
if resposta == ("a"):
  print("Você acertou")
else:
  print("Você errou")

print("Quantos dentes temos na boca? a) 25 b) 30 c) 32 d) 35")
resposta = input("Escolha a alternativa correta: ")
if resposta == ("c"):
  print("Você acertou")
else:
  print("Você errou")


print("Olá, seja bem vindo!")
print("Cada pergunta terá um valor determinado!")
print("Segue os valores:")
print("A primeira pergunta vale 20 pontos!")
print("A segunda pergunta vale 10 pontos!")

perguntas = ["Qual a capital do Brasil?" , "Quantos dentes temos na boca?"]
respostas = ["Brasília" , "32"]
pontuacao = 0
respostas_corretas = 0

for pergunta in perguntas:
    print(pergunta)
    resposta_usuario = str(input('Qual sua resposta?: '))
    for resposta in respostas:
        if resposta_usuario == resposta:
            respostas_corretas += 1
pontos = respostas_corretas * 20 + 10

print('Você acertou {} perguntas e sua pontuação é {}'.format(respostas_corretas, pontos))