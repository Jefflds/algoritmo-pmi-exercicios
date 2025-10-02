# Receba o número de voltas, a extensão do circuito (em metros) e o tempo de duração (minutos). Calcule e mostre a velocidade média em km/h.

while True:
    try:
        voltas_str = input("Informe o número de voltas (ou 'S' para sair): ").strip()
        if voltas_str.upper() == 'S':
            break
        voltas = int(voltas_str)
        extensao_str = input("Informe a extensão do circuito em metros: ").strip()
        extensao = float(extensao_str)
        tempo_str = input("Informe o tempo de duração em minutos: ").strip()
        tempo_minutos = float(tempo_str)
    except ValueError:
        print("Entrada inválida. Informe números válidos.")
        continue

    if voltas <= 0 or extensao <= 0 or tempo_minutos <= 0:
        print("Todos os valores devem ser positivos.")
        continue

    # Calcular velocidade média em km/h
    distancia_total_metros = voltas * extensao
    distancia_total_km = distancia_total_metros / 1000
    tempo_horas = tempo_minutos / 60
    velocidade_media = distancia_total_km / tempo_horas

    print(f"Velocidade média: {velocidade_media:.2f} km/h")
    
    continue_input = input("Deseja calcular outra velocidade? (S/N): ")
    if continue_input.upper() == 'N':
        break