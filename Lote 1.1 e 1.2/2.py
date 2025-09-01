# Receba o salário de um funcionário e mostre o novo salário com reajuste de 15%.
salary: float = 0.0
new_salary: float = 0.0
percentage: float = 15.0

def calcNewSalary(salary: float, percentage: float) -> float:
    return salary * (1 + percentage / 100)

def sanitize_input(user_input: str) -> float:
    user_input = user_input.replace(',', '.').replace(' ', '').strip()
    try:
        value = float(user_input)
        return value
    except ValueError:
        print("Entrada inválida. Por favor, insira um número.")
        return 0.0

def main() -> None:
    while True:
        userSalaryInput = input("Digite o salário do funcionário (ou 'S' para sair): ")
        if userSalaryInput.upper() == 'S':
            break
        
        salary = sanitize_input(userSalaryInput)
        change_perc = input(f"Deseja alterar a porcentagem de aumento ({percentage}%)? (S/N): ")

        if change_perc.upper() == 'S':
            userPercInput = input("Digite a nova porcentagem: ")
            percentage = sanitize_input(userPercInput)
        
        new_salary = calcNewSalary(salary, percentage)
        print(f"O novo salário com reajuste é: {new_salary}")

main()