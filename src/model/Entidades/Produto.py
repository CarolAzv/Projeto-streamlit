
class Produto:
    def __init__(self, id, descricao, preco, estoque):
        self.__id = id
        self.set_descricao(descricao)
        self.set_preco(preco)
        self.set_estoque(estoque)
        self.__id_categoria = 0
    def set_id(self,id):
        self.__id = id
    def set_descricao(self,d):
        if d == "": raise ValueError(f"Informe a descrição")
        self.__descricao = d
    def set_preco(self,p):
        if p == 0.0: raise ValueError(f"Informe o preco")
        self.__preco = p
    def set_estoque(self,e):
        if e <= 0: raise ValueError(f"Informe o estoque")
        self.__estoque = e
    def set_idCategoria(self,id):
        self.__id_categoria = id
    def get_id(self):
        return self.__id
    def get_descricao(self):
        return self.__descricao
    def get_preco(self):
        return self.__preco
    def get_estoque(self):
        return self.__estoque
    def __str__(self):
        return f"{self.__id} - {self.__descricao} - R$ {self.__preco:.2f} - estoque: {self.__estoque}"
    def to_dict(self):
        return {"id": self.__id,"descricao": self.__descricao,"preco": self.__preco,"estoque": self.__estoque,"id_categoria": self.__id_categoria}