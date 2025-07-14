from datetime import datetime
class Pedido:
    def __init__(self,id,cliente_id,data_pedido,status,valor_total,endereco,itens_pedidos,entregador_id,data_entrega):
        self.set_id(id)
        self.set_cliente_id(cliente_id)
        self.set_data_pedido(data_pedido)
        self.set_status(status)
        self.set_valor_total(valor_total)
        self.set_endereco(endereco)
        self.set_itens_pedidos(itens_pedidos)
        self.set_entregador_id(entregador_id)
        self.set_data_entrega(data_entrega)

    def set_id(self,id):
        self.__id = id
    def set_cliente_id(self,id):
        self.__cliente_id = id
    def set_data_pedido(self,d):
        self.__data_pedido = d
    def set_status(self,s):
        if s == "":
             raise ValueError("Informe o Status")
        self.__status = s
    def set_valor_total(self,v):
        if v <= 0:
             raise ValueError("Valor total não pode ser negativo ou zero")
        self.__valor_total = v
    def set_endereco(self,e):
        if e ==  "":
            raise ValueError("Informe o endereço!")
        self.__endereco = e
    def set_itens_pedidos(self,i):
        if i == "":
            raise ValueError("Informe os itens do pedido")
        self.__itens_pedidos = i
    def set_entregador_id(self,id):
        self.__entregador_id = id
    def set_data_entrega(self,d):
        if d == "":
            raise ValueError("A data de entrega não pode está vazia")
        self.__data_entrega = d
    def get_id(self):
        return self.__id
    def get_cliente_id(self):
        return self.__cliente_id
    def get_data_pedido(self):
        return self.__data_pedido
    def get_status(self):
        return self.__status
    def get_valor_total(self):
        return self.__valor_total
    def get_endereco(self):
        return self.__endereco
    def get_itens_pedidos(self):
        return self.__itens_pedidos
    def get_entregador_id(self):
        return self.__entregador_id
    def get_data_entrega(self):
        return self.__data_entrega
    
    def to_dict(self) -> dict:
        return {
            "id": self.__id,
            "cliente_id": self.__cliente_id,
            "data_pedido": self.__data_pedido.isoformat(), 
            "status": self.__status,
            "valor_total": self.__valor_total,
            "endereco": self.__endereco,
            "itens_pedido": self.__itens_pedidos, 
            "entregador_id": self.__entregador_id,
            "data_entrega": self.__data_entrega.isoformat() if self.__data_entrega else None,
        }

    @classmethod
    def from_dict(cls, data: dict):
       
        data_pedido = datetime.fromisoformat(data.get('data_pedido')) if data.get('data_pedido') else datetime.now()
        data_entrega = datetime.fromisoformat(data.get('data_entrega')) if data.get('data_entrega') else None

        return cls(
            id=data.get('id', 0),
            cliente_id=data.get('cliente_id', 0),
            data_pedido=data_pedido,
            status=data.get('status', ''),
            valor_total=data.get('valor_total', 0.0),
            endereco=data.get('endereco', ''),
            itens_pedidos=data.get('itens_pedidos', []),
            entregador_id=data.get('entregador_id'),
            data_entrega=data_entrega
        )