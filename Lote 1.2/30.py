# Receba a data de nascimento e atual em ano, mês e dia. Calcule e mostre a idade em anos, meses e dias, considerando os anos bissextos.

def main():
    try:
        ano_nascimento = int(input("Informe o ano de nascimento: "))
        mes_nascimento = int(input("Informe o mês de nascimento: "))
        dia_nascimento = int(input("Informe o dia de nascimento: "))

        ano_atual = int(input("Informe o ano atual: "))
        mes_atual = int(input("Informe o mês atual: "))
        dia_atual = int(input("Informe o dia atual: "))
    except ValueError:
        print("Entrada inválida. Informe números inteiros para a data.")
        return

    anos = ano_atual - ano_nascimento
    meses = mes_atual - mes_nascimento
    dias = dia_atual - dia_nascimento

    if dias < 0:
        meses -= 1
        dias += 30  # Aproximação, não considera meses com 28/29/31 dias

    if meses < 0:
        anos -= 1
        meses += 12

    print(f"Idade: {anos} anos, {meses} meses e {dias} dias.")

main()