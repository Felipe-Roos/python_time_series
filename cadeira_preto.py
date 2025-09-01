"""
Arquivo: cadeira.preto.py
Descrição: Contém funções utilitárias como cálculo de máximo, verificação de número par e cálculo de fatorial.
Autor: Felipe Roos 
Data: 01/09/2025
Versão: 1.0
"""
"""Professor, eu acho que fiz certo as atividade foi mal ter mandando em cima da hora"""

"O que é um cabeçalho de dentro de um arquivo python e para que server o que é um Docstring, e para que server"
""
"O docString ele serve como algo para identificar e explicar de forma rapido o intuitiva o código, é usado exclusivamente para descrever um código especifico"

"O cabeçalho ele trablha executando alguns scrips e para executar o arquivo e realizando uma conversão de dados"

"Enquanto um atua descrevendo o que o código fonte vai fazer, 1 atua fazendo com o que o código rode"

# atividade 1 = formete o cabeçalho deste arquivo

# atividade 2 = implemente as funções abaixo e coloque as docstrings



def maximo(nums: list[int]) -> int:
    """
    Retorna o maior número de uma lista.

    Args:
        nums (list[int]): Lista de números inteiros.

    Returns:
        int: O maior número encontrado na lista.
    """
    maior = nums[0]
    for num in nums:
        if num > maior:
            maior = num
    return maior



def e_par(n: int) -> bool:
    """
    Verifica se um número é par.

    Args:
        n (int): Número inteiro a ser verificado.

    Returns:
        bool: True se for par, False caso contrário.
    """
    return n % 2 == 0
  

def fatorial(n: int) -> int:
    """
    Calcula o fatorial de um número de forma iterativa.

    Args:
        n (int): Número inteiro não-negativo.

    Returns:
        int: Valor do fatorial de n.

    Raises:
        ValueError: Se n for negativo.
    """
    if n < 0:
        raise ValueError("Não existe fatorial de número negativo.")

    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

    if __name__ == "__main__":
    print("Teste da função maximo:", maximo([1, 3, 9, 2, 10, 5, 201, 213, 218]))  
    print("Teste da função e_par:", e_par(5))             
    print("Teste da função fatorial:", fatorial(3))   
    ...
