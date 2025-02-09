import psycopg2

DB_CONFIG = {
  "dbname": "futebol",
  "user": "postgres",
  "password": "1234",
  "host": "localhost",
  "port": "5432"
}

def get_estadios():
  try:
    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()
    cursor.execute("SELECT id, data_fundacao, nome, capacidade, id_localizacao FROM Estadio;")
    localizacoes = cursor.fetchall()
    cursor.close()
    conn.close()
    return localizacoes
  except Exception as e:
    print("Erro ao buscar dados:", e)
    return []