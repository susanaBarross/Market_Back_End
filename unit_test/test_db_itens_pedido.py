from unittest import TestCase
from persistence.db_itens_pedido import Itens_PedidoDb
from model.models import Itens_Pedido


class TestItens_Pedido(TestCase):
    def test_positivo_insere_itens_pedido(self):
        itens_pedido = Itens_Pedido(cod_pedido=1, cod_produto=1, quantidade=1, valor_unitario=28)
        print(itens_pedido)
        itens_pedido_db = Itens_PedidoDb()
        result = itens_pedido_db.insere_itens_pedido_db(itens_pedido)
        self.assertEqual("Sucesso", result)
        
        
    def test_negativo_insere_itens_pedido(self):
        itens_pedido = Itens_Pedido(cod_pedido=1, cod_produto="test", quantidade="test", valor_unitario=28)
        print(itens_pedido)
        itens_pedido_db = Itens_PedidoDb()
        result = itens_pedido_db.insere_itens_pedido_db(itens_pedido)
        print(result)
        self.assertNotEqual("Sucesso", result)


    def test_positivo_remove_itens_pedido(self):
        itens_pedido_db = Itens_PedidoDb()
        result = itens_pedido_db.remove_itens_pedido_db(cod_pedido=2)
        self.assertEqual("Sucesso", result)


    def test_positivo_busca_itens_pedido(self):
        itens_pedido_db = Itens_PedidoDb()
        result = itens_pedido_db.busca_itens_pedido_db(cod_pedido=3)
        print(result)
        self.assertIsNotNone(result)
