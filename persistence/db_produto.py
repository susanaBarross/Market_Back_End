import psycopg2
from persistence.db_connection import ConnectionDb
from model.models import Produtos


class produtoDb:

    def __init__(self):
        pass

    def busca_produto_db(self, cod_produto=None):
        try:
            lista_produto = []
            connection = ConnectionDb()
            conn = connection.connect()
            """ busca produto ou lista do produto """
            sql = """SELECT * FROM produtos WHERE cod_produto = COALESCE(%s, cod_produto)"""
            cur = conn.cursor()
            cur.execute(sql, (cod_produto,))
            registros = cur.fetchone()
            while registros is not None:
                produtos = Produtos(cod_produto=registros[0],
                                    nome=registros[1],
                                    descricao=registros[2],
                                    preco=registros[3])

                lista_produto.append(produtos.produto_dicionario())
                registros = cur.fetchone()

            cur.close()

            return lista_produto

        except (Exception, psycopg2.DatabaseError) as error:
            return error

        finally:
            if conn is not None:
                conn.close()

    def insere_produto_db(self, produto):
        try:

            connection = ConnectionDb()
            conn = connection.connect()
            """ insere o novo produto """
            sql = """INSERT INTO produtos(nome,descricao,preco) VALUES(%s, %s, %s) returning cod_produto;"""

            cur = conn.cursor()
            cur.execute(sql, (produto.nome, produto.descricao, produto.preco))
            produto.cod_produto = cur.fetchone()[0]
            conn.commit()
            cur.close()

            return "Sucesso"

        except (Exception, psycopg2.DatabaseError) as error:
            return error

        finally:
            if conn is not None:
                conn.close()

    def altera_produto_db(self, cod_produto, produto):
        try:

            connection = ConnectionDb()
            conn = connection.connect()
            """ altera o produto """
            sql = """UPDATE Produtos SET nome =%s,descricao=%s ,preco=%s WHERE cod_produto=%s"""

            cur = conn.cursor()
            cur.execute(sql, (produto.nome, produto.descricao, produto.preco, cod_produto))
            conn.commit()
            cur.close()

            return "Sucesso"

        except (Exception, psycopg2.DatabaseError) as error:
            return error

        finally:
            if conn is not None:
                conn.close()

    def remove_produto_db(self, cod_produto):
        try:

            connection = ConnectionDb()
            conn = connection.connect()
            """ remove o produto """
            sql = """DELETE from Produtos WHERE cod_produto=%s"""
            cur = conn.cursor()
            cur.execute(sql, (cod_produto,))
            conn.commit()
            cur.close()

            return "Sucesso"

        except (Exception, psycopg2.DatabaseError) as error:
            return error

        finally:
            if conn is not None:
                conn.close()