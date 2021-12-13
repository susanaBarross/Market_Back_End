from model.models import Cliente
from persistence.db_clientes import ClienteDb


class ClienteCtrl:

    def __init__(self):
        pass

    def insere_cliente(self, dcliente):
        cliente = Cliente(cod_cliente=None, nome=dcliente["nome"], sobrenome=dcliente["sobrenome"], cpf=dcliente["cpf"],
                          email=dcliente["email"], senha=dcliente["senha"], endereco=dcliente["endereco"],
                          telefone=dcliente["telefone"])

        cliente_db = ClienteDb()

        result = cliente_db.insere_cliente_db(cliente)

        return result

    def altera_cliente(self, cod_cliente, dcliente):
        cliente = Cliente(cod_cliente=None, nome=dcliente["nome"], sobrenome=dcliente["sobrenome"], cpf=dcliente["cpf"],email=None, senha=None,
                          endereco=dcliente["endereco"], telefone=dcliente["telefone"])

        cliente_db = ClienteDb()

        result = cliente_db.altera_cliente_db(cod_cliente, cliente)

        return result

    def remove_cliente(self, cod_cliente):
        cliente_db = ClienteDb()
        result = cliente_db.remove_cliente_db(cod_cliente)

        return result

    def busca_cliente(self, cod_cliente):
        cliente_db = ClienteDb()
        result = cliente_db.busca_cliente_db(cod_cliente)

        return result