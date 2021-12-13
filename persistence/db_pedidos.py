import psycopg2
from persistence.db_connection import ConnectionDb
from model.models import Pedido


class PedidoDb:

    def __init__(self):
        pass

    def busca_pedido_db(self, cod_pedido):
        try:
            lista_pedidos = []
            connection = ConnectionDb()
            conn = connection.connect()
            """ busca pedido ou lista de pedidos """
            sql = """SELECT * FROM Pedidos WHERE cod_pedido = COALESCE(%s, cod_pedido)"""
            cur = conn.cursor()
            cur.execute(sql, (cod_pedido, ))
            registros = cur.fetchone()
            while registros is not None:
                pedido = Pedido(cod_pedido=registros[0],
                                  data_pedido=registros[1],
                                  valor=registros[2],
                                  cod_cliente=registros[3])

                lista_pedidos.append(pedido.pedido_dicionario())
                registros = cur.fetchone()

            cur.close()

            return lista_pedidos

        except (Exception, psycopg2.DatabaseError) as error:
            return error

        finally:
            if conn is not None:
                conn.close()


    def insere_pedido_db(self, pedido):
        try:

            connection = ConnectionDb()
            conn = connection.connect()
            """ insere o novo pedido """
            sql = """INSERT INTO Pedidos(data_pedido,valor,cod_cliente) VALUES(%s, %s, %s) returning cod_pedido;"""
            
            cur = conn.cursor()
            cur.execute(sql, (pedido.data_pedido, pedido.valor, pedido.cod_cliente))
            pedido.cod_pedido = cur.fetchone()[0]
            conn.commit()        
            cur.close()

            return "Sucesso"

        except (Exception, psycopg2.DatabaseError) as error:
            return error

        finally:
            if conn is not None:
                conn.close()


    def altera_pedido_db(self, pedido):
        try:

            connection = ConnectionDb()
            conn = connection.connect()
            """ altera o pedido """
            sql = """UPDATE Pedidos SET data_pedido =%s, valor=%s, cod_cliente=%s WHERE cod_pedido=%s"""

            cur = conn.cursor()
            cur.execute(sql, (pedido.data_pedido, pedido.valor, pedido.cod_cliente, pedido.cod_pedido))
            conn.commit()
            cur.close()

            return "Sucesso"

        except (Exception, psycopg2.DatabaseError) as error:
            return error

        finally:
            if conn is not None:
                conn.close()



    def remove_pedido_db(self, cod_pedido):
        try:

            connection = ConnectionDb()
            conn = connection.connect()
            """ remove o pedido """
            sql = """DELETE from Pedidos WHERE cod_pedido=%s"""
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
























