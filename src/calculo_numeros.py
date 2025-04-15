from src.exceptions import ingrese_numero, NumeroDebeSerPositivo

if __name__ == "__main__":
    try:
        while True:
            try:
                numero = ingrese_numero()
                print(f"Número válido: {numero}")
            except NumeroDebeSerPositivo as e:
                print(f"Error: {e}")
            except ValueError as e:
                print(f"Error: {e}")
    except KeyboardInterrupt:
        print("\nPrograma terminado.")
