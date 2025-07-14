import json
import os
from model.Entidades.Produto import Produto

class Produtos:
    objetos = []
    FILE_PATH = 'data/produtos.json'

    @classmethod
    def inserir(cls, obj: Produto):
        cls.abrir()
        m = max((x.get_id() for x in cls.objetos), default=0)
        obj.set_id(m + 1)
        cls.objetos.append(obj)
        cls.salvar()
        print(f"Produto '{obj.get_nome()}' inserido com ID {obj.get_id()}.")

    @classmethod
    def listar(cls) -> list[Produto]:
        cls.abrir()
        return list(cls.objetos)

    @classmethod
    def listar_id(cls, id: int) -> Produto | None:
        cls.abrir()
        for obj in cls.objetos:
            if obj.get_id() == id:
                return obj
        return None

    @classmethod
    def atualizar(cls, obj: Produto):
        cls.abrir()
        found = False
        for i, item in enumerate(cls.objetos):
            if item.get_id() == obj.get_id():
                cls.objetos[i] = obj
                found = True
                break
        if found:
            cls.salvar()
            print(f"Produto com ID {obj.get_id()} atualizado.")
        else:
            raise ValueError(f"Produto com ID {obj.get_id()} não encontrado para atualização.")

    @classmethod
    def excluir(cls, obj: Produto):
        cls.abrir()
        original_len = len(cls.objetos)
        cls.objetos = [item for item in cls.objetos if item.get_id() != obj.get_id()]
        if len(cls.objetos) < original_len:
            cls.salvar()
            print(f"Produto com ID {obj.get_id()} excluído.")
        else:
            raise ValueError(f"Produto com ID {obj.get_id()} não encontrado para exclusão.")

    @classmethod
    def abrir(cls):
        cls.objetos = []
        os.makedirs(os.path.dirname(cls.FILE_PATH), exist_ok=True)
        try:
            if os.path.exists(cls.FILE_PATH) and os.path.getsize(cls.FILE_PATH) > 0:
                with open(cls.FILE_PATH, "r", encoding='utf-8') as arquivo:
                    dados = json.load(arquivo)
                    for d in dados:
                        obj = Produto.from_dict(d)
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
        os.makedirs(os.path.dirname(cls.FILE_PATH), exist_ok=True)
        with open(cls.FILE_PATH, "w", encoding='utf-8') as arquivo:
            json.dump([obj.to_dict() for obj in cls.objetos], arquivo, indent=4, ensure_ascii=False)

    @classmethod
    def buscar_por_categoria(cls, categoria_id: int) -> list[Produto]:
        """
        Lista produtos de uma categoria específica.
        Este método é usado na página do cliente para filtrar produtos por categoria.
        """
        cls.abrir() 
        
        return [prod for prod in cls.objetos if prod.get_id_categoria() == categoria_id]
