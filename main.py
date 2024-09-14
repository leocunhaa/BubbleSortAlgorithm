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

def interface():
    lista_livros = ListaEncadeada()
    while True:
        print("\n1. Adicionar livro")
        print("2. Listar livros")
        print("3. Ordenar por título")
        print("4. Ordenar por autor")
        print("5. Buscar livro")
        print("6. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            ano = input("Ano de publicação: ")
            livro = Livro(titulo, autor, ano)
            lista_livros.adicionar(livro)

        elif opcao == "2":
            lista_livros.listar()

        elif opcao == "3":
            bubble_sort(lista_livros, 'titulo')
            print("Acervo ordenado por título.")
            lista_livros.listar()  # Listar os livros após a ordenação

        elif opcao == "4":
            bubble_sort(lista_livros, 'autor')
            print("Acervo ordenado por autor.")
            lista_livros.listar()  # Listar os livros após a ordenação

        elif opcao == "5":
            termo = input("Digite o título ou autor para buscar: ").lower()
            atual = lista_livros.cabeca
            encontrado = False
            while atual:
                if termo in atual.dado.titulo.lower() or termo in atual.dado.autor.lower():
                    print(atual.dado)
                    encontrado = True
                atual = atual.proximo
            if not encontrado:
                print("Livro não encontrado.")

        elif opcao == "6":
            print("Saindo...")
            break

        else:
            print("Opção inválida.")

interface()