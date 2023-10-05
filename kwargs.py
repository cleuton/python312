from typing import TypedDict, Unpack


def calcular_preco(base: float, **kwargs: float) -> float: 
    valor: float = base
    if "desconto_vendedor" in kwargs:
        valor = valor - (valor * kwargs["desconto_vendedor"])
    if "desconto_loja" in kwargs:
        valor = valor - (valor * kwargs["desconto_loja"])
    return valor

print(calcular_preco(5000))
print(calcular_preco(5000, desconto_vendedor=0.05))
print(calcular_preco(5000, desconto_loja=0.1, desconto_vendedor=0.05))

class Desconto(TypedDict):
    desconto_loja: float
    desconto_vendedor: float
    sobretaxa: float

def calcular_preco_2(base: float, **kwargs: Unpack[Desconto]) -> float: 
    valor: float = base
    valor = valor - (valor * kwargs["desconto_vendedor"])
    valor = valor - (valor * kwargs["desconto_loja"])
    valor = valor + (valor * kwargs["sobretaxa"])
    return valor
    
desconto: Desconto = {"desconto_loja": 0.1, "desconto_vendedor": 0.05, "sobretaxa": 0.0}
print(calcular_preco(5000,**desconto))


