#!/usr/bin/env python
'''bones_practiques.py. Escriure un programa que faci
una divisió

Institut Icària
Programació - 1r Batxillerat - Curs 2024-25
Programa que demana a l'usuari dos nombres
enters: dividend i divisor.
La sortida per pantalla ha de mostrar la
divisió, el quocient i el residu.
'''
__author__ = "Ángel Fabro Francia"
__email__ = "afabro@instituticaria.cat"
__date__ = "24/10/2025"

dividend = int(input("Introdueix el dividend: "))
divisor = int(input("Introdueix el divisor: "))
quocient = dividend // divisor
residu = dividend % divisor
print(f"Divisió: {dividend}/{divisor}")
print(f"Quocient: {quocient}")
print(f"Residu:  {residu}")
