# Receba a hora de início e de final de um jogo (HH,MM), calcular o tempo do jogo em horas e minutos, sabendo que o tempo máximo é menor que 24 horas e pode começar num dia e terminar noutro.

def main():
    try:
        hora_inicio_str = input("Informe a hora de início (HH:MM): ").strip()
        hora_fim_str = input("Informe a hora de término (HH:MM): ").strip()

        hora_inicio, minuto_inicio = map(int, hora_inicio_str.split(':'))
        hora_fim, minuto_fim = map(int, hora_fim_str.split(':'))

        if not (0 <= hora_inicio < 24 and 0 <= minuto_inicio < 60 and
                0 <= hora_fim < 24 and 0 <= minuto_fim < 60):
            print("Horas ou minutos inválidos. Use o formato HH:MM com valores válidos.")
            return

    except Exception:
        print("Entrada inválida. Use o formato HH:MM.")
        return

    inicio_total_minutos = hora_inicio * 60 + minuto_inicio
    fim_total_minutos = hora_fim * 60 + minuto_fim

    if fim_total_minutos <= inicio_total_minutos:
        fim_total_minutos += 24 * 60  # Adiciona um dia em minutos

    duracao_total_minutos = fim_total_minutos - inicio_total_minutos
    duracao_horas = duracao_total_minutos // 60
    duracao_minutos = duracao_total_minutos % 60

    print(f"Duração do jogo: {duracao_horas} horas e {duracao_minutos} minutos")

main()