# 📊 Projeto ETL com Python

## 🧠 Descrição

Este projeto implementa um pipeline ETL (Extração, Transformação e Carregamento) utilizando Python.

Os dados são extraídos de um arquivo CSV, tratados e padronizados, e posteriormente armazenados em um banco de dados SQLite.

---

## 🚀 Tecnologias utilizadas

- Python
- Pandas
- SQLite

---

## 📂 Estrutura do projeto
etl_projeto/
│
├── data/
│ └── clientes.csv
│
├── src/
│ ├── extract.py
│ ├── transform.py
│ ├── load.py
│ └── main.py
│
├── database/
│ └── banco.db
│
└── requirements.txt

---

## 🔄 Etapas do ETL

### 📥 Extração
Leitura dos dados a partir de um arquivo CSV.

### 🔄 Transformação
- Remoção de espaços extras
- Padronização de nomes (letras maiúsculas)
- Filtragem de clientes maiores de idade
- Padronização de cidades

### 📤 Carregamento
Armazenamento dos dados tratados em um banco de dados SQLite.

---

## ▶️ Como executar o projeto

1. Instale as dependências:
pip install pandas

2. Execute o pipeline:
python src/main.py

---

## 🗄️ Resultado

Os dados tratados são armazenados no banco:
database/banco.db

Tabela criada:
clientes_tratados

---

## 🎯 Objetivo

Demonstrar na prática a construção de um pipeline ETL utilizando Python, aplicando conceitos de manipulação de dados e persistência em banco de dados.

---

## 👩‍💻 Autora

Luana Silvério de Farias