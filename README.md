# Tarea 4.2 – Ejercicios de Programación  
**Materia:** Pruebas de Software y Calidad  
**Autor:** Ricardo Gómez  
**Actividad:** 4.2 Ejercicio de programación 1 

---

## 📌 Descripción general

Este repositorio contiene la solución a la **Tarea 4.2**, la cual consiste en **tres ejercicios de programación en Python**, enfocados en la correcta aplicación de:

- Estándares de codificación (**PEP 8**)
- Buenas prácticas de programación
- Manejo de errores
- Uso de análisis estático con **pylint**
- Evidencia de ejecución mediante casos de prueba

Cada problema fue implementado siguiendo estrictamente los requerimientos definidos en la actividad y verificado con los archivos de prueba proporcionados por el profesor.

---

## 📂 Estructura del repositorio

El repositorio está organizado por problema, siguiendo la estructura sugerida en clase:

```
P1/
├─ source/
├─ tests/
└─ results/

P2/
├─ source/
├─ tests/
└─ results/

P3/
├─ source/
├─ tests/
└─ results/
```

### Descripción de carpetas

- **source/**  
  Contiene el código fuente del programa correspondiente al problema.

- **tests/**  
  Incluye los archivos de entrada (TC1.txt, TC2.txt, etc.) utilizados como casos de prueba.

- **results/**  
  Contiene la evidencia de ejecuciones exitosas:
  - Archivos de salida generados por los programas.
  - Capturas de pantalla de la ejecución en consola.
  Además, contiene los resultados de referencia proporcionados por el profesor para fines de comparación.
  

---

## 🧪 Problemas implementados

### 🔹 Problema 1 – Compute Statistics (P1)
Programa que calcula estadísticas descriptivas a partir de un archivo con datos numéricos:

- Media
- Mediana
- Moda
- Desviación estándar poblacional
- Varianza poblacional

Resultados impresos en consola y guardados en `StatisticsResults.txt`.

---

### 🔹 Problema 2 – Converter (P2)
Programa que convierte números enteros a:
- Base binaria
- Base hexadecimal  

Las conversiones se realizan utilizando algoritmos básicos, sin funciones de conversión integradas (`bin`, `hex`, etc.).

Resultados impresos en consola y guardados en `ConvertionResults.txt`.

---

### 🔹 Problema 3 – Count Words (P3)
Programa que identifica:
- Todas las palabras distintas en un archivo de texto
- La frecuencia de aparición de cada palabra  

Incluye normalización básica de texto (minúsculas y eliminación de signos externos).

Resultados impresos en consola y guardados en `WordCountResults.txt`.

---

## ▶️ Ejecución de los programas

Cada programa se ejecuta desde la línea de comandos de la siguiente forma:

```bash
python nombre_programa.py archivo_de_prueba.txt