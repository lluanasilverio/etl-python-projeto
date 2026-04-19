def transformar_dados(df):
    df["nome"] = df["nome"].str.strip().str.upper()
    df = df[df["idade"] >= 18]
    df["cidade"] = df["cidade"].str.strip().str.title()
    return df