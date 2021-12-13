import psycopg2
from persistence.db_connection import ConnectionDb
from model.models import Itens_Pedido


class Itens_PedidoDb:

    def __init__(self):
        pass

    def busca_itens_pedido_db(self, cod_pedido):
        try:
            lista_itens_pedido = []
            connection = ConnectionDb()
            conn = connection.connect()
            """ busca item do pedido ou itens do pedido """
            sql = """SELECT cod_pedido, cod_produto, Quantidade, valor_unitario FROM itens_pedido WHERE cod_pedido = COALESCE(%s, cod_pedido)"""

            cur = conn.cursor()
            cur.execute(sql, (cod_pedido, ))
            registros = cur.fetchone()
            while registros is not None:
                itens_pedido = Itens_Pedido(cod_pedido=registros[0],
                                  cod_produto=registros[1],
                                  quantidade=registros[2],
                                  valor_unitario=registros[3])

                lista_itens_pedido.append(itens_pedido.itens_pedido_dicionario())
                registros = cur.fetchone()

            cur.close()

            return lista_itens_pedido

        except (Exception, psycopg2.DatabaseError) as error:
            return error

        finally:
            if conn is not None:
                conn.close()



    def insere_itens_pedido_db(self, itens_pedido):
        try:

            connection = ConnectionDb()
            conn = connection.connect()
            """ insere o novo item do pedido """
            sql = """INSERT INTO itens_pedido(cod_pedido, cod_produto,Quantidade,valor_unitario) VALUES(%s, %s, %s, %s) returning cod_pedido;"""
            
            cur = conn.cursor()
            cur.execute(sql, (itens_pedido.cod_pedido, itens_pedido.cod_produto, itens_pedido.quantidade, itens_pedido.valor_unitario))
            itens_pedido.cod_pedido = cur.fetchone()[0]
            conn.commit()        
            cur.close()

            return "Sucesso"

        except (Exception, psycopg2.DatabaseError) as error:
            return error

        finally:
            if conn is not None:
                conn.close()


    def remove_itens_pedido_db(self, cod_pedido):
        try:

            connection = ConnectionDb()
            conn = connection.connect()
            """ remove o item do pedido """
            sql = """DELETE from itens_pedido WHERE cod_pedido=%s"""
            cur = conn.cursor()
            cur.execute(sql, (cod_pedido, ))
            conn.commit()
            cur.close()

            return "Sucesso"

        except (Exception, psycopg2.DatabaseError) as error:
            return error

        finally:
            if conn is not None:
                conn.close()

# so tera insert e delete