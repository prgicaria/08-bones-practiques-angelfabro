#!/usr/bin/env python
'''bones_practiques.py. Escriure un programa que faci una divisió

Institut Icària
Programació - 1r Batxillerat - Curs 2024-25
Escriure un programa que demani a l'usuari dos nombres enters: dividend i divisor. La sortida per pantalla ha de mostrar la divisió, el quocient i el residu.
'''
dividend = int(input("Introdueix el dividend"))
divisor = int(input("Introdueix el divisor"))
quocient = dividend // divisor
residu = dividend % divisor
print(f"Divisió: {dividend}/{divisor}")
print("Quocient:", quocient)
print("Residu: ", residu)