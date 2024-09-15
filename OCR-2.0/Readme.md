# Modelo GOT OCR 2.0

## 1. Arquitectura Unificada End-to-End
GOT utiliza una arquitectura de **codificador-decodificador** que procesa imágenes ópticas de manera integral, eliminando la necesidad de pipelines modulares como en OCR-1.0. El codificador tiene **80 millones de parámetros** y reduce las imágenes de **1024x1024 píxeles** a **256x1024 tokens**. El decodificador tiene **500 millones de parámetros** y puede manejar secuencias de hasta **8000 tokens**, permitiendo el procesamiento de imágenes densas.

## 2. Entrenamiento en Múltiples Etapas
El entrenamiento del modelo se realiza en tres fases:
- **Primera etapa**: El codificador se entrena usando imágenes de escenas y documentos para reconocer texto en diversos formatos.
- **Segunda etapa**: El codificador y el decodificador se entrenan conjuntamente, incorporando tareas como el reconocimiento de partituras de música, fórmulas matemáticas y formas geométricas.
- **Tercera etapa**: Se mejora la generalización del modelo añadiendo características como el OCR de alta resolución, OCR multi-página y OCR fino a nivel de región.

## 3. Interactividad y OCR Dinámico
El modelo **GOT** permite realizar OCR interactivo. El usuario puede definir regiones específicas de la imagen para realizar el reconocimiento mediante **coordenadas o colores**. Además, soporta imágenes de alta resolución mediante **resolución dinámica** y puede procesar documentos de **múltiples páginas** sin bucles.

## 4. Versatilidad y Multitarea
**GOT OCR 2.0** es capaz de manejar una variedad de caracteres artificiales, más allá del texto plano, como:
- **Fórmulas**
- **Partituras musicales**
- **Gráficos y tablas**

El modelo utiliza herramientas como **LaTeX**, **Mathpix** y **Verovio** para generar formatos legibles como **Markdown** y **TikZ**.

## 5. Datos Sintéticos
Para mejorar su robustez, el modelo emplea **datos sintéticos**. Esto incluye datos de texto, manuscritos y contenido estructurado como tablas y fórmulas, ampliando su capacidad para manejar tareas complejas de OCR.

## 6. Comparación y Resultados
**GOT OCR 2.0** muestra un rendimiento superior en comparación con otros modelos de OCR y **LVLM** (Large Vision-Language Models) en tareas como:
- Reconocimiento de documentos densos
- OCR en escenas
- OCR con formato estructurado

El modelo, con **580 millones de parámetros**, combina eficiencia en el procesamiento de imágenes ópticas con la capacidad de generar resultados OCR estructurados y legibles, siendo adaptable a una amplia variedad de tareas y escenarios ópticos.
