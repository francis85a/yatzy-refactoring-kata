# Refactorización de Yatzy 


- [chance](src/yatzy.py#L8)
  - Versión antigua: recibía cinco parámetros posicionales y sumaba manualmente cada uno.
  - Versión final: acepta `*dice` y usa `sum(dice)`.
  - Code smells solucionados: **Long Parameter List**, **Duplicated Code**.

- [yatzy](src/yatzy.py#L15)
  - Versión antigua: construía un array de conteo y buscaba un valor con contador == 5.
  - Versión final: acepta `*dice` y comprueba si `len(set(dice)) == 1`; devuelve la constante de puntuación.
  - Code smells solucionados: **Long Parameter List**, **Long Function / Complexity**.
  - Versión antigua: construía un array de conteo y buscaba un valor con contador == 5.
  - Versión final: acepta `*dice` y comprueba si `len(set(dice)) == 1`; devuelve la constante de puntuación.
  - Code smells solucionados: **Long Parameter List**, **Long Function / Complexity**.


- [ones / twos / threes / fours / fives / sixes](src/yatzy.py#L26-L53)
  - Versión antigua: cada función contenía bloques repetidos que comprobaban cada parámetro individual.
  - Versión final: delegan en una utilidad `_sum_by_value(dice, value)` y usan `*dice`.
  - Code smells solucionados: **Duplicated Code**, **Long Parameter List**, **Primitive Obsession** (uso de parámetros posicionales en lugar de colecciones).


- [pair](src/yatzy.py#L60)
  - Versión antigua: conteo manual sobre cinco parámetros y búsqueda del par mayor con bucles.
  - Versión final: reutiliza la utilidad `find_n_of_a_kind(dice, 2)` y multiplica por 2.
  - Code smells solucionados: **Long Parameter List**, **Duplicated Code**, **Mysterious Name** (se renombró a `pair`).

- [two_pairs](src/yatzy.py#L71)
  - Versión antigua: sumaba ocurrencias manualmente en una lista de 6 y usaba variables poco descriptivas.
  - Versión final: obtiene frecuencias con `get_counts(dice)`, recorre de mayor a menor y usa nombres claros (`pairs_count`, `total_points`).
  - Code smells solucionados: **Long Parameter List**, **Duplicated Code**, **Mysterious Name**, **Loops / Complexity**.

- [three_of_a_kind / four_of_a_kind](src/yatzy.py#L93-L105)
  - Versión antigua: conteos manuales y bucles para detectar >= 3 o >= 4.
  - Versión final: usan `find_n_of_a_kind(dice, n)` y multiplican por `n`.
  - Code smells solucionados: **Long Parameter List**, **Duplicated Code**, **Loops / Complexity**.

- [small_straight / large_straight](src/yatzy.py#L112-L133)
  - Versión antigua: construían `tallies` manualmente y comprobaban posiciones concretas.
  - Versión final: simplificadas (uso de `sorted()` o comparación por conjuntos y utilidades del enum) y devuelven constantes (15/20).
  - Code smells solucionados: **Long Parameter List**, **Long Function / Complexity**, **Duplicated Code**, **Mysterious Name** (nomenclatura inconsistente con snake_case).

- [full_house](src/yatzy.py#L136)
  - Versión antigua: dos bucles separados para detectar un `2` y un `3`, variables con nombres poco claros y código muerto (inicializaciones innecesarias).
  - Versión final: usa `get_counts(dice)`, detecta `2` y `3` en la misma estructura, obtiene índices y calcula la puntuación directamente.
  - Code smells solucionados: **Mysterious Name**, **Duplicated Code**, **Dead Code** (inicializaciones no usadas), **Long Function / Complexity**.

---

## 🧰 Utilidades y métodos

- **_sum_by_value(dice, value)**
  - Versión antigua: la lógica de suma estaba replicada en múltiples funciones.
  - Versión final: función dedicada que suma todas las caras iguales a `value`.

- **get_counts(dice)**
  - Versión antigua: (en su forma temprana) iteraba y acumulaba en una lista de frecuencias mediante un bucle manual.
  - Versión final: implementada con una comprehension `[dice.count(v) for v in values()]` (más declarativa y compacta).

- **find_n_of_a_kind(dice, n)**
  - Versión antigua: cada función que necesitaba detectar n-of-a-kind repetía el conteo y la búsqueda.
  - Versión final: utilidad central que usa `get_counts` y busca de mayor a menor el valor con frecuencia >= `n`.










