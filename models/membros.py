class Membros:
    def __init__(self, id, nome, idade, data_nascimento, telefone, rua, complemento, cidade, estado, codigo_postal, estado_civil, ministerio):
        self.id = int(id)  # Certifique-se de que o id é um inteiro
        self.nome = nome
        self.idade = idade
        self.data_nascimento = data_nascimento
        self.telefone = telefone
        self.rua = rua
        self.complemento = complemento
        self.cidade = cidade
        self.estado = estado
        self.codigo_postal = codigo_postal
        self.estado_civil = estado_civil
        self.ministerio = ministerio
