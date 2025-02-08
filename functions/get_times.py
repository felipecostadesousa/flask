import base64
import psycopg2
from datetime import date

DB_CONFIG = {
    "dbname": "futebol",
    "user": "postgres",
    "password": "1234",
    "host": "localhost",
    "port": "5432"
}

# Converte o campo BYTEA em Base64
def bytea_to_base64(bytea_data):
    if bytea_data:
        return f"data:image/png;base64,{base64.b64encode(bytea_data).decode('utf-8')}"
    return None

# Função para buscar os times do banco de dados
def get_times():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT id, imagem_escudo, nome, apelido, data_fundacao, site_time_url, quantidade_socios, quantidade_jogadores_selecao, valor_mercado
            FROM Time;
        """)
        rows = cursor.fetchall()
        cursor.close()
        conn.close()

        # Processa os resultados e converte a imagem para Base64
        times = []
        for row in rows:
            times.append({
                "id": row[0],
                "imagem_escudo": bytea_to_base64(row[1]),  # Converte o campo BYTEA
                "nome": row[2],
                "apelido": row[3],
                "data_fundacao": row[4],
                "site_time_url": row[5],
                "quantidade_socios": row[6],
                "quantidade_jogadores_selecao": row[7],
                "valor_mercado": row[8],
            })

        return times
    except Exception as e:
        print("Erro ao buscar dados:", e)
        return []
