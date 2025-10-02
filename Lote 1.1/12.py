# Receba o ano de nascimento e o ano atual. Calcule e mostre a sua idade e quantos anos terá daqui a 17 anos.

while True:
    try:
        birth_year_str = input("Informe o ano de nascimento (ou 'S' para sair): ").strip()
        if birth_year_str.upper() == 'S':
            break
        current_year_str = input("Informe o ano atual: ").strip()
        birth_year = int(birth_year_str)
        current_year = int(current_year_str)
    except ValueError:
        print("Entrada inválida. Informe números inteiros para os anos.")
        continue

    if birth_year > current_year:
        print("Ano de nascimento não pode ser maior que o ano atual.")
        continue

    # Calcular idade
    age = current_year - birth_year
    age_in_17_years = age + 17

    print(f"Sua idade atual é: {age} anos")
    print(f"Sua idade daqui a 17 anos será: {age_in_17_years} anos")
    
    continue_input = input("Deseja calcular outra idade? (S/N): ")
    if continue_input.upper() == 'N':
        break