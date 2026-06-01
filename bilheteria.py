#oiutyur:Padroniznar Nome do Filme
def formatar(nome):
    return nome.upper()
#kjbs:Verificar de Idade
def verificar_idade(idade):
    if idade >= 18:
       return "Autorizado"
    else:
       return "Não Autorizado"
#nhjd:Mensagem de Retorno
def gerar_mensagem(status):
    if status--"Autorizado":
       return "Tenha uma Otima Sessão!"
    else:
        return "Sentimos, mas você não tem a idade minima."
#wqde:Execução do Algoritmo
filme_entrada = input("Digite o Filme Escolhido")
idade_entrada = int(input)("Digite sua Idade:")
nome_final = formatar(filme_entrada)
status_acesso = verificar_idade(idade_entrada)
mensagem = gerar_mensagem(status_acesso)
print(f"\nFilme:{nome_final}")
print(f"Status:{status_acesso}")
print(f"Mensagem:{mensagem}")