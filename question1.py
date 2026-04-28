"""Laboratorio 8 - Problema 1.

Implementa una CLI que calcule carga por punto de soporte.
"""

# TODO: Implementar según README.md
import sys

def calcular_carga(total_load, num_supports):
    return total_load / num_supports

def main():
    try:
        if len(sys.argv) != 3:
            raise ValueError
        total_load = float(sys.argv[1])
        num_supports = float(sys.argv[2])
if num_supports == 0:
            print("Error: Cannot divide by zero! Supports must be greater than zero.")
        else:
            resultado = calcular_carga(total_load, num_supports)
            print(f"Load per support point: {resultado:.2f} N")
    except ValueError:
        print("Error: Invalid input! Enter numeric values only.")
main()
f"{resultado:.2f}" 
