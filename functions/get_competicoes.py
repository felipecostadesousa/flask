import psycopg2

DB_CONFIG = {
  "dbname": "futebol",
  "user": "postgres",
  "password": "1234",
  "host": "localhost",
  "port": "5432"
}

def get_competicoes():
  try:
    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, ano, confederacao, imagemURL, divisao FROM Competicao;")
    competicoes = cursor.fetchall()
    cursor.close()
    conn.close()
    return competicoes
  except Exception as e:
    print("Erro ao buscar dados:", e)
    return []