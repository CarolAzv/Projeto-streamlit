
class Produto:
    def __init__(self, id,nome, descricao, preco, estoque,categoria_id):
        self.set_id(id)
        self.set_nome(nome)
        self.set_descricao(descricao)
        self.set_preco(preco)
        self.set_estoque(estoque)
        self.set_idCategoria(categoria_id)
    def set_id(self,id):
        self.__id = id
    def set_nome(self,nome):
        if nome == "":
            raise ValueError("Informe o nome")
        self.__nome = nome
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
    def get_nome(self):
        return self.__nome
    def get_descricao(self):
        return self.__descricao
    def get_preco(self):
        return self.__preco
    def get_estoque(self):
        return self.__estoque
    def get_id_categoria(self):
        return self.__id_categoria
    def __str__(self):
        return f"ID:{self.__id} - Nome:{self.__nome} - R$ {self.__preco:.2f} - Estoque: {self.__estoque}"
    def to_dict(self):
        return {"id": self.__id,"nome":self.__nome, "descricao": self.__descricao,"preco": self.__preco,"estoque": self.__estoque,"id_categoria": self.__id_categoria}
    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data.get('id', 0),
            nome=data.get('nome', ''),
            descricao=data.get('descricao', ''),
            preco=data.get('preco', 0.0),
            estoque=data.get('estoque', 0),
            categoria_id=data.get('id_categoria', 0) 
        )