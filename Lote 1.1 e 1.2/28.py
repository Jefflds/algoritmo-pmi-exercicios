# Receba o preço atual e a média mensal de um produto. Calcule e mostre o novo preço sabendo que:
# Venda Mensal        Preço Atual      Preço Novo
# < 500               < 30               +10%
# >= 500 e <1000      >= 30 e <80        +15%
# >=1000              >= 80              -5%

def main():
    try:
        preco_atual_str = input("Informe o preço atual do produto: ").strip()
        preco_atual = float(preco_atual_str)

        venda_mensal_str = input("Informe a média mensal de vendas do produto: ").strip()
        venda_mensal = float(venda_mensal_str)
    except Exception:
        print("Entrada inválida. Informe números para o preço e a venda mensal.")
        return

    if venda_mensal < 500 and preco_atual < 30:
        preco_novo = preco_atual * 1.10
    elif 500 <= venda_mensal < 1000 and 30 <= preco_atual < 80:
        preco_novo = preco_atual * 1.15
    elif venda_mensal >= 1000 and preco_atual >= 80:
        preco_novo = preco_atual * 0.95
    else:
        preco_novo = preco_atual  # No change if conditions are not met

    print(f"Novo preço do produto: {preco_novo:.2f}")
main()
