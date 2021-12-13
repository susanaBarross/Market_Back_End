from unittest import TestCase
from persistence.db_pedidos import PedidoDb
from model.models import Pedido


class TestClientes(TestCase):
    def test_positivo_insere_pedido(self):
        pedido = Pedido(cod_pedido=None,data_pedido="test", valor=10, cod_cliente=1)
        print(pedido)
        pedido_db = PedidoDb()
        result = pedido_db.insere_pedido_db(pedido)
        print(pedido.cod_pedido)
        self.assertEqual("Sucesso", result)


    def test_negativo_insere_pedido(self):
        pedido = Pedido(cod_pedido=None, data_pedido="test", valor="test", cod_cliente="test - confirmar depois")
        print(pedido)
        pedido_db = PedidoDb()
        result = pedido_db.insere_pedido_db(pedido)
        print(pedido.cod_pedido)
        print(result)
        self.assertNotEqual("Sucesso", result)

    def test_positivo_altera_pedido(self):
        pedido = Pedido(cod_pedido=2, data_pedido="14/05/2021", valor=17, cod_cliente=1)
        print(pedido)
        pedido_db = PedidoDb()
        result = pedido_db.altera_pedido_db(pedido)
        self.assertEqual("Sucesso", result)


    def test_positivo_remove_pedido(self):
        pedido_db = PedidoDb()
        result = pedido_db.remove_pedido_db(cod_pedido=2)
        self.assertEqual("Sucesso", result)


    def test_positivo_busca_pedidos(self):
        pedido_db = PedidoDb()
        result = pedido_db.busca_pedido_db(cod_pedido=None)
        print(result)
        self.assertIsNotNone(result)

    def test_positivo_busca_pedido_unico(self):
        pedido_db = PedidoDb()
        result = pedido_db.busca_pedido_db(cod_pedido=3)
        print(result)
        self.assertIsNotNone(result)