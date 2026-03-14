def inverso_modular(a, m):
    m0 = m
    x0, x1 = 0, 1
    valor_a, valor_m = a, m

    if a % m == 0:
        return None

    print(f"{'q':<5} | {'a':<5} | {'m':<5} | {'x0':<5} | {'x1':<5}")
    print("-" * 35)

    while valor_a > 1 and valor_m != 0:
        q = valor_a // valor_m

        antiguo_a = valor_a
        antiguo_x0 = x0
        
        valor_a = valor_m
        valor_m = antiguo_a % valor_m
        
        x0 = x1 - q * antiguo_x0
        x1 = antiguo_x0
        
        print(f"{q:<5} | {valor_a:<5} | {valor_m:<5} | {x0:<5} | {x1:<5}")

    if valor_a != 1: return None
    return x1 % m0
# RESULTADO
a, m = 3, 11
resultado = inverso_modular(a, m)

if resultado:
    print("-" * 35)
    print(f"{a} * {resultado} ≡ 1 (mod {m})")
    print(f"Resultado final: {resultado}")
else:
    print("No existe inverso modular.")
