from unittest import TestCase
from controller.pedidos_controller import PedidosCtrl


class TestPedidoCtrl(TestCase):
    def test_insere_pedido(self):

        dpedido = {"data_pedido": "20/01/2021",
                   "valor": 10,
                   "cod_cliente": 1,
                   "itens_pedido": [{"cod_produto": 1, "quantidade": "1", "valor_unitario": 5},
                                    {"cod_produto": 2, "quantidade": "1", "valor_unitario": 5}]
                   }

        pedido_ctrl = PedidosCtrl()
        result = pedido_ctrl.insere_pedido(dpedido=dpedido)

        self.assertEqual(result, "Sucesso")

    def test_altera_pedido(self):

        dpedido = {"data_pedido": "20/01/2021",
                   "valor": 10,
                   "cod_cliente": 1,
                   "itens_pedido": [{"cod_produto": 1, "quantidade": "1", "valor_unitario": 5},
                                    {"cod_produto": 2, "quantidade": "1", "valor_unitario": 5}]
                   }

        pedido_ctrl = PedidosCtrl()
        result = pedido_ctrl.altera_pedido(cod_pedido=3, dpedido=dpedido)

        self.assertEqual(result, "Sucesso")

    def test_remove_pedido(self):
        pedido_ctrl = PedidosCtrl()
        result = pedido_ctrl.remove_pedido(cod_pedido=4)

        self.assertEqual(result, "Sucesso")

    def test_busca_pedidos(self):
        pedido_ctrl = PedidosCtrl()
        result = pedido_ctrl.busca_pedido(cod_pedido=None)
        print(result)

        self.assertIsNotNone(result)

    def test_busca_pedido_unico(self):
        pedido_ctrl = PedidosCtrl()
        result = pedido_ctrl.busca_pedido(cod_pedido=3)
        print(result)

        self.assertIsNotNone(result)