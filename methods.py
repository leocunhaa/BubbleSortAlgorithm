class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def __str__(self):
        return f"'{self.titulo}' by {self.autor} ({self.ano})"

class No:
    def __init__(self, dado=None):
        self.dado = dado
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.cabeca = None

    def adicionar(self, dado):
        novo_no = No(dado)
        if not self.cabeca:
            self.cabeca = novo_no
        else:
            atual = self.cabeca
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo_no

    def listar(self):
        atual = self.cabeca
        if not atual:
            print("O acervo está vazio.")
        while atual:
            print(atual.dado)
            atual = atual.proximo

def bubble_sort(lista, chave):
    trocou = True
    while trocou:
        trocou = False
        atual = lista.cabeca
        while atual and atual.proximo:
            proximo = atual.proximo
            if getattr(atual.dado, chave) > getattr(proximo.dado, chave):
                atual.dado, proximo.dado = proximo.dado, atual.dado
                trocou = True
            atual = atual.proximo

class NoArvore:
    def __init__(self, livro):
        self.livro = livro
        self.esquerda = None
        self.direita = None

class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None

    def adicionar(self, livro):
        novo_no = NoArvore(livro)
        if self.raiz is None:
            self.raiz = novo_no
        else:
            self._adicionar_recursivo(self.raiz, novo_no)

    def _adicionar_recursivo(self, no_atual, novo_no):
        if novo_no.livro.autor < no_atual.livro.autor:
            if no_atual.esquerda is None:
                no_atual.esquerda = novo_no
            else:
                self._adicionar_recursivo(no_atual.esquerda, novo_no)
        else:
            if no_atual.direita is None:
                no_atual.direita = novo_no
            else:
                self._adicionar_recursivo(no_atual.direita, novo_no)

    def listar_em_ordem(self):
        self._listar_em_ordem_recursivo(self.raiz)

    def _listar_em_ordem_recursivo(self, no_atual):
        if no_atual is not None:
            self._listar_em_ordem_recursivo(no_atual.esquerda)
            print(no_atual.livro)
            self._listar_em_ordem_recursivo(no_atual.direita)

    def buscar_por_autor(self, autor):
        return self._buscar_recursivo(self.raiz, autor)

    def _buscar_recursivo(self, no_atual, autor):
        if no_atual is None:
            return None
        if no_atual.livro.autor == autor:
            return no_atual.livro
        elif autor < no_atual.livro.autor:
            return self._buscar_recursivo(no_atual.esquerda, autor)
        else:
            return self._buscar_recursivo(no_atual.direita, autor)

    def recomendar_livros(self, autor):
        print(f"Recomendações baseadas no autor '{autor}':")
        self._recomendar_recursivo(self.raiz, autor)

    def _recomendar_recursivo(self, no_atual, autor):
        if no_atual is not None:
            self._recomendar_recursivo(no_atual.esquerda, autor)
            if autor in no_atual.livro.autor:
                print(no_atual.livro)
            self._recomendar_recursivo(no_atual.direita, autor)