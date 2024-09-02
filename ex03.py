import json

def calcular_faturamento(faturamento_mensal):
    small_fatura = float('inf')  
    large_fatura = float('-inf')  
    soma_faturamento = 0
    dias_com_faturamento = 0

    for entrada in faturamento_mensal:
        valor = entrada['faturamento']
        if valor > 0:  
            if valor < small_fatura:
                small_fatura = valor
            if valor > large_fatura:
                large_fatura = valor
            soma_faturamento += valor
            dias_com_faturamento += 1

    media_mensal = soma_faturamento / dias_com_faturamento if dias_com_faturamento > 0 else 0

    dias_acima_da_media = sum(1 for entrada in faturamento_mensal if entrada['faturamento'] > media_mensal)

    return small_fatura, large_fatura, dias_acima_da_media

def carregar_dados_json(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        dados = json.load(arquivo)
    return dados

faturamento_mensal = carregar_dados_json('faturamento.json')

menor, maior, dias_acima = calcular_faturamento(faturamento_mensal)

print(f"Menor valor de faturamento: {menor}")
print(f"Maior valor de faturamento: {maior}")
print(f"Número de dias com faturamento acima da média: {dias_acima}")
