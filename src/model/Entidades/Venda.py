from datetime import datetime

class Venda:
    def __init__(self, id):
        self.__id = id       
        self.__data = datetime.now()
        self.__carrinho = True
        self.__total = 0
        self.__id_cliente = 0
        self.__forma_pagamento = None
        self.__carrinho = True
    def set_id(self,id):
        self.__id = id
    def set_data(self,d):
        self.__data = d
    def set_total(self,t):
        self.__total = t
    def set_idCliente(self,id):
        self.__id_cliente = id
    def set_formaPagamento(self,f):
        self.__forma_pagamento = f
    def set_carrinho(self,b):
        self.__carrinho = b
    def get_id(self):
        return self.__id
    def get_data(self):
        return self.__data
    def get_total(self):
        return self.__total
    def get_idCliente(self):
        return self.__id_cliente
    def get_formapagamento(self):
        return self.__forma_pagamento
    def get_carrinho(self):
        return self.__carrinho
    
    def __str__(self):
        return f"{self.get_id()} - {self.get_data().strftime('%d/%m/%Y %H:%M')} - R$ {self.get_total():.2f}"

    def to_json(self):
        dic = {}
        dic["id"] = self.get_id()     
        dic["data"] = self.get_data().strftime("%d/%m/%Y %H:%M:%S")
        dic["carrinho"] = self.get_carrinho()
        dic["total"] = self.get_total()
        dic["id_cliente"] = self.get_idCliente()
        dic["Forma_Pagamento"] = self.get_formapagamento()
        return dic