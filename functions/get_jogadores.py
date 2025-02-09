import psycopg2

DB_CONFIG = {
  "dbname": "futebol",
  "user": "postgres",
  "password": "1234",
  "host": "localhost",
  "port": "5432"
}

def get_jogadores():
  try:
    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, apelido, data_nascimento, nacionalidade, imagemURL, posicao, altura, pe_dominante, valor_mercado, cidade_nascimento, numero_camisa, agente, patrocinador, redes_sociais, contrato_incio, contrato_fim, id_time FROM Jogador;")
    jogadores = cursor.fetchall()
    cursor.close()
    conn.close()
    return jogadores
  except Exception as e:
    print("Erro ao buscar dados:", e)
    return []