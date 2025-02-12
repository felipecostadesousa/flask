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
    cursor.execute("SELECT id, nome, apelido, nacionalidade, imagem, contrato_inicio, data_nascimento FROM Arbitro;")
    arbitros = cursor.fetchall()
    cursor.close()
    conn.close()
    return arbitros
  except Exception as e:
    print("Erro ao buscar dados:", e)
    return []