from unittest import TestCase
from persistence.db_produto import produtoDb
from model.models import Produtos



class Testprodutos(TestCase):
    def test_positivo_insere_produto(self):
        produto = Produtos(cod_produto=None,nome="refri_fanta", descricao="bebidas", preco=6.00)
        print(produto)
        produto_db = produtoDb()
        result = produto_db.insere_produto_db(produto)
        print(produto.cod_produto)
        self.assertEqual("Sucesso", result)


    def test_negativo_insere_produto(self):
       produto = Produtos(cod_produto=None,nome="refri", descricao="bebidas", preco=5.00)
       print(produto)
       produto_db = produtoDb()
       result = produto_db.insere_produto_db(produto)
       print(produto.cod_produto)
       self.assertEqual("Sucesso", result)


    def test_positivo_altera_produto(self):
        produto = Produtos(cod_produto=1,nome="refrigerante", descricao="bebidas", preco=5.50)
        print(produto)
        produto_db = produtoDb()
        result = produto_db.altera_produto_db(1, produto)
        self.assertEqual("Sucesso", result)


    def test_positivo_remove_produto(self):
       produto_db = produtoDb()
       result = produto_db.remove_produto_db(cod_produto=1)
       self.assertEqual("Sucesso", result)


    def test_positivo_busca_produto(self):
        produto_db = produtoDb()
        result = produto_db.busca_produto_db(cod_produto=2)
        print(result)
        self.assertIsNotNone(result)

    def test_positivo_busca_produtos(self):
        produto_db = produtoDb()
        result = produto_db.busca_produto_db(cod_produto=None)
        print(result)
        self.assertIsNotNone(result)