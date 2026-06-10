import os

DATABASE_USER = os.getenv("DATABASE_USER")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
API_TOKEN = os.getenv("API_TOKEN")

print("Iniciando aplicação...")

if DATABASE_USER:
    print("Usuário do banco carregado:", DATABASE_USER)

if DATABASE_PASSWORD:
    print("Senha do banco carregada: ***")

if API_TOKEN:
    print("Token da API carregado: ***")