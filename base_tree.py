""" 
Algoritmo de base para uma indexação baseada em Árvore B+
Nome: Clara Araújo Maia e Nicolas Augusto Montovani
Curso: Engenharia da Computação
Matrícula: 0065609, 0065527
"""

import csv 
import logging  #Útil para debugar o código (vai gravando as mensagens log em um arquivo)
import argparse

TAMANHO_PAGINA = 512    #Tamanho de página padrão (512 bytes)

class Pagina(): 
    """
    Página de dados
    
    Os métodos inserir(), remover() e procurar() são abstratos. Com isso, devem ser implementados nas classes filhas
    
    Args:
        _tamanho (int)
        _dados (list)
    """
    def __init__(self, tamanho=0, dados=None):
        self._tamanho = tamanho
        self._dados = []
        
        if dados is not None:
            self._dados = dados
        #endif
    #enddef
    
    @property   #Faz com que o código abaixo seja um atributo da classe
    def espaco_usado(self):
        """
        Espaço usado por uma página
        
        Returns:
            _type_: tamanho da página
        """
        
        return get_tamanho(self._dados)
    #enddef
    
    def consegue_inserir(self, registro):
        """
        Faz a checagem se uma inserção é possível
        
        Args:
            registro: registro armazenado na página

        Raises:
            Exception: é raised quando o tamanho do registro for maior do que o tamanho ocupado pela página

        Returns:
            bool: se o tamanho do registro for menor ou igual àquele ocupado pela página, retorna True. Caso contrário, retorna False depois da Exception ser raised
        """
        
        if get_tamanho(registro) > self._tamanho:
            raise Exception("Registro é maior do que o tamanho da página.")
        #endif
        
        if get_tamanho(registro) <= self._tamanho - self.espaco_usado:
            return True
        #endif
        
        return False
    #enddef
    
    def inserir(self, registro):
        """
        Insere um registro na página
        
        Args:
            registro: registro a ser armazenado na página
        """
        
        #Deve ser implementado nas classes filhas
        raise NotImplementedError
    #enddef
    
    def remover(self, chave):
        """
        Remove um registro da página
        
        Args:
            chave: chave do registro a ser excluído
        """
        
        #Deve ser implementado nas classes filhas
        raise NotImplementedError
    #enddef
    
    @property   #Pega o método abaixo como se ele fosse um atributo
    def get_dados(self):
        """
        Método get() do atributo privado 'dados' da classe Página
        
        Returns:
            dados: dados da página
        """
        
        return self._dados 
    #enddef
    
    def set_dados(self, dados):     #Usado no Hash
        """
        Método set() do atributo privado 'dados' da classe Página
        Args:
            dados: dados da página
        """
        
        self._dados = dados
    #enddef
    
    def procurar(self, chave):
        """
        Procurar o registro na árvore
        
        Args:
            chave: chave do registro armazenado na árvore
        """
        
        #Deve ser implementado nas classes filhas
        raise NotImplementedError
    #enddef
    
    
    def __len__(self):  
        """
        Quantidade de registros que tem na página
        
        Returns:
            tamanho_dados: retorna o tamanho da lista de dados da página
        """
        
        return len(self._dados)
    #enddef
#endclass

class Indice():
    """
    Classe Índice
    
    Os métodos inserir(), remover(), procurar() e __repr__() são abstratos. Por isso, devem ser implementados dentro das classes filhas
    
    Args:
        _tamanho (int)
        _debugging (bool)
        _log (Logger)
    """
    def __init__(self, tamanho, log, debugging=False):
        """
        Construtor da classe Índice

        Args:
            tamanho: tamanho do índice
            log: nome do arquivo para colocar as mensagens log
            debugging (bool, optional): variável para debugar o índice. Defaults to False.
        """
        self._tamanho = tamanho
        self._debugging = debugging
        self._config_log(log)
        self._debug(f"Criando índice (página = {tamanho})...")
    #enddef
    
    
    def inserir(self, registro):
        """
        Insere um registro na página
        
        Args:
            registro: registro a ser armazenado na página
        """
        
        #Deve ser implementado nas classes filhas
        raise NotImplementedError
    #enddef
    
    def remover(self, chave):
        """
        Remove um registro da página
        
        Args:
            chave: chave do registro a ser excluído
        """
        
        #Deve ser implementado nas classes filhas
        raise NotImplementedError
    #enddef
    
    def procurar(self, chave): 
        """
        Procurar o registro na árvore
        
        Args:
            chave: chave do registro armazenado na árvore
        """
        
        #Deve ser implementado nas classes filhas
        raise NotImplementedError
    #enddef
    
    
    def carregar_arquivo(self, nomeArquivo):
        """
        Cria o arquivo CSV 
        
        Args:
            nomeArquivo (str): nome do arquivo a ser criado
        """
        
        with open(nomeArquivo, encoding="utf-8") as arquivo:
            leitor = csv.reader(arquivo)
            
            next(leitor)
            
            for linha in leitor:
                operacao = linha[0]
                
                registro = [int(valor) for valor in linha[1:]]
                
                if operacao == '+':
                    self.inserir(registro)
                #endif
                elif operacao == '-':
                    self.remover(registro[0])   #Envolve a busca (remoção de chaves existentes)
                #endelif
                elif operacao == '?':
                    self.procurar(registro[0])  #A chave não precisa existir para fazer a busca dela (tem o erro de NÃO ACHAR)
                #endelif
                
                self._debug(str(self))
            #endfor
        #endwithas
    #enddef
    
    def __repr__(self):     
        """
        Representação para str()
        """
        
        #Deve ser implementado nas classes filhas
        raise NotImplementedError
    #enddef
    
    def _debug(self, mensagem, *args, **kwargs):
        self._log.debug(mensagem, *args, **kwargs)
    #enddef
    
    def _config_log(self, log):
        """
        Criação do log
        
        Args:
            log (Logger): _description_
        """
        
        self._log = logging.getLogger(log)
        
        formatoStr = "%(nomeLevel)s - %(mensagem)s"
        formatoLog = logging.Formatter(formatoStr)
        
        gerenciadorArquivo = logging.FileHandler(log)
        gerenciadorArquivo.setFormatter(formatoLog)
        
        gerenciadorConsole = logging.StreamHandler()
        gerenciadorConsole.setFormatter(formatoLog)
        
        self._log.addHandler(gerenciadorArquivo)
        self._log.addHandler(gerenciadorConsole)
        
        if self._debugging:
            self._log.setLevel(logging.DEBUG)
        #endif
        else:
            self._log.setLevel(logging.INFO)
        #endelse
    #enddef
    
    def menu(self):
        """
        Menu interativo com o usuário
        Realiza as operações de inserir, de remover e de buscar
        """
        
        while True:
            print(str(self))
            print("+ | - | chave | (S)air")
            
            resposta = input().upper().strip()
            
            if resposta[0] == '+':
                registro = resposta[1:].split()
                
                if len(registro) > 0:
                    registro = [int(valor) for valor in registro]
                    
                    registro = tuple(registro)
                    
                    self.inserir(registro)
                #endif
            #endif
            elif resposta[0] == '-':
                chave = resposta[1:].strip()
                
                if len(chave) > 0:
                    chave = int(chave)
                    
                    self.remover(chave)
                #endif
            #endelif
            elif resposta == 'S':
                break
            #endelif
            else:
                chave = int(resposta)
                
                listaRegistros = self.procurar(chave)
                
                if len(listaRegistros) == 0:
                    print("Chave não encontrada!")
                #endif
                else:
                    print("Registros encontrados: ")
                    
                    for r in listaRegistros:
                        print(r, end=' ')
                    #endfor
                    
                    input()
                #endelse
            #endelse
        #endwhile
    #enddef
#endclass

def get_tamanho(dado):
    """
    Calcula o tamanho do dado
    
    Args:
        dado (int): dados armazenados na página

    Returns:
        somaTamanhoDados: se o dado for uma lista, retorna a soma de todos os itens armazenados nela
        
        tamanhoDados: se o dado não for uma lista, retorna o tamanho dele
    """
    
    if isinstance(dado, list):
        return sum(item.__sizeof__() for item in dado)
    #endif
    
    return dado.__sizeof__()
#enddef

def get_argumentos(texto):
    """
    Pega os argumentos
    
    Args:
        texto (str): _description_

    Returns:
        argumentos: _description_
    """
    
    parser = argparse.ArgumentParser(texto)
    
    parser.add_argument('-a', '--arquivo', help='Arquivo de entrada (CSV)')
    parser.add_argument(f'-p', '--tamanho-pagina {TAMANHO_PAGINA}', type=int, default=TAMANHO_PAGINA)
    parser.add_argument('-D', '--debug', action="store_true", default=False, help='Debugar')
    
    argumentos = parser.parse_args()
    
    return argumentos
#enddef