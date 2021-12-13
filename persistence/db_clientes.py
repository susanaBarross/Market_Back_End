import psycopg2
from persistence.db_connection import ConnectionDb
from model.models import Cliente


class ClienteDb:

    def __init__(self):
        pass

    def busca_cliente_db(self, cod_cliente=None):
        try:
            lista_clientes = []
            connection = ConnectionDb()
            conn = connection.connect()
            """ busca cliente ou lista de clientes """
            sql = """SELECT * FROM clientes WHERE cod_cliente = COALESCE(%s, cod_cliente)"""
            cur = conn.cursor()
            cur.execute(sql, (cod_cliente,))
            registros = cur.fetchone()
            while registros is not None:
                cliente = Cliente(cod_cliente=registros[0],
                                  nome=registros[1],
                                  sobrenome=registros[2],
                                  cpf=registros[3],
                                  email=registros[4],
                                  senha=None,
                                  endereco=registros[6],
                                  telefone=registros[7])

                lista_clientes.append(cliente.cliente_dicionario())
                registros = cur.fetchone()

            cur.close()

            return lista_clientes

        except (Exception, psycopg2.DatabaseError) as error:
            return error

        finally:
            if conn is not None:
                conn.close()

    def insere_cliente_db(self, cliente):
        try:

            connection = ConnectionDb()
            conn = connection.connect()
            """ insere o novo cliente """
            sql = """INSERT INTO clientes(Nome,Sobrenome,CPF,email,senha,endereco,telefone) VALUES(%s, %s, %s, %s, %s, %s, %s) returning cod_cliente;"""

            cur = conn.cursor()
            cur.execute(sql, (
            cliente.nome, cliente.sobrenome, cliente.cpf, cliente.email, cliente.senha, cliente.endereco,
            cliente.telefone))
            cliente.cod_cliente = cur.fetchone()[0]
            conn.commit()
            cur.close()

            return "Sucesso"

        except (Exception, psycopg2.DatabaseError) as error:
            return error

        finally:
            if conn is not None:
                conn.close()

    def altera_cliente_db(self, cod_cliente, cliente):
        try:

            connection = ConnectionDb()
            conn = connection.connect()
            """ altera o cliente """
            sql = """UPDATE clientes SET Nome =%s,Sobrenome=%s ,CPF=%s, endereco=%s, telefone=%s WHERE cod_cliente=%s"""

            cur = conn.cursor()
            cur.execute(sql,
                        (cliente.nome, cliente.sobrenome, cliente.cpf, cliente.endereco, cliente.telefone, cod_cliente))
            conn.commit()
            cur.close()

            return "Sucesso"

        except (Exception, psycopg2.DatabaseError) as error:
            return error

        finally:
            if conn is not None:
                conn.close()

    def remove_cliente_db(self, cod_cliente):
        try:

            connection = ConnectionDb()
            conn = connection.connect()
            """ remove o cliente """
            sql = """DELETE from clientes WHERE cod_cliente=%s"""
            cur = conn.cursor()
            cur.execute(sql, (cod_cliente,))
            conn.commit()
            cur.close()

            return "Sucesso"

        except (Exception, psycopg2.DatabaseError) as error:
            return error

        finally:
            if conn is not None:
                conn.close()