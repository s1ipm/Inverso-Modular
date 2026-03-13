# Inverso Modular

## Estructura del Código

El script se divide en tres bloques fundamentales que reflejan el procedimiento matemático:

### 1. Inicialización de Variables
El código comienza preparando el "entorno de trabajo" con los valores iniciales:
- `m0 = m`: Se guarda una copia del módulo original. Esto es vital porque al final necesitamos asegurar que el resultado sea positivo mediante `x1 % m0`.
- `x0, x1`: Representan los coeficientes que se van transformando. Empezamos con `x0 = 0` y `x1 = 1`.
- `valor_a, valor_m`: Son las variables que irán sufriendo las divisiones sucesivas.

### 2. El Ciclo de Transformación (`while`)

Esta es la parte que realiza las iteraciones. Su estructura es:
- **Cálculo de `q`**: Se usa `//` para obtener el cociente entero (cuántas veces cabe un número en el otro).
- **Uso de Temporales (`antiguo_a`, `antiguo_x0`)**: En programación, al asignar un valor nuevo (`valor_a = valor_m`), el valor anterior se pierde. El script usa variables temporales para "recordar" el valor previo y poder usarlo en la siguiente línea, tal como haces al escribir en papel.
- **Actualización de Euclides**: 
  - El nuevo `valor_a` es el antiguo divisor.
  - El nuevo `valor_m` es el residuo de la división.
- **Actualización de Coeficientes**:
  - `x0` se calcula con la fórmula: `x1 - (q * x0)`.
  - `x1` toma el valor que tenía `x0` antes de ser actualizado.


### 3. Verificación y Salida
- **Condición de Existencia**: Si al terminar el ciclo `valor_a` no es igual a **1**, significa que el Máximo Común Divisor no es 1, por lo tanto, el inverso modular no existe.
- **Ajuste Final**: El valor de `x1` puede resultar negativo durante las restas.

- La modificación de los valores ocurre exclusivamente dentro del bloque `while`. Aquí es donde la "magia" sucede en tres líneas clave:

1.  **Actualización de Residuos (`valor_a`, `valor_m`):**
    ```python
    valor_a = valor_m
    valor_m = antiguo_a % valor_m
    ```
    Aquí es donde el algoritmo "avanza". El divisor se convierte en el nuevo dividendo y el residuo en el nuevo divisor. Si no hiciéramos esto, el programa se quedaría trabado en un bucle infinito.

2.  **Cálculo del Coeficiente (`x0`):**
    ```python
    x0 = x1 - q * antiguo_x0
    ```
    Esta es la línea más importante. Aquí es donde se calcula el valor que eventualmente será el inverso. Se resta el producto del cociente actual por el `x` anterior.

3.  **El Ajuste Final (Fuera del bucle):**
    ```python
    return x1 % m0
    ```
    Aquí se modifica el resultado por última vez. Si `x1` es negativo, el operador `%` de Python lo convierte automáticamente al rango positivo del módulo (por ejemplo, convierte un `-7` en un `4` si el módulo es `11`).

## (La Lógica)

Los números que ves en la terminal (como el `4` para `3 mod 11`) no son aleatorios; siguen la identidad establecida a verificar.

### El objetivo matemático
Buscamos que: `(a * x) + (m * y) = mcd(a, m)`.
Cuando el `mcd` es 1, ese valor `x` es nuestro inverso modular.

* **El cociente `q`**: Nos dice cuánta "distancia" hay entre los números en cada paso.
* **Los negativos en `x0`**: Es normal ver números como `-3` o `-11`. Eso significa que estamos restando múltiplos del módulo para acercarnos al `1`.
* **Por qué llegamos al 4**: Porque el algoritmo descubre que:
    `(-3 * 11) + (11 * 3)` no es... sino que la combinación lineal termina resultando en que `4 * 3 = 12`, y `12` es exactamente **1 unidad mayor** que el módulo `11`. Ese "1 de sobra" es lo que define al inverso modular.
