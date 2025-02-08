import psycopg2

DB_CONFIG = {
  "dbname": "futebol",
  "user": "postgres",
  "password": "1234",
  "host": "localhost",
  "port": "5432"
}

def get_arbitros():
  try:
    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()
    cursor.execute("SELECT id, apelido, nome, data_nascimento, nacionalidade, imagemURL, contrato_inicio FROM Arbitro;")
    arbitros = cursor.fetchall()
    cursor.close()
    conn.close()
    return arbitros
  except Exception as e:
    print("Erro ao buscar dados:", e)
    return []