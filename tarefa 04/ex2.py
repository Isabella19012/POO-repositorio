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
        return f'nome: {self.__nome} | id: {self.__id} | descrição: {self.__descricao}'
class PlayListItem:
    def __init__(self, id, idPlayList, idMusica, sequencia):
        self.set_id(id)
        self.set_idPlayList(idPlayList)
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
    def get_idPlayList(self): return self.__idPlayList
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
    def __str__(self): 
        return f'id: {self.__id} | título: {self.__titulo} | artista: {self.__artista} | albúm: {self.__album}'
class UI:
    playlists = []
    musicas = []
    itens = []
    @staticmethod
    def main():
        op=0
        while op != 7:
            op=UI.menu()
            if op ==1: UI.inserir_playlist()
            if op ==2: UI.listar_playlist()
            if op ==3: UI.inserir_musica()
            if op ==4: UI.listar_musica()
            if op ==5: UI.inserir_item_playlist()
            if op ==6: UI.listar_item()

    @staticmethod
    def menu():
        print("\n1 - Inserir Playlist")
        print("2 - Listar Playlists")
        print("3 - Inserir Música")
        print("4 - Listar Músicas")
        print("5 - Inserir Item na Playlist")
        print("6 - Listar Itens")
        print("7 - Sair\n")
        return int(input('Escolha uma opção: '))
    @classmethod
    def inserir_playlist(o):
        id=int(input("Insira o ID: "))
        nome=input('Insira seu nome: ')
        descricao=input('Descreva a música: ')
        p=PlayList(id, nome, descricao)
        o.playlists.append(p)
        print('Dados inseridos com sucesso!')
    @classmethod
    def listar_playlist(po):
        if len(po.playlists) !=0:
            for x in po.playlists:
                print(x)
        else: print('Não há playlist registradas.')
    @classmethod
    def inserir_musica(o):
        id=int(input("Insira o ID: "))
        titulo=input('Insira o título da música: ')
        artista=input("Insira o artista da música: ")
        album= input('Insira o nome do albúm: ')
        m=Musica(id, titulo, artista, album)
        o.musicas.append(m)
        print('Dados inseridos com sucesso!')
    @classmethod
    def listar_musica(po):
        if len(po.musicas) !=0:
            for x in po.musicas:
                print(x)
        else: print('Não há músicas registradas.')
    @classmethod
    def inserir_item_playlist(o):
        id=int(input("Insira o ID: "))
        idPlayList=int(input('Insira o ID da playlist'))
        idMusica=int(input('Insira o ID da música: '))
        sequencia=int(input('Sequência da música'))
        pi=PlayListItem(id, idPlayList, idMusica, sequencia)
        o.itens.append(pi)
        print('Dados inseridos com sucesso!')
    @classmethod
    def listar_item(po):

        if len(po.itens) != 0:
            for item in po.itens:
                nome_musica = "Desconhecida"
                for m in po.musicas:
                    if m.get_id() == item.get_idMusica():
                        nome_musica = m.get_titulo()
                        break

                nome_playlist = "Desconhecida"
                for p in po.playlists:
                    if p.get_id() == item.get_idPlayList():
                        nome_playlist = p.get_nome()
                        break
                
                print(
                    f'Música "{nome_musica}" (ID {item.get_idMusica()}) '
                    f'faz parte da playlist "{nome_playlist}" '
                    f'(ID {item.get_idPlayList()}) '
                    f'- Sequência: {item.get_sequencia()}')        
        else: print('Não há itens registrados.')    
UI.main()