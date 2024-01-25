print("-" * 60)
print()
operador = str(input(f"Por favor digite um operador entre (+, -, *, /): "))

if operador not in ["+", "-", "*", "/"]:
    print("Operador inválido")
    breakpoint()
else:
    n1 = int(input(f"Digite o primeiro número: "))
    n2 = int(input(f"Digite o segundo número: "))

if operador == "+":
    print(f"A soma dos números é: {n1 + n2}")
    
elif operador == "-":
    print(f"A subtração dos números é: {n1 - n2}")
    
elif operador == "*":
    print(f"A multiplicação dos números é: {n1 * n2}")
    
elif operador == "/":
    if n2 == 0:
        print("Não é possível dividir por zero")
        breakpoint()
    else:
        print(f"A divisão dos números é: {n1 / n2}")

print("Isso foi tudo.")
print("Encerrando...")
print()
print("-" * 60)