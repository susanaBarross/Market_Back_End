from model.models import Produtos
from persistence.db_produto import produtoDb


class produtoCtrl:

    def __init__(self):
        pass

    def insere_produto(self, dproduto):
        produto = Produtos(cod_produto=None, nome=dproduto["nome"], descricao=dproduto["descricao"], preco=dproduto["preco"])

        produto_db = produtoDb()

        result = produto_db.insere_produto_db(produto)

        return result

    def altera_produto(self, cod_produto, dproduto):
        produto = Produtos(cod_produto=None, nome=dproduto["nome"], descricao=dproduto["descricao"], preco=dproduto["preco"])

        produto_db = produtoDb()

        result = produto_db.altera_produto_db(cod_produto, produto)

        return result

    def remove_produto(self, cod_produto):
        produto_db = produtoDb()
        result = produto_db.remove_produto_db(cod_produto)

        return result

    def busca_produto(self, cod_produto):
        produto_db = produtoDb()
        result = produto_db.busca_produto_db(cod_produto)

        return result