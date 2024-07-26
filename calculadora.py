def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero"

def main():
    print("Selecciona operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    while True:
        eleccion = input("Ingresa elección(1/2/3/4): ")

        if eleccion in ['1', '2', '3', '4']:
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))

            if eleccion == '1':
                print(f"{num1} + {num2} = {suma(num1, num2)}")

            elif eleccion == '2':
                print(f"{num1} - {num2} = {resta(num1, num2)}")

            elif eleccion == '3':
                print(f"{num1} * {num2} = {multiplicacion(num1, num2)}")

            elif eleccion == '4':
                print(f"{num1} / {num2} = {division(num1, num2)}")

            siguiente = input("¿Deseas realizar otra operación? (s/n): ")
            if siguiente.lower() != 's':
                break
        else:
            print("Entrada no válida")

if __name__ == "__main__":
    main()
