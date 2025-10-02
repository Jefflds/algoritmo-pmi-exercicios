# Receba a quantidade de horas trabalhadas, o valor por hora, o percentual de desconto e o número de dependentes. Calcule o salário que serão as horas trabalhadas x o valor por hora. Calcule o salário líquido (= SalárioBruto – desconto). A cada dependente será acrescido R$ 100 no Salário Líquido. Exiba o salário a receber.

while True:
    try:
        horas_str = input("Informe a quantidade de horas trabalhadas (ou 'S' para sair): ").strip()
        if horas_str.upper() == 'S':
            break
        valor_hora_str = input("Informe o valor por hora: ").strip()
        percentual_desconto_str = input("Informe o percentual de desconto (ex: 10 para 10%): ").strip()
        num_dependentes_str = input("Informe o número de dependentes: ").strip()

        horas = float(horas_str)
        valor_hora = float(valor_hora_str)
        percentual_desconto = float(percentual_desconto_str)
        num_dependentes = int(num_dependentes_str)
    except ValueError:
        print("Entrada inválida. Informe números válidos.")
        continue

    # Calcular salário
    salario_bruto = horas * valor_hora
    desconto = (percentual_desconto / 100) * salario_bruto
    salario_liquido = salario_bruto - desconto + (num_dependentes * 100)

    print(f"Salário a receber: R$ {salario_liquido:.2f}")
    
    continue_input = input("Deseja calcular outro salário? (S/N): ")
    if continue_input.upper() == 'N':
        break