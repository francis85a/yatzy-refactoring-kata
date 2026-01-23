# Yatzy Refactoring - Documentación de Refactorizaciones

Este documento describe todas las refactorizaciones realizadas en el código del juego Yatzy, mejorando la legibilidad, mantenibilidad y eliminando código duplicado.

## 📋 Tabla de Refactorizaciones por Función

### [chance()](src/yatzy.py#L7-L8)

**Problemas que vimos:**
- **Long Parameter List (página 74)**: El código estaba atado a 5 argumentos específicos `(d1, d2, d3, d4, d5)`

**Refactorización:**
- Se cambió a `*dice` para aceptar cualquier número de dados
- Simplifica el cálculo: solo suma todos los dados

---

### [yatzy()](src/yatzy.py#L13-L18)

**Problemas que vimos:**
- **Long Parameter List (página 74)**: Eliminamos los parámetros nombrados `d1, d2, d3, d4, d5`
- **Duplicated Code (página 72)**: Se repetía la comparación para cada dado

**Refactorización:**
- Se utilizó `*dice` para recibir los dados
- Se implementó un bucle `for` simple para verificar si todos los dados tienen el mismo valor
- Retorna 50 puntos si coinciden, 0 en caso contrario

---

### [ones(), twos(), threes(), fours(), fives(), sixes()](src/yatzy.py#L20-L38)

**Problemas que vimos:**
- **Duplicated Code (página 72)**: La lógica de suma era idéntica en todas las funciones
- **Long Parameter List (página 74)**: Parámetros `(d1, d2, d3, d4, d5)` repetidos

**Refactorización:**
- Se eliminó la duplicación extrayendo la lógica a [Pips._sum_by_value()](src/pips.py#L28-L33)
- Todas las funciones ahora usan `*dice` como parámetro
- Cada función solo llama a `Pips._sum_by_value()` con el valor correspondiente

---

### [pair()](src/yatzy.py#L40-L46)

**Problemas que vimos:**
- **Long Parameter List (página 74)**: Parámetros nombrados específicos
- **Duplicated Code (página 72)**: Algoritmo de conteo repetido en otras funciones

**Refactorización:**
- Se utiliza `*dice` para recibir los dados
- Se extrajo la lógica a [Pips.find_n_of_a_kind()](src/pips.py#L44-L51) para buscar n-of-a-kind
- Retorna el valor más alto que aparece al menos 2 veces, multiplicado por 2

---

### [two_pairs()](src/yatzy.py#L48-L65)

**Problemas que vimos:**
- **Long Parameter List (página 74)**: Parámetros `d1-d5` específicos
- **Duplicated Code (página 72)**: Asignación manual de dados a lista de conteos
- **Mysterious Name (página 72)**: Variables con nombres poco claros como `n`
- **Loops (página 79)**: Estructura de recorrido innecesariamente compleja

**Refactorización:**
- Cambio a `*dice` para acepar cualquier número de dados
- Uso de [Pips.get_counts()](src/pips.py#L35-L40) para evitar duplicación del conteo
- Recorrido simplificado de 6 hacia 1 (usando `range(6, 0, -1)`)
- Nombres de variables mejorados: `pairs_count`, `total_points`
- Lógica clara: busca exactamente 2 pares y retorna su suma multiplicada por 2

---

### [three_of_a_kind()](src/yatzy.py#L67-L71)

**Problemas que vimos:**
- **Long Parameter List (página 74)**: Parámetros nombrados
- **Duplicated Code (página 72)**: Lógica de conteo repetida
- **Mysterious Name (página 72)**: Nombres de parámetros como `_1, _2`
- **Loops (página 79)**: Complejidad innecesaria

**Refactorización:**
- Se utiliza `*dice` para flexibilidad
- Se reutiliza [Pips.find_n_of_a_kind()](src/pips.py#L44-L51) con parámetro `n=3`
- Retorna el valor más alto que aparece al menos 3 veces, multiplicado por 3

---

### [four_of_a_kind()](src/yatzy.py#L73-L81)

**Problemas que vimos:**
- **Mysterious Name (página 72)**: Argumentos como `_1, _2` en versión anterior
- **Duplicated Code (página 72)**: Conteo de frecuencias repetido
- **Long Parameter List (página 74)**: Parámetros específicos

**Refactorización:**
- Cambio a `*dice` para recibir dados
- Reutiliza [Pips.find_n_of_a_kind()](src/pips.py#L44-L51) con parámetro `n=4`
- Retorna el valor más alto que aparece al menos 4 veces, multiplicado por 4

---

### [small_straight()](src/yatzy.py#L83-L91)

**Problemas que vimos:**
- **Long Parameter List (página 74)**: Parámetros `d1-d5`
- **Long Function / Complexity (página 73)**: Lógica innecesariamente compleja
- **Duplicated Code (página 72)**: Repetición de `tallies[d1-1] += 1`, etc.
- **Mysterious Name (página 72)**: Variable `tallies` poco clara

**Refactorización:**
- Uso de `*dice` para flexibilidad
- Simplificación con `sorted(dice)` para ordenar los dados
- Comparación directa con `[1, 2, 3, 4, 5]`
- Variable renombrada a `sorted_dice` (más clara)
- Retorna 15 puntos si es una escalera pequeña, 0 en caso contrario

---

### [large_straight()](src/yatzy.py#L93-L99)

**Problemas que vimos:**
- Mismos problemas que `small_straight()`

**Refactorización:**
- Mismo enfoque que `small_straight()`
- Comparación con `[2, 3, 4, 5, 6]`
- Retorna 20 puntos si es una escalera grande

---

### [full_house()](src/yatzy.py#L101-L124)

**Problemas que vimos:**
- **Mysterious Name (página 72)**: Variables como `floats` poco claras, `tallies` confuso
- **Long Parameter List (página 74)**: Parámetros `d1-d5`
- **Duplicated Code (página 72)**: Dos bucles `for` idénticos para buscar el 2 y el 3
- **Dead Code / Speculative Generality (página 80)**: Tenía `tallies = []` y luego `tallies = [0]*6`, el primero no se usaba

**Refactorización:**
- Uso de `*dice` para recibir dados
- Uso de [Pips.get_counts()](src/pips.py#L35-L40) para obtener frecuencias
- Un único bucle que detecta simultáneamente la pareja (2) y el trío (3)
- Nombres de variables mejorados: `has_pair`, `has_three`, `pair_value`, `three_value`
- Eliminación de código muerto (asignación inicial `tallies = []`)
- Retorna la suma: `pair_value * 2 + three_value * 3` si existe ambos, 0 en caso contrario

---

## 🔧 Funciones auxiliares que usamos

### [Pips.get_counts()](src/pips.py#L35-L40)

Función extraída para evitar duplicación del conteo de frecuencias en múltiples métodos.

**Descripción:**
- Recibe una lista de dados
- Retorna una lista de 6 elementos con la frecuencia de cada cara (1-6)

### [Pips.find_n_of_a_kind()](src/pips.py#L44-L51)

Función extraída para reutilización en `pair()`, `three_of_a_kind()` y `four_of_a_kind()`.

**Descripción:**
- Busca el valor de dado más alto que aparece al menos `n` veces
- Retorna el valor del dado (1-6) o 0 si no se encuentra
- Implementa búsqueda descendente para encontrar el valor máximo

---

## 📊 Resumen de Code Smells corregidos

| Code smell | Problemas | Soluciones |
|--------|-----------|-----------|
| **Long Parameter List** | 15 funciones | Cambio a `*dice` (argumentos variables) |
| **Duplicated Code** | Conteo de frecuencias, sumas | Extracción a `Pips.get_counts()`, `_sum_by_value()` |
| **Mysterious Names** | Variables confusas | Renombrado: `tallies`→`sorted_dice`, `n`→`pairs_count` |
| **Loops** | Complejidad innecesaria | Simplificación con funciones auxiliares |
| **Dead Code** | Asignaciones no usadas | Eliminación |


