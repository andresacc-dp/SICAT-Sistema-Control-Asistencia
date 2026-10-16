# SICAT - Sistema Integral de Control de Asistencia y Tardanzas

Proyecto académico del curso **Fundamentos de Programación 1**.

**Autor:** [Jhefersson Huerta Valencia , Enoc John Ari Coronado Salvador , Andrés Humberto Arnao Ccarhuas]
**Docente:** [Lucas Fajardo Montes]
**Institución:** [Universidad Peruana de Ciencias Aplicadas]
**Año:** 2026

---
## 1. Introducción

El control de la asistencia del personal es una tarea frecuente en cualquier organización. Cuando se hace de forma manual, es fácil cometer errores al calcular las horas trabajadas, las tardanzas o el tiempo adicional laborado.

SICAT es un programa de consola desarrollado en Python que automatiza este proceso. Permite registrar trabajadores y sus asistencias diarias, y calcula de forma automática el tiempo trabajado, las tardanzas y el tiempo adicional, con validación de los datos ingresados.

## 2. Objetivos

### Objetivo general
Desarrollar un sistema de consola en Python que permita registrar y controlar la asistencia de trabajadores, calculando el tiempo trabajado, las tardanzas y el tiempo adicional.

### Objetivos específicos
- Registrar trabajadores con un código único y un nombre.
- Registrar asistencias diarias con horario programado, horario real y minutos de descanso.
- Validar los datos ingresados (formatos de fecha y hora, duplicados, rangos y coherencia).
- Calcular el tiempo trabajado, la tardanza y el tiempo adicional de cada jornada.
- Consultar asistencias por trabajador o de forma general.
- Generar un resumen general con totales acumulados.

## 3. Funcionalidades

| Opción | Función | Descripción |
|--------|---------|-------------|
| 1 | Registrar trabajador | Guarda código y nombre; no permite códigos repetidos |
| 2 | Registrar asistencia | Valida los datos y calcula tiempo trabajado, tardanza y adicional |
| 3 | Consultar asistencias | Muestra los registros de un trabajador o de todos |
| 4 | Resumen general | Muestra totales de tiempo, tardanzas y tiempo adicional |
| 5 | Salir | Termina el programa |

## 4. Reglas de cálculo

- **Tiempo trabajado** = salida real − ingreso real − descanso
- **Tiempo programado** = salida programada − ingreso programado − descanso
- **Tardanza** = ingreso real − ingreso programado (solo si llegó después de la hora)
- **Tiempo adicional** = tiempo trabajado − tiempo programado (solo si es positivo)

> El tiempo adicional no equivale automáticamente a horas extras pagables.

## 5. Estructuras y conceptos aplicados

- Estructuras secuenciales, condicionales (`if`, `elif`, `else`) y repetitivas (`for`, `while`).
- Listas para almacenar los datos en memoria.
- Funciones para dividir el programa en partes reutilizables.
- Validación de entradas del usuario.

## 6. Estructura del repositorio

```text
sicat/
├── sicat.py            Código fuente en Python
├── pseudocodigo.txt    Pseudocódigo del algoritmo
├── README.md           Presentación del proyecto
└── .gitignore
```

## 7. Alcance y limitaciones

- Los datos se guardan solo en memoria: al cerrar el programa se pierden.
- Solo se admiten jornadas que empiezan y terminan el mismo día.
- La validación de fechas comprueba día (1 a 31) y mes (1 a 12), pero no el número real de días de cada mes.

## 8. Control de versiones

Este proyecto usa **Git** y está alojado en **GitHub**. El historial de commits muestra la evolución del desarrollo.

```bash
git log --oneline
```
