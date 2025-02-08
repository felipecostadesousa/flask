import psycopg2

DB_CONFIG = {
  "dbname": "futebol",
  "user": "postgres",
  "password": "1234",
  "host": "localhost",
  "port": "5432"
}

def get_localizacoes():
  try:
    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()
    cursor.execute("SELECT id, pais, regiao, estado, cidade FROM Localizacao;")
    localizacoes = cursor.fetchall()
    cursor.close()
    conn.close()
    return localizacoes
  except Exception as e:
    print("Erro ao buscar dados:", e)
    return []