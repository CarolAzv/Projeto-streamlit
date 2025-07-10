
class Categoria:
    def __init__(self, id, descricao):
        self.__id = id
        self.set_descricao(descricao)
    def set_id(self, id):
        self.__id = id
    def set_descricao(self, descricao):
        if descricao == "":
            raise ValueError("Informe a descrição")
        self.__descricao = descricao
    def get_id(self):
        return self.__id
    def get_descricao(self):
        return self.__descricao
    def to_dict(self):
        return {"id": self.__id, "descricao": self.__descricao}
    def __str__(self):
        return f"ID:{self.__id} - Descrição{self.__descricao}"
