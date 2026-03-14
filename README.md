# Inverso Modular

Este script calcula el inverso modular de un número $a$ bajo un módulo $m$ siguiendo la lógica del Algoritmo de Euclides Extendido.

## Estructura del Código

El programa se divide en tres secciones clave que replican el cálculo manual:

1. **Inicialización**: 
   - `x0, x1 = 0, 1`: Define los coeficientes iniciales para la combinación lineal.
   - `valor_a, valor_m`: Copias de los valores originales para realizar las divisiones sucesivas.

2. **Bucle de Cálculo (`while`)**:
   - **Cociente (`q`)**: Determina cuántas veces cabe el divisor en el dividendo (`//`).
   - **Intercambio y Residuo**: Actualiza `valor_a` y `valor_m` usando el módulo (`%`). Es el mismo proceso de "bajar el divisor y el residuo" que se hace en papel.
   - **Actualización de `x`**: La línea `x0 = x1 - q * antiguo_x0` calcula el valor acumulado del inverso. El uso de variables "antiguas" evita que Python pierda los datos del paso anterior.

3. **Salida y Formato**:
   - `x1 % m0`: Ajusta el resultado para que siempre sea un número positivo dentro del módulo.
   - **Notación**: Imprime la congruencia final: $a \times x \equiv 1 \pmod{m}$.

### ¿Cómo llega al resultado?
El algoritmo trabaja en reversa. Mientras busca el Máximo Común Divisor (MCD) mediante divisiones, va guardando en `x0` y `x1` cómo deshacer esas operaciones. Cuando el residuo llega a **1**, el valor almacenado en `x1` es, por definición, el número que anula a todos los demás bajo ese módulo.

### (Ejemplo 3 y 11)
El programa encuentra que:
1.  Las divisiones sucesivas terminan en **1**.
2.  La combinación lineal resultante es $4 \times 3 + (-1) \times 11 = 1$.
3.  En aritmética modular, cualquier múltiplo del módulo (como $-1 \times 11$) equivale a **0**.
4.  Por lo tanto, nos queda: $4 \times 3 \equiv 1 \pmod{11}$.
