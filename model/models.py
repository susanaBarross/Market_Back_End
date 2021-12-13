# classe cliente
class Cliente:
    def __init__(self, cod_cliente, nome, sobrenome, cpf, email, senha, endereco, telefone):
        self.cod_cliente = cod_cliente
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
        self.email = email
        self.senha = senha
        self.endereco = endereco
        self.telefone = telefone

    def cliente_dicionario(self):
        return {"cod_cliente": self.cod_cliente,
                "nome": self.nome,
                "sobrenome": self.sobrenome,
                "cpf": self.cpf,
                "email": self.email,
                "endereco": self.endereco,
                "telefone": self.telefone}


# classe produto
class Produtos:
    def __init__(self, cod_produto, nome, descricao,preco):
        self.cod_produto = cod_produto
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
       

    def produto_dicionario(self):
        return {"cod_produto": self.cod_produto,
                "nome": self.nome,
                "descricao": self.descricao,
                "preco": self.preco}



# classe pedido
class Pedido:

    def __init__(self, cod_pedido, data_pedido, valor, cod_cliente):
        self.cod_pedido = cod_pedido
        self.data_pedido = data_pedido
        self.valor = valor
        self.cod_cliente = cod_cliente
        self.itens_pedido = []


    def pedido_dicionario(self):

        return {"cod_pedido": self.cod_pedido,
                "data_pedido": self.data_pedido,
                "valor": self.valor,
                "cod_cliente": self.cod_cliente,
                "itens_pedido": self.itens_pedido}


# classe itens_pedido
class Itens_Pedido:
    def __init__(self, cod_pedido, cod_produto, quantidade, valor_unitario):
        self.cod_pedido = cod_pedido
        self.cod_produto = cod_produto
        self.quantidade = quantidade
        self.valor_unitario = valor_unitario

        

    def itens_pedido_dicionario(self):
        return {"cod_pedido": self.cod_pedido,
                "cod_produto": self.cod_produto,
                "quantidade": self.quantidade,
                "valor_unitario": self.valor_unitario}
