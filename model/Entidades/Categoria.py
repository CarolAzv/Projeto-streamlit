class Categoria:
    def __init__(self, id,nome, descricao):
        self.__id = id
        self.set_nome(nome)
        self.set_descricao(descricao)
    def set_id(self, id):
        self.__id = id
    def set_nome(self,nome):
        if nome == "":
            raise ValueError("Informe o nome da categoria")
        self.__nome = nome
    def set_descricao(self, descricao):
        if descricao == "":
            raise ValueError("Informe a descrição")
        self.__descricao = descricao
    def get_id(self):
        return self.__id
    def get_nome(self):
        return self.__nome
    def get_descricao(self):
        return self.__descricao
    def to_dict(self):
        return {"id": self.__id,"nome":self.__nome, "descricao": self.__descricao}
        
    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data['id'],
            nome=data['nome'],
            descricao=data['descricao']
        )
    def __str__(self):
        return f"ID:{self.__id} - Nome{self.__nome} - Descrição{self.__descricao}"
