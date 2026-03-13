# Valores iniciales
a = 3
m = 11

a_original = a
m0 = m
x0 = 0
x1 = 1
valor_a = a
valor_m = m

print(f"Iniciando: a={a}, m={m}")
print("-" * 30)

# La condición 
if a % m == 0:
    print("No existe inverso modular porque mcd(a, m) > 1")
else:
    # El bucle 'Mientras' 
    while valor_a > 1 and valor_m != 0:
        q = valor_a // valor_m
        
        # Guardamos valores para no perderlos
        temp_a = valor_a
        temp_x0 = x0 
        
        valor_a = valor_m
        valor_m = temp_a % valor_m
        
        # x1 toma el valor PREVIO de x0
        x0 = x1 - q * temp_x0
        x1 = temp_x0
        
        print(f"q={q}, valor_a={valor_a}, valor_m={valor_m}, x0={x0}, x1={x1}")

    # Verificación final
    if valor_a != 1:
        print("No existe inverso modular")
    else:
        # Regresa x1 mod m0
        resultado = x1 % m0
        print("-" * 30)
        print(f"Resultado final: {resultado}")
