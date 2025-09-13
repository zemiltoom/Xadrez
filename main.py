"""
Desafio de Xadrez - MateCheck
Autor: José Hamilton
Descrição:
    Este programa simula movimentos de peças de xadrez (Bispo, Torre e Rainha)
    utilizando estruturas de repetição (loops) para cada caso.
    O objetivo é treinar lógica de repetição e funções básicas.
"""

# =============================
# Constantes do desafio
# =============================

# Movimentos definidos pelo enunciado
BISPO_PASSOS = 5      # casas em diagonal superior direita
TORRE_PASSOS = 5      # casas para a direita
RAINHA_PASSOS = 8     # casas para a esquerda

# Direções simuladas com "printf"
def printf(direcao: str):
    """Simula o comando printf conforme exigido no enunciado."""
    print(direcao)


# =============================
# Funções de movimentação
# =============================

def mover_bispo():
    """
    Move o bispo 5 casas na diagonal superior direita.
    Para simular isso, imprimimos 'Cima' e 'Direita' juntos a cada passo.
    """
    print("\nMovimentação do Bispo:")
    for i in range(BISPO_PASSOS):
        printf("Cima")
        printf("Direita")


def mover_torre():
    """
    Move a torre 5 casas para a direita.
    Exemplo de repetição usando while.
    """
    print("\nMovimentação da Torre:")
    i = 0
    while i < TORRE_PASSOS:
        printf("Direita")
        i += 1


def mover_rainha():
    """
    Move a rainha 8 casas para a esquerda.
    Exemplo de repetição usando loop do tipo 'simulação do-while'.
    """
    print("\nMovimentação da Rainha:")
    i = 0
    while True:
        printf("Esquerda")
        i += 1
        if i >= RAINHA_PASSOS:
            break


# =============================
# Programa Principal
# =============================

if __name__ == "__main__":
    print("===== MateCheck - Simulação de Movimentos =====")
    mover_bispo()
    mover_torre()
    mover_rainha()
    print("\n===== Fim da Simulação =====")
