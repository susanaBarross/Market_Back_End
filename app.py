from flask import Flask, request
import flask
import simplejson as json
from controller.pedidos_controller import PedidosCtrl
from controller.clientes_controller import ClienteCtrl
from controller.controller_produto import produtoCtrl
from flask_cors import CORS


app = Flask(__name__)
app.debug = True
CORS(app)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route("/clientes", methods=['GET', 'POST'])
@app.route("/clientes/<cod_cliente>", methods=['DELETE', 'PUT', 'GET'])
def clientes(cod_cliente=None):
    result = ""

    if request.method == 'GET':
        cliente_ctrl = ClienteCtrl()
        result = cliente_ctrl.busca_cliente(cod_cliente=cod_cliente)
        flask.Response(status=200)
        return json.dumps(result)

    if request.method == 'PUT':

        dcliente = request.get_json(silent=True)
        cliente_ctrl = ClienteCtrl()
        result = cliente_ctrl.altera_cliente(cod_cliente, dcliente)
        if result == "Sucesso":
            flask.Response(status=200)
        else:
            flask.Response(status=400)

    if request.method == 'DELETE':

        cliente_ctrl = ClienteCtrl()
        result = cliente_ctrl.remove_cliente(cod_cliente=cod_cliente)
        if result == "Sucesso":
            flask.Response(status=200)
        else:
            flask.Response(status=400)

    if request.method == 'POST':

        dcliente = request.get_json(silent=True)
        cliente_ctrl = ClienteCtrl()
        result = cliente_ctrl.insere_cliente(dcliente)
        if result == "Sucesso":
            flask.Response(status=201)
        else:
            flask.Response(status=400)

    else:

        flask.Response(status=405)  # metodo não permitido

    return result


@app.route("/pedidos", methods=['GET', 'POST'])
@app.route("/pedidos/<cod_pedido>", methods=['DELETE', 'PUT', 'GET'])
def pedidos(cod_pedido=None):
    result = ""

    if request.method == 'GET':
        pedido_ctrl = PedidosCtrl()
        result = pedido_ctrl.busca_pedido(cod_pedido=cod_pedido)
        flask.Response(status=200)
        return json.dumps(result)

    if request.method == 'PUT':

        dpedido = request.get_json(silent=True)
        pedido_ctrl = PedidosCtrl()
        result = pedido_ctrl.altera_pedido(cod_pedido, dpedido)
        if result == "Sucesso":
            flask.Response(status=200)
        else:
            flask.Response(status=400)

    if request.method == 'DELETE':

        pedido_ctrl = PedidosCtrl()
        result = pedido_ctrl.remove_pedido(cod_pedido=cod_pedido)
        if result == "Sucesso":
            flask.Response(status=200)
        else:
            flask.Response(status=400)

    if request.method == 'POST':

        dpedido = request.get_json(silent=True)
        pedido_ctrl = PedidosCtrl()
        result = pedido_ctrl.insere_pedido(dpedido)
        if result == "Sucesso":
            flask.Response(status=201)
        else:
            flask.Response(status=400)

    else:

        flask.Response(status=405)  # metodo não permitido

    return result


@app.route("/produtos", methods=['GET', 'POST'])
@app.route("/produtos/<cod_produto>", methods=['DELETE', 'PUT', 'GET'])
def produtos(cod_produto=None):
    result = ""

    if request.method == 'GET':
        produto_ctrl=produtoCtrl()
        result = produto_ctrl.busca_produto(cod_produto=cod_produto)
        flask.Response(status=200)
        return json.dumps(result)

    if request.method == 'PUT':

        dprodutos=request.get_json(silent=True)
        produto_ctrl=produtoCtrl()
        result = produto_ctrl.altera_produto(cod_produto, dprodutos)
        if result == "Sucesso":
            flask.Response(status=200)
        else:
            flask.Response(status=400)

    if request.method == 'DELETE':

        produto_ctrl=produtoCtrl()
        result=produto_ctrl.remove_produto(cod_produto=cod_produto)
        if result == "Sucesso":
            flask.Response(status=200)
        else:
            flask.Response(status=400)

    if request.method == 'POST':

        dprodutos=request.get_json(silent=True)
        produto_ctrl=produtoCtrl()
        result = produto_ctrl.insere_produto(dprodutos)
        if result=="Sucesso":
            flask.Response(status=201)
        else:
            flask.Response(status=400)

    else:

        flask.Response(status=405)  # metodo não permitido

    return result


if __name__ == '__main__':
    app.run()

