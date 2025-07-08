class VendaItem:
    def __init__(self, id, qtd, preco):
        self.__id = id       
        self.__qtd = qtd
        self.__preco = preco
        self.__id_venda = 0
        self.__id_produto = 0
    def set_id(self, id):
        self.__id = id
    def set_qtd(self, qtd):
        if qtd == 0.0: raise ValueError(f"Informe a quantidade")
        self.__qtd = qtd
    def set_preco(self, preco):
        if preco == 0.0: raise ValueError(f"Informe o preco")
        self.__preco = preco
    def set_id_venda(self, id_venda):
        self.__id_venda = id_venda
    def set_id_produto(self, id_produto):
        self.__id_produto = id_produto
    def get_id(self):
        return self.__id
    def get_qtd(self):
        return self.__qtd
    def get_preco(self):
        return self.__preco
    def get_id_venda(self):
        return self.__id_venda
    def get_id_produto(self):
        return self.__id_produto
    def __str__(self):
        return f"{self.__id} - {self.__qtd} - R$ {self.__preco:.2f}"