def soma_imposto(valor, imposto):
    taxa = imposto / 100
    valor_total = valor + valor * taxa

    return valor_total


valor_prod = float(input('Digite o valor do produto: '))
valor_taxa = float(input('Digite o valor do imposto a ser aplicado no produto: '))

somaImposto = soma_imposto(valor_prod, valor_taxa)
print(f'O valor do produto com o imposto fica: {somaImposto:.2f}')