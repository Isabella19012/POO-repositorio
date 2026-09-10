from models.Convenio import Convenio
import json
class ConvenioDAO:
    def __init__(self):
        self.__arquivo = 'convenios.json'
        self.__objetos = []
        self.__abrir()
    def inserir(self, obj):
        if len(self.__objetos) == 0:
            obj.set_id(1)
        else:
            maior = 0
            for convenio in self.__objetos:
                if convenio.get_id() > maior:
                    maior = convenio.get_id()
            obj.set_id(maior + 1)

        self.__objetos.append(obj)
        self.__salvar()
    def listar(self):
        return self.__objetos
    def atualizar(self, obj):
        aux = self.listar_id(obj.get_id())
        if aux != None:
            self.__objetos.remove(aux)
            self.__objetos.append(obj)
            self.__salvar()
    def excluir(self, id):
        aux= self.listar_id(id)
        if aux != None:
            self.__objetos.remove(aux)
            self.__salvar()
    def __abrir(self):
        try:
            arquivo = open(self.__arquivo, mode='r')
            list_dic=json.load(arquivo)
            arquivo.close()
            self.__objetos = []
            for dic in list_dic:
                obj=Convenio.from_json(dic)
                self.__objetos.append(obj)
        except FileNotFoundError:
            pass
    def __salvar(self):
        arquivo = open(self.__arquivo, mode='w')
        json.dump(self.__objetos, arquivo, default=Convenio.to_json, indent=2)
        arquivo.close()