from src.exceptions import NumeroDebeSerPositivo

def ingrese_numero():
    entrada = input("Ingrese un número: ")
    try:
        numero = int(entrada)
    except ValueError:
        raise ValueError("La entrada debe ser un número válido")

    if numero < 0:
        raise NumeroDebeSerPositivo("El número debe ser positivo")

    return numero

if __name__ == "__main__":
    while True:
        try:
            numero = ingrese_numero()
            print(f"Número válido: {numero}")
        except NumeroDebeSerPositivo as e:
            print(f"Error: {e}")
        except ValueError as e:
            print(f"Error: {e}")
        except KeyboardInterrupt:
            print("\nPrograma terminado por el usuario.")
            break
