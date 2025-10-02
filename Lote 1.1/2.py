# Receba o salário de um funcionário e mostre o novo salário com reajuste de 15%.

while True:
    userSalaryInput = input("Digite o salário do funcionário (ou 'S' para sair): ")
    if userSalaryInput.upper() == 'S':
        break
    
    # Sanitizar entrada
    userSalaryInput = userSalaryInput.replace(',', '.').replace(' ', '').strip()
    try:
        salary = float(userSalaryInput)
        percentage = 15.0
        
        change_perc = input(f"Deseja alterar a porcentagem de aumento ({percentage}%)? (S/N): ")
        
        if change_perc.upper() == 'S':
            userPercInput = input("Digite a nova porcentagem: ")
            userPercInput = userPercInput.replace(',', '.').replace(' ', '').strip()
            try:
                percentage = float(userPercInput)
            except ValueError:
                print("Entrada inválida para porcentagem. Usando 15%.")
                percentage = 15.0
        
        # Calcular novo salário
        new_salary = salary * (1 + percentage / 100)
        print(f"O novo salário com reajuste é: {new_salary}")
    except ValueError:
        print("Entrada inválida. Por favor, insira um número.")