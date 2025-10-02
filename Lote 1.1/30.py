# Receba a data de nascimento e atual em ano, mês e dia. Calcule e mostre a idade em anos, meses e dias, considerando os anos bissextos.

while True:
    try:
        print("Data de nascimento:")
        dia_nasc = int(input("Dia: "))
        mes_nasc = int(input("Mês: "))
        ano_nasc = int(input("Ano: "))
        
        continuar = input("Digite 'S' para sair ou pressione Enter para continuar: ").strip()
        if continuar.upper() == 'S':
            break
            
        print("Data atual:")
        dia_atual = int(input("Dia: "))
        mes_atual = int(input("Mês: "))
        ano_atual = int(input("Ano: "))
    except ValueError:
        print("Entrada inválida. Digite números inteiros para as datas.")
        continue

    # Calcular idade
    anos = ano_atual - ano_nasc
    meses = mes_atual - mes_nasc
    dias = dia_atual - dia_nasc

    # Ajustar se dias são negativos
    if dias < 0:
        meses -= 1
        # Dias do mês anterior
        if mes_atual == 1:
            dias_mes_anterior = 31 if ano_atual % 4 == 0 and (ano_atual % 100 != 0 or ano_atual % 400 == 0) else 28 if mes_atual == 3 else [31,28,31,30,31,30,31,31,30,31,30,31][mes_atual-2]
        else:
            dias_mes_anterior = [31,28,31,30,31,30,31,31,30,31,30,31][mes_atual-2]
        dias += dias_mes_anterior

    # Ajustar se meses são negativos
    if meses < 0:
        anos -= 1
        meses += 12

    print(f"Idade: {anos} anos, {meses} meses e {dias} dias")
    
    continue_input = input("Deseja calcular outra idade? (S/N): ")
    if continue_input.upper() == 'N':
        break