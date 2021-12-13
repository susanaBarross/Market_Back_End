from unittest import TestCase
from controller.controller_produto import produtoCtrl


class TestprodutoCtrl(TestCase):
    def test_insere_produto(self):

        dproduto = {"nome": "SUCO",
                   "descricao": "Bebidas",
                    "preco": 1.25}

        produto_ctrl = produtoCtrl()
        result = produto_ctrl.insere_produto(dproduto=dproduto)

        self.assertEqual(result, "Sucesso")


    def test_altera_produto(self):

        dproduto = {"nome": "SUCO laranja",
                   "descricao": "bebidas",
                    "preco": 1.50}

        produto_ctrl = produtoCtrl()
        result = produto_ctrl.altera_produto(cod_produto=4, dproduto=dproduto)
        self.assertEqual(result, "Sucesso")

    def test_remove_produto(self):
        produto_ctrl = produtoCtrl()
        result =produto_ctrl.remove_produto(cod_produto=3)

        self.assertEqual(result, "Sucesso")

    def test_busca_produto(self):
        produto_ctrl = produtoCtrl()
        result = produto_ctrl.busca_produto(cod_produto=4)
        print(result)

        self.assertIsNotNone(result)

    def test_busca_produtos(self):
        produto_ctrl = produtoCtrl()
        result = produto_ctrl.busca_produto(cod_produto=None)
        print(result)

        self.assertIsNotNone(result)

