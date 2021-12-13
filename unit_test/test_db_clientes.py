from unittest import TestCase
from persistence.db_clientes import ClienteDb
from model.models import Cliente


class TestClientes(TestCase):
    def test_positivo_insere_cliente(self):
        cliente = Cliente(cod_cliente=None,nome="test", sobrenome="test", cpf="test", email="test", senha="test", endereco="test", telefone="test")
        print(cliente)
        cliente_db = ClienteDb()
        result = cliente_db.insere_cliente_db(cliente)
        print(cliente.cod_cliente)
        self.assertEqual("Sucesso", result)


    def test_negativo_insere_cliente(self):
        cliente = Cliente(cod_cliente=None, nome="test", sobrenome="test", cpf="test", email="test", senha="test", endereco="test", telefone="test")
        print(cliente)
        cliente_db = ClienteDb()
        result = cliente_db.insere_cliente_db(cliente)
        print(cliente.cod_cliente)
        print(result)
        self.assertNotEqual("Sucesso", result)

    def test_positivo_altera_cliente(self):
        cliente = Cliente(cod_cliente=None, nome="test altera", sobrenome="test", cpf="test", email="test", senha="test", endereco="test", telefone="test")
        print(cliente)
        cliente_db = ClienteDb()
        result = cliente_db.altera_cliente_db(2, cliente)
        self.assertEqual("Sucesso", result)

    def test_positivo_remove_cliente(self):
        cliente_db = ClienteDb()
        result = cliente_db.remove_cliente_db(cod_cliente=7)
        self.assertEqual("Sucesso", result)


    def test_positivo_busca_cliente(self):
        cliente_db = ClienteDb()
        result = cliente_db.busca_cliente_db(cod_cliente=6)
        print(result)
        self.assertIsNotNone(result)