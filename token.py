from enum import IntEnum

class Token (IntEnum):
    # Tokens
    erro = 1
    eof = 2
    identificador = 3
    numero = 4
    string = 5

    # Comandos
    INICIO = 6
    FIM = 7
    LEIA = 8
    ESCREVA = 9
    IF = 10
    ELSE = 11
    AND = 12
    OR = 13
    NOT = 14

    # Símbolos
    abreParentese = 15          # (
    fechaParentese = 16         # )
    virgula = 17                # ,
    pontoVirgula = 18           # ;
    ponto = 19                  # .
    abreChave = 20              # {
    fechaChave = 21             # }
    igual = 22                  # ==
    diferente = 23              # !=
    menor = 24                  # <
    menorIgual = 25             # <=
    maior = 26                  # >
    maiorIgual = 27             # >=
    mais = 28                   # +
    menos = 29                  # -
    multiplicacao = 30          # *
    divisao = 31                # /
    modulo = 32                 # %
    atribuicao = 33             # =

    @classmethod
    def msg (cls, token):
        nomes = {
            1: 'erro',
            2: '<eof>',
            3: 'ident',
            4: 'numero',
            5: 'string',
            6: 'INICIO',
            7: 'FIM',
            8: 'LEIA',
            9: 'ESCREVA',
            10: 'IF',
            11: 'ELSE',
            12: 'AND',
            13: 'OR',
            14: 'NOT',
            15: '(',
            16: ')',
            17: ',',
            18: ';',
            19: '.',
            20: '{',
            21: '}',
            22: '==',
            23: '!=',
            24: '<',
            25: '<=',
            26: '>',
            27: '>=',
            28: '+',
            29: '-',
            30: '*',
            31: '/',
            32: '%',
            33: '='
        }
        return nomes[token]

    @classmethod
    def reservadas (cls, lexema):
        reservadas = {
            'INICIO': Token.INICIO,
            'FIM': Token.FIM,
            'LEIA': Token.LEIA,
            'ESCREVA': Token.ESCREVA,
            'IF': Token.IF,
            'ELSE': Token.ELSE,
            'AND': Token.AND,
            'OR': Token.OR,
            'NOT': Token.NOT,
        }

        if lexema in reservadas: return reservadas[lexema]
        else: return Token.identificador