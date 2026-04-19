from extract import extrair_dados
from transform import transformar_dados
from load import carregar_dados

def executar_pipeline():
    caminho_csv = "data/clientes.csv"
    caminho_banco = "database/banco.db"

    df = extrair_dados(caminho_csv)
    print("Dados extraídos:")
    print(df)

    df_tratado = transformar_dados(df)
    print("\nDados transformados:")
    print(df_tratado)

    carregar_dados(df_tratado, caminho_banco)
    print("\nDados carregados com sucesso!")

if __name__ == "__main__":
    executar_pipeline()