from typing import List, Dict

listaCompras: List[Dict[str, float]] = []
compra1 = {'Sabão em pó': 1.0}
compra2 = {'Manteiga': 0.5}
compra3 = {'Café': 1.0}
compraX = {1: True}

listaCompras.append(compra1)
listaCompras.append(compra2)
listaCompras.append(compra3)
listaCompras.append(compraX) # Erro

class Usuario:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

usu1: Usuario
usu2: Usuario

usu1 = Usuario("Fulano", "fulano@teste")
usu2 = "Meu usuario"