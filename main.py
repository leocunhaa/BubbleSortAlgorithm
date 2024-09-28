from methods import Livro, No, NoArvore, ListaEncadeada, ArvoreBinariaBusca

def interface():
    arvore_livros = ArvoreBinariaBusca()
    while True:
        print("\n1. Adicionar livro")
        print("2. Listar livros")
        print("3. Buscar livro por autor")
        print("4. Recomendar livros por autor")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            ano = input("Ano de publicação: ")
            livro = Livro(titulo, autor, ano)
            arvore_livros.adicionar(livro)

        elif opcao == "2":
            print("Listando todos os livros em ordem alfabética por autor:")
            arvore_livros.listar_em_ordem()

        elif opcao == "3":
            autor = input("Digite o nome do autor: ")
            livro = arvore_livros.buscar_por_autor(autor)
            if livro:
                print(livro)
            else:
                print(f"Nenhum livro encontrado para o autor '{autor}'.")

        elif opcao == "4":
            autor = input("Digite o nome do autor para recomendações: ")
            arvore_livros.recomendar_livros(autor)

        elif opcao == "5":
            print("Saindo...")
            break

        else:
            print("Opção inválida.")

interface()