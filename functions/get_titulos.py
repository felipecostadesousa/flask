import psycopg2

DB_CONFIG = {
  "dbname": "futebol",
  "user": "postgres",
  "password": "1234",
  "host": "localhost",
  "port": "5432"
}

def get_titulos():
  try:
    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome FROM Titulo;")
    titulos = cursor.fetchall()
    cursor.close()
    conn.close()
    return titulos
  except Exception as e:
    print("Erro ao buscar dados:", e)
    return []