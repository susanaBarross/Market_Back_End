from unittest import TestCase
from model.models import Cliente
from model.models import Pedido
from model.models import Itens_Pedido
import json

class TestCliente(TestCase):
    def test_cliente_dicionario(self):

        cliente = Cliente(cod_cliente=None, nome="test altera", sobrenome="test", cpf="test", email="test", senha="test", endereco="test", telefone="test")
        # transforma o dicionario em JSON
        print(json.dumps(cliente.cliente_dicionario()))

        self.assertEqual(1, 1)
        

class TestPedido(TestCase):
    def test_pedido_dicionario(self):

        pedido = Pedido(cod_pedido=None, data_pedido="test altera", valor="test", cod_cliente="como colocar aqui o cod_cliente - atualizar depois?")
        # transforma o dicionario em JSON
        print(json.dumps(pedido.pedido_dicionario()))

        self.assertEqual(1, 1)


class TestItens_Pedido(TestCase):
    def test_itens_pedido_dicionario(self):

        itens_pedido = Itens_Pedido(cod_pedido=None, item="test altera", cod_produto="test", quantidade="test", valor_produto='test', valor_total='test')
        # transforma o dicionario em JSON
        print(json.dumps(itens_pedido.itens_pedido_dicionario()))

        self.assertEqual(1, 1)
        