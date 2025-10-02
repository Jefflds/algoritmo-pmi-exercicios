# Receba o número de voltas, a extensão do circuito (em metros) e o tempo de duração (minutos). Calcule e mostre a velocidade média em km/h.

def main():
    try:
        num_voltas_str = input("Informe o número de voltas: ").strip()
        num_voltas = int(num_voltas_str)
        extensao_circuito_str = input("Informe a extensão do circuito (em metros): ").strip()
        extensao_circuito = float(extensao_circuito_str)
        tempo_duracao_str = input("Informe o tempo de duração (em minutos): ").strip()
        tempo_duracao = float(tempo_duracao_str)
    except ValueError:
        print("Entrada inválida. Informe números válidos.")
        return

    if num_voltas <= 0 or extensao_circuito <= 0 or tempo_duracao <= 0:
        print("Todos os valores devem ser positivos e maiores que zero.")
        return

    distancia_total_metros = num_voltas * extensao_circuito
    distancia_total_km = distancia_total_metros / 1000
    tempo_duracao_horas = tempo_duracao / 60

    velocidade_media_kmh = distancia_total_km / tempo_duracao_horas
    print(f"Velocidade média: {velocidade_media_kmh:.2f} km/h")

main()