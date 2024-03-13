def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def dividir(a, b):
    return a / b

def multiplicar(a, b):
    return a * b

if __name__ == "__main__":
    opcion = input("¿Que operacion deseas hacer? Escribe Multiplicar, Dividir, Restar o Sumar dependiendo de cual sea ").lower()
    while opcion != "multiplicar" and opcion != "restar" and opcion != "sumar" and opcion != "dividir":
        opcion = input("Escribe Multiplicar, Dividir, Restar o Sumar dependiendo de cual sea ").lower()

    n1 = "a"
    while n1.isdigit() == False:
        n1 = input("Escribe el primer numero ")
    if n1.isdigit():
        n1 = int(n1)
        
    n2 = "b"
    while n2.isdigit() == False:
        n2 = input("Escribe el segundo numero ")
        if n2 == "0" and opcion == "dividir": 
            print("Error al intentar dividir entre 0")
            n2 = "b"
    if n2.isdigit():
        n2 = int(n2)


    if opcion == "multiplicar":  
        print(multiplicar(n1,n2))
    elif opcion == "sumar": 
        print(sumar(n1,n2))
    elif opcion == "restar":  
        print(restar(n1,n2))
    elif opcion == "dividir":  
        print(dividir(n1,n2))
