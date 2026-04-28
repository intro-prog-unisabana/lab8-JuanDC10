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
