class PlayList:
    def __init__(self, id, nome, descricao):
        self.set_id(id)
        self.set_nome(nome)
        self.set_descricao(descricao)
    def set_id(self,i):
        if i <=0: raise ValueError('Id negativo')
        else: self.__id=i
    def set_nome(self, i): self.__nome=i
    def set_descricao(self,i): self.__descricao=i
    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_descricao(self): return self.__descricao
    def __str__(self):
        return f'nome: {self.__nome} | id: {self.__id} | desc1rição: {self.__descricao}'
class PlayListItem:
    def __init__(self, id, idPlayList, idMusica, sequencia):
        self.set_id(id)
        self.set_nome(idPlayList)
        self.set_idMusica(idMusica)
        self.set_sequencia(sequencia)
    def set_id(self,i):
        if i <=0 or isinstance(i, str): raise ValueError('Id negativo ou é string')
        else: self.__id=i
    def set_idPlayList(self,i):
        if i <=0 or isinstance(i, str): raise ValueError('Id negativo ou é string')
        else: self.__idPlayList=i
    def set_idMusica(self,i):
        if i <=0 or isinstance(i, str): raise ValueError('Id negativo ou é string')
        else: self.__idMusica=i
    def set_sequencia(self,i):
        if i <=0 or isinstance(i, str): raise ValueError('sequencia negativo ou é string')
        else: self.__sequencia=i
    def get_id(self): return self.__id
    def get_idplayList(self): return self.__idPlayList
    def get_idMusica(self): return self.__idMusica
    def get_sequencia(self): return self.__sequencia
    def __str__(self):
        return f'ID: {self.__id} | ID da playlist: {self.__idPlayList} | ID da música: {self.__idMusica} | Sequência: {self.__sequencia}'
class Musica:
    def __init__(self, id, titulo, artista, album):
        self.set_id(id)
        self.set_titulo(titulo)
        self.set_artista(artista)
        self.set_album(album)
    def set_id(self,i):
        if i <=0 or isinstance(i, str): raise ValueError('Id negativo ou é string')
        else: self.__id=i
    def set_artista(self,i):
        self.__artista=i
    def set_titulo(self,i):
        self.__titulo=i
    def set_album(self,i):
        self.__album=i
    def get_id(self): return self.__id
    def get_titulo(self): return self.__titulo
    def get_artista(self): return self.__artista
    def get_album(self): return self.__album
class UI:
    @staticmethod
    def main():
        op=0
        if op != 5:
            pass
    def menu():
        print('nada ainda')
        return input('Escolha uma opção.')
UI.main()