from datetime import datetime
class Entrega:
    def __init__(self,id,id_venda,id_entregador,valor_total,valor_frete,endereco,cliente,data_inicio,data_fim):
        self.__id = id
        self.set_id_venda(id_venda)
        self.set_id_entregador(id_entregador)
        self.set_valor_total(valor_total)
        self.set_valor_frete(valor_frete)
        self.set_endereco(endereco)
        self.set_nome_cliente(cliente)
        self.set_data_inicio(data_inicio)
        self.set_data_fim(data_fim) 
    def set_id(self,id): self.__id = id
    def set_id_venda(self,id): 
        if id <= 0:
            raise ValueError("ID da venda não pode ser negativo ou igual a 0")
        self.__id_venda = id
    def set_id_entregador(self,id):
        if id <= 0:
            raise ValueError("ID do entregador não pode ser negativo ou igual a 0")
        self.__id_entregador = id
    def set_valor_total(self,v):
        if v <= 0:
            raise ValueError("Valor total não pode ser 0 ou menor")
        self.__valor_total = v
    def set_valor_frete(self,v):
        if v <= 0:
            raise ValueError("Valor do frete não pode ser 0 ou menor")
        self.__valor_frete = v
    def set_endereco(self,e):
        self.__endereco = e
    def set_nome_cliente(self,e):
        self.__nome_cliente = e
    def set_data_inicio(self,i):
        if i == None:
            i = datetime.now()
        else:
            self.__data_inicio = i
        self.__data_inicio = i
    def set_data_fim(self,f): 
        self.__data_fim = f
    def get_id(self): return self.__id
    def get_id_entregador(self): return self.__id_entregador
    def get_valor_total(self): return self.__valor_total
    def get_valor_frete(self): return self.__valor_frete
    def get_endereco(self): return self.__endereco
    def get_nome_cliente(self): return self.__nome_cliente
    def get_data_inicio(self): return self.__data_inicio
    def get_data_fim(self): return self.__data_fim
    def __str__(self):
        return f"{self.__id} - {self.__id_venda} - {self.__id_entregador} - {self.__nome_cliente} - {self.__endereco} - {self.__valor_total} - {self.__valor_frete} - {self.__data_inicio} - {self.__data_fim}"
    def to_dict(self):
      return {"id":self.__id,"id_venda":self.__id_venda,"id_entregador":self.__id_entregador,"nome_cliente":self.__nome_cliente,"endereço":self.__endereco,"valor_total":self.__valor_total,"valor_frete":self.__valor_frete,"data_inicio":self.__data_inicio,"data_fim":self.__data_fim}
    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data['id'],
            id_venda=data['id_venda'],
            id_entregador=data['id_entregador'],
            valor_total=data['valor_total'],
            valor_frete=data['valor_frete'],
            endereco=data['endereco'],
            cliente=data['nome_cliente'], 
            data_inicio=data['data_inicio'],
            data_fim=data['data_fim']
        )