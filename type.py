def saudacao(nome: str) -> str:
    return f"Como vai, {nome}?"

if __name__=="__main__":
    print(saudacao("Fulano"))
    print(saudacao(1))
    print(saudacao(True))

    varLogica: bool
    varInteira: int
    varReal: float

    varLogica = True
    varLogica = "Teste" # Erro

    varInteira = 10
    varInteira = 5.7 # Erro

    varReal = 10.6 
    varReal = 5
    varReal = "Real" # Erro

    