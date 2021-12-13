from unittest import TestCase
from controller.clientes_controller import ClienteCtrl


class TestClienteCtrl(TestCase):
    def test_insere_cliente(self):

        dcliente = {"nome": "test",
                   "sobrenome": "ctrl",
                    "cpf": "12345",
                    "email": "test@email",
                    "senha": "12345",
                    "endereco": "rua test",
                    "telefone": "123456"}

        cliente_ctrl = ClienteCtrl()
        result = cliente_ctrl.insere_cliente(dcliente=dcliente)

        self.assertEqual(result, "Sucesso")

    def test_altera_cliente(self):

        dcliente = {"nome": "test altera",
                   "sobrenome": "ctrl",
                    "cpf": "12345",
                    "endereco": "rua test",
                    "telefone": "123456"}

        cliente_ctrl = ClienteCtrl()
        result = cliente_ctrl.altera_cliente(cod_cliente=2, dcliente=dcliente)

        self.assertEqual(result, "Sucesso")

    def test_remove_cliente(self):
        cliente_ctrl = ClienteCtrl()
        result = cliente_ctrl.remove_cliente(cod_cliente=2)

        self.assertEqual(result, "Sucesso")

    def test_busca_cliente(self):
        cliente_ctrl = ClienteCtrl()
        result = cliente_ctrl.busca_cliente(cod_cliente=1)
        print(result)

        self.assertIsNotNone(result)

    def test_busca_clientes(self):
        cliente_ctrl = ClienteCtrl()
        result = cliente_ctrl.busca_cliente(cod_cliente=None)
        print(result)

        self.assertIsNotNone(result)