#Etapa 1 - Calculo do IMC
def calc_imc(peso,altura):
    imc = peso / (altura * altura)
    return imc
#Etapa 2- CLassificar o IMC
def classificar_imc(valor_imc):
    if valor_imc >=25 :
        return "ACIMA DO PESO"
    else:
        return "PESO NORMAL"
#Etapa 3 - Mensagem de Saída
def mensagem(status):
    if status == "ACIMA DO PESO":
        return "!ATENÇÃO! Procure um Médico"
    else:
        return "Muito Bom, Continue Assim"
#Etapa 4 - Integração do Projeto
valor_peso = float(input("Digite seu peso Atual: "))
valor_altura  = float(input("Digite sua ALtura: "))

resultado = calc_imc(valor_peso,valor_altura)
classificar = classificar_imc(resultado)
saida = mensagem(classificar)

print("=" * 50)
print(f"Seu IMC é:{resultado:.1f}")
print(f"{saida}")
print("=" * 50)