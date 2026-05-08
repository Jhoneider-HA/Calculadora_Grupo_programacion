# Calculadora basica terminal

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: No se puede dividir por cero"
    return a / b

def mostrar_menu():
    print("\n=== Calculadora Básica ===")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    print("==========================")

def pedir_numeros():
    a = float(input("Ingresa el primer número: "))
    b = float(input("Ingresa el segundo número: "))
    return a, b

def main():
    print("Bienvenido a la Calculadora Básica")

    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-5): ")

        if opcion == '5':
            print("Gracias por usar la calculadora. ¡Adiós!")
            break

        if opcion not in ['1', '2', '3', '4']:
            print("Opcion invalida. Intenta de nuevo.")
            continue

        a, b = pedir_numeros()

        if opcion == '1':
            resultado = sumar(a, b)
            operacion = "+"
        elif opcion == '2':
            resultado = restar(a, b)
            operacion = "-"
        elif opcion == '3':
            resultado = multiplicar(a, b)
            operacion = "*"
        elif opcion == '4':
            resultado = dividir(a, b)
            operacion = "/"

        print(f"\nResultado: {a} {operacion} {b} = {resultado}")

# Punto de entrada del programa 
if __name__ == "__main__":
    main()
