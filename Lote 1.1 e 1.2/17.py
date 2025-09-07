# Calcule a quantidade de litros gastos em uma viagem, sabendo que o automóvel faz 12 km/l. Receber o tempo de percurso e a velocidade média.

def main():
    try:
        tempo_str = input("Informe o tempo de percurso em horas: ").strip()
        velocidade_str = input("Informe a velocidade média em km/h: ").strip()
        tempo = float(tempo_str)
        velocidade = float(velocidade_str)
    except Exception:
        print("Entrada inválida. Informe números válidos.")
        return

    if tempo <= 0 or velocidade <= 0:
        print("O tempo e a velocidade devem ser positivos.")
        return

    distancia = tempo * velocidade
    litros_gastos = distancia / 12

    print(f"Quantidade de litros gastos: {litros_gastos:.2f} L")

main()