from estados import Estado
from token import Token as tk

class Lexico:
    def __init__ (self, arquivo):
        self.arquivo = arquivo                          # Arquivo do código .toy
        self.codigo_fonte = self.arquivo.read()         # String do código
        self.tamanho_codigo = len(self.codigo_fonte)    # Tamanho do código
        self.indice = 0                                 # Onde se está no arquivo
        self.token_lido = None                          # token == (token_id, lexema, linha, coluna)
        self.linha = 1                                  # Linha atual
        self.coluna = 0                                 # Coluna atual

    def fim_de_arquivo (self):
        return self.indice >= self.tamanho_codigo

    def descartar_brancos_e_comentarios (self):
        pass

    def get_char (self):
        if self.fim_de_arquivo():   # Chegou no final do arquivo
            return '\0'

        caractere = self.codigo_fonte[self.indice]
        self.indice += 1

        if caractere == '\n':   # Mudou de linha
            self.linha += 1
            self.coluna = 0
        else:                   # Ainda não chegou no final da linha
            self.coluna += 1

        return caractere

    def unget_char (self, simbolo):
        if simbolo == '\n': self.linha -= 1
        if self.indice > 0: self.indice -= 1
        self.coluna -= 1

    def imprimir_token (self, token):
        pass

    def get_token (self):
        estado = Estado.INICIAL
        simbolo = self.get_char()
        lexema = ''

        # TODO: Descartar brancos e comentários aqui

        linha = self.linha
        coluna = self.coluna

        while True:
            if estado == Estado.INICIAL:
                if simbolo.isalpha(): estado = Estado.IDENTS_OU_PALAVRAS_RESERVADAS
                elif simbolo.isdigit(): estado = Estado.NUMEROS
                elif simbolo == '"':  estado = Estado.STRINGS
                elif simbolo == '(': return tk.abreParentese, tk.msg(tk.abreParentese), linha, coluna
                elif simbolo == ')': return tk.fechaParentese, tk.msg(tk.fechaParentese), linha, coluna
                elif simbolo == ',': return tk.virgula, tk.msg(tk.virgula), linha, coluna
                elif simbolo == '<': estado = Estado.MENOR_OU_MENOR_IGUAL
                elif simbolo == '>': estado = Estado.MAIOR_OU_MAIOR_IGUAL
                elif simbolo == '=': estado = Estado.ATRIBUICAO_OU_IGUALDADE
                elif simbolo == '!': estado = Estado.DIFERENTE
                elif simbolo == '\0': return tk.eof, tk.msg(tk.eof), linha, coluna
                else:
                    lexema += simbolo
                    return tk.erro, lexema, linha, coluna

            if estado == Estado.IDENTS_OU_PALAVRAS_RESERVADAS: pass
            if estado == Estado.NUMEROS: pass
            if estado == Estado.STRINGS: pass
            if estado == Estado.MENOR_OU_MENOR_IGUAL: pass
            if estado == Estado.MAIOR_OU_MAIOR_IGUAL: pass
            if estado == Estado.ATRIBUICAO_OU_IGUALDADE: pass
            if estado == Estado.DIFERENTE: pass