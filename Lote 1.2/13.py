# Receba a quantidade de alimento em quilos. Calcule e mostre quantos dias durará esse alimento sabendo que a pessoa consome 50g ao dia.

def main():
    try:
        alimento_kg_str = input("Informe a quantidade de alimento em quilos: ").strip()
        alimento_kg = float(alimento_kg_str)
    except Exception:
        print("Entrada inválida. Informe um número para a quantidade de alimento.")
        return

    if alimento_kg < 0:
        print("A quantidade de alimento não pode ser negativa.")
        return

    alimento_g = alimento_kg * 1000
    consumo_diario_g = 50
    dias_duracao = alimento_g / consumo_diario_g

    print(f"O alimento durará {dias_duracao:.0f} dias.")

main()