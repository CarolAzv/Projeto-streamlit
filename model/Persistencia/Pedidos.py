import json
import os
from model.Entidades.Pedido import Pedido # Importa a entidade Pedido

class Pedidos:
    objetos = []
    FILE_PATH = 'data/pedidos.json'

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        m = max((x.get_id() for x in cls.objetos), default=0)
        obj.set_id(m + 1)
        cls.objetos.append(obj)
        cls.salvar()
        print(f"Pedido com ID {obj.get_id()} inserido.")

    @classmethod
    def listar(cls) :
        """Lista todos os objetos Pedido."""
        cls.abrir()
        return list(cls.objetos)

    @classmethod
    def listar_id(cls, id) :
        """Busca um objeto Pedido pelo ID."""
        cls.abrir()
        for obj in cls.objetos:
            if obj.get_id() == id:
                return obj
        return None

    @classmethod
    def atualizar(cls, obj):
        """Atualiza um objeto Pedido existente."""
        cls.abrir()
        found = False
        for i, item in enumerate(cls.objetos):
            if item.get_id() == obj.get_id():
                cls.objetos[i] = obj
                found = True
                break
        if found:
            cls.salvar()
            print(f"Pedido com ID {obj.get_id()} atualizado.")
        else:
            raise ValueError(f"Pedido com ID {obj.get_id()} não encontrado para atualização.")

    @classmethod
    def excluir(cls, obj):
        """Exclui um objeto Pedido."""
        cls.abrir()
        original_len = len(cls.objetos)
        cls.objetos = [item for item in cls.objetos if item.get_id() != obj.get_id()]
        if len(cls.objetos) < original_len:
            cls.salvar()
            print(f"Pedido com ID {obj.get_id()} excluído.")
        else:
            raise ValueError(f"Pedido com ID {obj.get_id()} não encontrado para exclusão.")

    @classmethod
    def abrir(cls):
        """Abre o arquivo JSON e carrega os objetos Pedido."""
        cls.objetos = []
        os.makedirs(os.path.dirname(cls.FILE_PATH), exist_ok=True)
        try:
            if os.path.exists(cls.FILE_PATH) and os.path.getsize(cls.FILE_PATH) > 0:
                with open(cls.FILE_PATH, "r", encoding='utf-8') as arquivo:
                    dados = json.load(arquivo)
                    for d in dados:
                        obj = Pedido.from_dict(d) # Converte dicionário para objeto Pedido
                        cls.objetos.append(obj)
            else:
                with open(cls.FILE_PATH, 'w', encoding='utf-8') as f:
                    json.dump([], f, indent=4)
        except json.JSONDecodeError:
            cls.objetos = []
            print(f"Atenção: O arquivo '{cls.FILE_PATH}' está corrompido ou vazio. Inicializando com dados vazios.")
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        """Salva os objetos Pedido no arquivo JSON."""
        os.makedirs(os.path.dirname(cls.FILE_PATH), exist_ok=True)
        with open(cls.FILE_PATH, "w", encoding='utf-8') as arquivo:
            json.dump([obj.to_dict() for obj in cls.objetos], arquivo, indent=4, ensure_ascii=False)

    @classmethod
    def listar_pedidos_para_atribuicao(cls) -> list[Pedido]:

        cls.abrir() 
        return [
            p for p in cls.objetos
            if p.get_entregador_id() is None and p.get_status() in ["Pendente", "Em Preparacao", "Pronto para Entrega"]
        ]
