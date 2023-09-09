import matplotlib.pyplot as plt

def main():
    print("Bienvenido al Laboratorio de Suma Acumulativa")
    
    # Paso 2: Solicitar la cantidad de números a sumar
    cantidad_numeros = int(input("Por favor, ingrese la cantidad de números a sumar: "))
    
    # Paso 3: Solicitar al usuario que ingrese los números
    numeros = []
    for i in range(cantidad_numeros):
        numero = float(input(f"Ingrese el número {i + 1}: "))
        numeros.append(numero)
    
    # Paso 4: Calcular la suma acumulativa
    suma_acumulativa = 0
    suma_acumulativa_lista = []
    for numero in numeros:
        suma_acumulativa += numero
        suma_acumulativa_lista.append(suma_acumulativa)
    
    # Paso 5: Mostrar la suma acumulativa como lista
    print("Suma acumulativa en forma de lista:")
    for i, acumulativa in enumerate(suma_acumulativa_lista):
        print(f"Número {i + 1}: {acumulativa}")
    
    # Paso 6: Crear un gráfico de barras
    plt.bar(range(1, cantidad_numeros + 1), suma_acumulativa_lista)
    plt.xlabel("Número de entrada")
    plt.ylabel("Suma acumulativa")
    plt.title("Gráfico de Suma Acumulativa")
    plt.show()

if __name__ == "__main__":
    main()
