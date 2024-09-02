estado_value = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

total = sum(estado_value.values())

print("Percentual de representação por estado:")
for estado, faturamento in estado_value.items():
    percentual = (faturamento / total) * 100
    print(f"{estado}: {percentual:.2f}%")
