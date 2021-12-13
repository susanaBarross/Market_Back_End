from model.models import Pedido, Itens_Pedido
from persistence.db_pedidos import PedidoDb
from persistence.db_itens_pedido import Itens_PedidoDb

class PedidosCtrl:

    def __init__(self):
        pass

    def insere_pedido(self, dpedido):
        pedido = Pedido(cod_pedido=None, data_pedido=dpedido["data_pedido"], valor = dpedido["valor"], cod_cliente = dpedido["cod_cliente"])

        pedido_db = PedidoDb()

        result = pedido_db.insere_pedido_db(pedido)

        for item in dpedido["itens_pedido"]:

            itens_pedido = Itens_Pedido(cod_pedido=pedido.cod_pedido, cod_produto=item["cod_produto"], quantidade=item["quantidade"],
                                        valor_unitario=item["valor_unitario"])

            itens_pedido_db = Itens_PedidoDb()

            result = itens_pedido_db.insere_itens_pedido_db(itens_pedido)

        return result


    def altera_pedido(self, cod_pedido, dpedido):
        pedido = Pedido(cod_pedido=cod_pedido, data_pedido = dpedido["data_pedido"], valor = dpedido["valor"], cod_cliente = dpedido[
            "cod_cliente"])

        pedido_db = PedidoDb()

        result = pedido_db.altera_pedido_db(pedido)

        itens_pedido_db = Itens_PedidoDb()

        result_item = itens_pedido_db.remove_itens_pedido_db(cod_pedido)

        for item in dpedido["itens_pedido"]:

            itens_pedido = Itens_Pedido(cod_pedido=pedido.cod_pedido, cod_produto=item["cod_produto"], quantidade=item["quantidade"],
                                        valor_unitario=item["valor_unitario"])

            itens_pedido_db = Itens_PedidoDb()

            result = itens_pedido_db.insere_itens_pedido_db(itens_pedido)

        return result


    def remove_pedido(self, cod_pedido):

        itens_pedido_db = Itens_PedidoDb()

        result_item = itens_pedido_db.remove_itens_pedido_db(cod_pedido)

        pedido_db = PedidoDb()

        result = pedido_db.remove_pedido_db(cod_pedido)

        return result


    def busca_pedido(self, cod_pedido):

        pedido_db = PedidoDb()

        result = pedido_db.busca_pedido_db(cod_pedido)

        itens_pedido_db = Itens_PedidoDb()

        for i, pedido in enumerate(result):

            itens = itens_pedido_db.busca_itens_pedido_db(pedido["cod_pedido"])
            result[i]["itens_pedido"] = itens

        return result

