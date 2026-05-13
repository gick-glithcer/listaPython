#Criando um Teste com Pontuação
print("Teste seus Conhecimentos sobre Ciências🔢")
pontos = 0
#-Questão 1--
print("Qual é a Formula da água ?🚰")
print("a-H20 \nb-C02  \nc-A1")
resposta1 = input("Digite a Resposta:").lower()
if resposta1 == "a":
   print("Resposta Correta👌" )
   pontos = pontos + 1
else:
   print("Você Errou❌!!!")
#-Questão 2--
print("2-O sol é ?☀️ ")
print("a-Satélite \nb-Estrela \nc-Asteróide")
resposta2 = input("Digite a Resposta:").lower()
if resposta2 == "b" :
   print("Você Acertou👌")
   pontos = pontos + 1
else:
   print("Você Errou❌!!!")
print("Fim do Questionário")
print(f"Sua Pontuação foi:{pontos}")
#Samuel Henrique Das Chagas--