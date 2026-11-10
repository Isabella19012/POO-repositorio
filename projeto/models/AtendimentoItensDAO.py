from models.AtendimentoItens import AtendimentoItens
import json
from models.dao import DAO

class AtendimentoItensDAO(DAO):
    def __init__(self):
        super().__init__('atendimentoItens.json')
    def _abrir(self):
        try:
            arquivo = open(self._arquivo, mode='r')
            list_dic=json.load(arquivo)
            arquivo.close()
            self._objetos = []
            for dic in list_dic:
                obj=AtendimentoItens.from_json(dic)
                self.__objetos.append(obj)
        except FileNotFoundError:
            pass
    def _salvar(self):
        arquivo = open(self._arquivo, mode='w')
        json.dump(self._objetos, arquivo, default=AtendimentoItens.to_json, indent=2)
        arquivo.close()