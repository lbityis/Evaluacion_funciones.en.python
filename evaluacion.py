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
    num.append(n)
  print(numerosenteros(num))

# Ejercicio 6 - Jonathan Alquinta
'''Crear una función que reciba una lista de edades y clasifique a las 
 personas en tres grupos: menores de edad, adultos y adultos mayores (60+).
 Debe mostrar la cantidad de personas en cada grupo.'''

def pedi_edades():
    edades = []
    n = int(input("¿Cuantas edades vas a ingresar?: "))
    for i in range(n):
        edad = int(input("Ingresar una edad: "))
        edades.append(edad)
    return edades

def calsificar_edades(edades):
    menor = 0
    Adulto = 0
    adultoMayor = 0
    for edad in edades:
        if edad < 18:
            menor += 1
        elif edad < 60:
            adultoMayor += 1
        else:
            Adulto += 1
    print(f"Menores: {menor}")
    print(f"Adulto Mayor: {adultoMayor}")
    print(f"Adultos: {Adulto}")

def limpiar_consola():
    os.system('cls')

continuar = True
while continuar: 
    print("\n- Ejercicios Python -")
    print("--- Ejercicio 1 ---")
    print("--- Ejercicio 2 ---")

    opcion = input("\n---Elije una opción: (1 o 2) (0 para salir): ")
    if opcion == "1":
        limpiar_consola()
        print("\nEjecutar ejercicio 1: ")
        recibir()
    elif opcion == "2":
        limpiar_consola()
        print("\nEjecutar ejercicio 2: ")
        lista = pedi_edades()
        calsificar_edades(lista)
    elif opcion == "0":
        limpiar_consola()
        print("Saliendo...")
        continuar = False
    else:
        print("Opción no válido. Intenta otra vez.")