while True:
    try: 
        number = int(input("Escriba un numero: "))
    except ValueError: # si se escribe texto o numero con coma (error de valor, ya que definimos la variable number como int)
        print("No es un entero, intente de nuevo")    
    else:
        if number%2 == 0:
            print("El numero", number, "es par")
        else:
            print("El numero", number, "es impar")
            continue #el bucle se sigue ejecutando, en cambio si ponemos "break" termina el programa