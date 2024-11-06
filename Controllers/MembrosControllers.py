import models.membros as membros
import services.database as db
import sys

# Adiciona o diretório raiz ao caminho do sistema
sys.path.append(r'C:\Users\mhele\Documents\VisualCode\PROJETO')


def incluir_membro(nome, idade, data_nascimento, telefone, rua, complemento, cidade, estado, codigo_postal, estado_civil, ministerio):
    cursor = None
    try:
        if db.conexao is None:
            raise ConnectionError("Falha na conexão com o banco de dados.")

        cursor = db.conexao.cursor()
        inserir_sql = """
        INSERT INTO membros (nome, idade, data_nascimento, telefone, rua, complemento, cidade, estado, codigo_postal, estado_civil, ministerio)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        valores = (nome, idade, data_nascimento, telefone, rua, complemento,
                   cidade, estado, codigo_postal, estado_civil, ministerio)
        print(f"Executando SQL: {inserir_sql} com valores {valores}")
        cursor.execute(inserir_sql, valores)
        db.conexao.commit()
        print("Membro inserido com sucesso!")
    except Exception as e:
        if db.conexao:
            db.conexao.rollback()
        print(f"Erro ao inserir membro: {e}")
    finally:
        if cursor:
            cursor.close()


def excluir_membro(id):
    cursor = None
    try:
        if not isinstance(id, int):
            raise ValueError("O valor do id deve ser um inteiro")

        if db.conexao is None:
            raise ConnectionError("Falha na conexão com o banco de dados.")

        cursor = db.conexao.cursor()
        excluir_sql = """DELETE FROM MEMBROS WHERE id = %s"""
        cursor.execute(excluir_sql, (id,))
        db.conexao.commit()
        print("Membro excluído com sucesso!")
    except Exception as e:
        if db.conexao:
            db.conexao.rollback()
        print(f"Erro ao excluir membro: {e}")
    finally:
        if cursor:
            cursor.close()


def selecionar_todos():
    cursor = None
    try:
        if db.conexao is None:
            raise ConnectionError("Falha na conexão com o banco de dados.")

        cursor = db.conexao.cursor()
        cursor.execute("SELECT * FROM MEMBROS")
        lista_membros = []
        for row in cursor.fetchall():
            lista_membros.append(membros.Membros(
                int(row[0]), row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11]
            ))
        return lista_membros
    except Exception as e:
        if db.conexao:
            db.conexao.rollback()
        print(f"Erro ao selecionar membros: {e}")
        return []
    finally:
        if cursor:
            cursor.close()


def selecionar_id(id):
    cursor = None
    try:
        if db.conexao is None:
            raise ConnectionError("Falha na conexão com o banco de dados.")

        cursor = db.conexao.cursor()
        cursor.execute("SELECT * FROM MEMBROS WHERE id = %s", (id,))
        row = cursor.fetchone()
        if row:
            membro = membros.Membros(
                int(row[0]), row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11]
            )
            return membro
        return None
    except Exception as e:
        if db.conexao:
            db.conexao.rollback()
        print(f"Erro ao selecionar membro: {e}")
        return None
    finally:
        if cursor:
            cursor.close()


def editar_membro(id, nome, idade, data_nascimento, telefone, rua, complemento, cidade, estado, codigo_postal, estado_civil, ministerio):
    cursor = None
    try:
        if db.conexao is None:
            raise ConnectionError("Falha na conexão com o banco de dados.")

        cursor = db.conexao.cursor()
        editar_sql = """
        UPDATE membros
        SET nome = %s, idade = %s, data_nascimento = %s, telefone = %s, rua = %s, complemento = %s, cidade = %s, estado = %s, codigo_postal = %s, estado_civil = %s, ministerio = %s
        WHERE id = %s
        """
        valores = (nome, idade, data_nascimento, telefone, rua, complemento,
                   cidade, estado, codigo_postal, estado_civil, ministerio, id)
        print(f"Executando SQL: {editar_sql} com valores {valores}")
        cursor.execute(editar_sql, valores)
        db.conexao.commit()
        print("Membro editado com sucesso!")
    except Exception as e:
        if db.conexao:
            db.conexao.rollback()
        print(f"Erro ao editar membro: {e}")
    finally:
        if cursor:
            cursor.close()
