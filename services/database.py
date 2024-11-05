import psycopg2

# Função para conectar ao banco de dados


def conectar_bd():
    try:
        conexao = psycopg2.connect(
            host="localhost",
            user="postgres",
            password="M@ximo19",
            port="6146",
            dbname="Church_Members"
        )
        print("Conexão ao banco de dados bem-sucedida!")
        return conexao
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None


# Estabelecer conexão e criar cursor
conexao = conectar_bd()
cursor = conexao.cursor() if conexao else None
