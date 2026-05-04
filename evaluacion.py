import os

# Ejercicio 1 - Elisa Soto
'''Crear una función que reciba una lista de números enteros y genere una nueva
 lista solo con los números pares mayores a 10. Luego debe mostrar la nueva
 lista y la cantidad de elementos encontrados.'''

def numerosenteros(lista):
   encontrados = 0
   nueva = []
   for i in range(len(lista)):
       if lista[i] % 2 == 0 and lista[i] > 10:
            nueva.append(lista[i])
            encontrados += 1
   print(f"numeros pares mayores a 10: {nueva}")
   print(f"elementos encontrados: {encontrados}")

def recibir():
  cantidad = int(input("Cantidad de numeros que vas a usar: "))
  num = []
  for e in range(cantidad):
    n = int(input(f"Ingresa el numero {e + 1}: "))
    if n != " ":
            num.append(n)
  print(numerosenteros(num))

def limpiar_consola():
    os.system('cls')

continuar = True
while continuar: 
    print("\n- Ejercicios Python -")
    print("--- Ejercicio 1 ---")
    print("--- Ejercicio 2 ---")
    print("--- Ejercicio 3 ---")

    opcion = input("\n---Elije una opción: (1 - 3) (0 para salir): ")
    if opcion == "1":
        limpiar_consola()
        print("\nEjecutar ejercicio 1: ")
        recibir()
    elif opcion == "2":
        limpiar_consola()
        print("\nEjecutar ejercicio 2: ")
    elif opcion == "0":
        limpiar_consola()
        print("Saliendo...")
        continuar = False
    else:
        print("Opción no válido. Intenta otra vez.")