# Sesión 6 — Árboles de Decisión y Machine Learning

## Taller Analítico: El Algoritmo en Papel (20 min)

**Datos:** 6 clientes, 3 compraron un seguro y 3 no. La entropía inicial (50/50) es máxima: `Entropía = 1.0`.

**Pregunta A** (¿Es mayor de 30 años?): Izquierdo `[2 compraron, 2 no]` (n=4), Derecho `[1, 1]` (n=2).
**Pregunta B** (¿Tiene Auto?): Izquierdo `[3 compraron, 0 no]` (n=3), Derecho `[0, 3]` (n=3).

### Paso 1 — Ganancia de Información de la Pregunta A

Ambos grupos siguen 50/50 → entropía de cada grupo = 1.0.
Entropía ponderada = `(4/6)·1.0 + (2/6)·1.0 = 1.0`
**Ganancia = Entropía inicial − Entropía ponderada = 1.0 − 1.0 = 0** (no reduce el desorden en absoluto).

### Paso 2 — Ganancia de Información de la Pregunta B

Cada grupo queda puro (0% desorden) → entropía de cada grupo = 0.
Entropía ponderada = `(3/6)·0 + (3/6)·0 = 0`
**Ganancia = 1.0 − 0 = 1.0** (ganancia máxima, separación perfecta).

**Respuesta 1:** La **Pregunta B** ("¿Tiene Auto?") proporciona la mayor Ganancia de Información, porque separa a los clientes en dos grupos totalmente puros (entropía = 0), mientras que la Pregunta A no reduce el desorden en absoluto (ganancia = 0).

### Paso 3 — Regla lógica aprendida si el árbol elige la Pregunta B como raíz


SI Tiene_Auto = Sí  ENTONCES Compra_Seguro = Sí
SI Tiene_Auto = No  ENTONCES Compra_Seguro = No



## Taller de Laboratorio Final: El Experto Automático (45 min)

**Misión Práctica (Proyecto Integrador del Módulo 1):**

1. Instalar/importar `scikit-learn`.
2. Dataset simulado (arrays NumPy `X`, `Y`) para un departamento de Marketing. `X` con 3 columnas numéricas: `[Edad, Horas_Online, Compras_Previas]`. `Y` = 1 si hizo clic en el anuncio, 0 si lo ignoró (10 filas con un patrón lógico: personas jóvenes, muchas horas en línea y pocas compras previas tienden a hacer clic).
3. Entrenar el `DecisionTreeClassifier`.
4. Imprimir el árbol de texto con `export_text`.
5. **Discusión grupal:** las reglas (IF-THEN) que imprime la consola sí tienen sentido comercial (el patrón "joven + muchas horas online + pocas compras previas → clic" es coherente con el comportamiento típico de un usuario explorando ofertas). La IA es capaz de generar la Base de Conocimientos de un Sistema Experto **mucho más rápido** que un humano analizando miles de registros, pero sigue dependiendo de que el dataset sea representativo y de la validación de un experto de negocio para confirmar que las reglas encontradas tienen sentido causal y no son solo correlaciones espurias.

