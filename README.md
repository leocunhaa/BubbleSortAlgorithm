# Sistema de Gerenciamento de Acervo de Livro

Este projeto implementa um sistema simples de gerenciamento de acervo de livros com funcionalidades avançadas, como a recomendação de livros baseada em autores. Utilizamos uma **Árvore Binária de Busca (BST)** para organizar e otimizar operações de busca e recomendação de livros.

## Funcionalidades

O sistema oferece as seguintes funcionalidades:

1. **Adicionar Livro**: O usuário pode inserir novos livros no acervo informando o título, autor e ano de publicação.
2. **Listar Livros**: Exibe todos os livros do acervo em ordem alfabética por autor.
3. **Buscar Livro por Autor**: Permite buscar por livros de um autor específico.
4. **Recomendar Livros**: Recomenda livros baseados no autor informado, retornando também autores semelhantes.
5. **Sair**: Encerra o programa.

## Estrutura de Dados: Árvore Binária de Busca (BST)

A **Árvore Binária de Busca (BST)** é a estrutura principal do projeto, utilizada para armazenar os livros de forma ordenada com base no nome do autor. A BST permite a inserção, busca e recomendação de livros de maneira eficiente.

### Vantagens da BST:

- **Busca Eficiente**: Com uma complexidade média de **O(log n)**, a BST permite encontrar livros rapidamente, mesmo em coleções grandes.
- **Organização Natural**: Ao inserir os livros na árvore, eles são automaticamente organizados de forma ordenada, facilitando operações como listagem e recomendação.

### Implementação da BST

Cada nó da árvore armazena um objeto da classe `Livro`, que contém os seguintes atributos:
- **Título**: Nome do livro.
- **Autor**: Nome do autor.
- **Ano de publicação**: Ano de lançamento.

Os livros são inseridos na árvore seguindo a regra da BST: autores com nomes lexicograficamente menores são armazenados no lado esquerdo do nó, enquanto autores maiores ficam no lado direito.

## Algoritmo de Recomendação

A funcionalidade de recomendação é baseada na busca de livros de autores que correspondem ao termo fornecido pelo usuário. A recomendação inclui:

- **Livros do autor exato**: Quando o autor fornecido coincide totalmente com o nome de um autor na árvore.
- **Autores semelhantes**: Livros de autores cujo nome contém o termo fornecido (baseado em prefixos).

### Como Funciona:

1. O sistema percorre a árvore binária de forma recursiva.
2. Para cada nó, verifica se o nome do autor contém o termo de busca.
3. Se houver correspondência, o livro é recomendado.

### Exemplo de Recomendações:

- Se o usuário buscar por "John", o sistema pode recomendar livros de "John Smith", "John Doe" e "Johnny Appleseed".

## Estrutura da Classe Livro

A classe `Livro` encapsula os detalhes de cada livro:

```python
class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def __str__(self):
        return f"'{self.titulo}' by {self.autor} ({self.ano})"
