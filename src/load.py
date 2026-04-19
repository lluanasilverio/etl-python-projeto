import sqlite3

def carregar_dados(df, caminho_banco):
    conn = sqlite3.connect(caminho_banco)
    df.to_sql("clientes_tratados", conn, if_exists="replace", index=False)
    conn.close()