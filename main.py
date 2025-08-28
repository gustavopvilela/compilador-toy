from lexico import Lexico
from token import Token

if __name__ == '__main__':
    lexico = Lexico("teste.toy")
    token = lexico.get_token()
    while token[0] != Token.eof:
        lexico.imprimir_token(token)
        token = lexico.get_token()
    lexico.imprimir_token(token)