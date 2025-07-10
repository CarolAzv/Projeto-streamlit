# src/model/persistence/EntregaDAO.py
import json
import os
from src.model.Entidades.Entrega import Entrega # Importa sua classe Entrega

class Entregas:
    objetos = []

    FILE_PATH = 'data/entregas.json'

    @classmethod
    def inserir(cls, obj: Entrega):
        cls.abrir()
        m = max((x.get_id() for x in cls.objetos), default=0)
        obj.set_id(m + 1)
        cls.objetos.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls) -> list[Entrega]:
        cls.abrir()
        return cls.objetos

    @classmethod
    def listar_id(cls, id: int) -> Entrega | None:
        cls.abrir()
        for obj in cls.objetos:
            if obj.get_id() == id:
                return obj
        return None

    @classmethod
    def atualizar(cls, obj: Entrega):
        cls.abrir()
        found = False
        for i, item in enumerate(cls.objetos):
            if item.get_id() == obj.get_id():
                cls.objetos[i] = obj
                found = True
                break
        if found:
            cls.salvar()
        else:
            raise ValueError(f"Entrega com ID {obj.get_id()} não encontrada para atualização.")

    @classmethod
    def excluir(cls, obj: Entrega):
        cls.abrir()
        original_len = len(cls.objetos)
        cls.objetos = [item for item in cls.objetos if item.get_id() != obj.get_id()]
        if len(cls.objetos) < original_len:
            cls.salvar()
        else:
            raise ValueError(f"Entrega com ID {obj.get_id()} não encontrada para exclusão.")

    @classmethod
    def abrir(cls):
        cls.objetos = []
        os.makedirs(os.path.dirname(cls.FILE_PATH), exist_ok=True)
        try:
            if os.path.exists(cls.FILE_PATH) and os.path.getsize(cls.FILE_PATH) > 0:
                with open(cls.FILE_PATH, "r", encoding='utf-8') as arquivo:
                    dados = json.load(arquivo)
                    for d in dados:
                        obj = Entrega.from_dict(d)
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
        with open(cls.FILE_PATH, "w", encoding='utf-8') as arquivo:
            json.dump([obj.to_dict() for obj in cls.objetos], arquivo, indent=4, ensure_ascii=False)