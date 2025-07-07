from app import analyzer, api_client

def main():
    print("Ejecutando análisis externo...")
    code, output = analyzer.run_analysis([])
    print(f"Resultado del binario: código={code}, salida='{output.strip()}'")

    print("Consultando API externa...")
    data = api_client.fetch_data()
    print(f"Respuesta de la API: {data}")

if __name__ == "__main__":
    main()
