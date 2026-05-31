### Simulador de Imvestimento em CDB
taxa_mensal = 0.113  # 1.13% ao mês

valor_inical = float(input("Digite o Valor Inicial Investido:  "))
meses = int(input("Digite o Número de Meses do Investimento:  "))

valor_final = valor_inical * (1 + taxa_mensal) ** meses

print(f"valor_final apos {meses} meses: é R$ {valor_final:.2f}")
### Samuel Henrique Das Chagas