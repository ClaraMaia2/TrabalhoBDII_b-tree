""" 
Algoritmo de implementação da Árvore B+
Nome: Clara Araújo Maia e Nicolas Augusto Montovani
Curso: Engenharia da Computação
Matrícula: 0065609, 0065527
"""
from base_tree import Pagina, Indice

class PaginaArvore(Pagina): 
    def __init__(self, chave, tamanho):
        super().__init__(tamanho)
        
        self._chave = chave
        self._dados = []
    #enddef
    
    @property
    def get_lista_chave(self):
        """
        Pega a lista de chaves da árvore
        """
        #Deve ser implementada na classe filha
        raise NotImplementedError
    #enddef
    
    #?????????
    def get_chave(self, posicao):
        """
        Pega a chave em uma certa posição
        
        Args:
            posicao (int): posição da chave na árvore

        Returns:
            c
        """
        #Deve ser implementada na classe filha
        raise NotImplementedError 
    #enddef
    
    #?????????
    def get_esquerda(self, remove):
        
        #Deve ser implementada na classe filha
        raise NotImplementedError
    #enddef
    
    #?????????
    def get_direita(self, remove):
        
        #Deve ser implementada na classe filha
        raise NotImplementedError
    #enddef
    
    def get_estrutura(self, nivel=0):
        """
        Mostra a estrutura da árvore

        Args:
            nivel (int, optional): nível máximo definido para a implementação da árvore. Defaults to 0.
        
        Returns:
            Estrutura da árvore (str)
        """
        #Deve ser implementada na classe filha
        raise NotImplementedError
    #enddef
    
    def dividir(self):
        
        #Deve ser implementada na classe filha
        raise NotImplementedError
    #enddef
    
    def inserir_direita(self, dados):
        """
        Fazer a inserção dos dados na parte da direita da árvore (valores maiores)
        
        Args:
            dados: dados a serem inseridos na árvore
        """
        print()
    #enddef
    
    def inserir_esquerda(self, dados):
        """
        Fazer a inserção dos dados na parte da esquerda da árvore (valores menores)
        
        Args:
            dados: dados a serem inseridos na árvore
        """
        print()
    #enddef
    
    def busca_binaria(self, chave, comeco=0):
        """
        Algoritmo de busca em vetores que segue o paradigma de divide and conquer. 
        Parte do pressuposto que o vetor está ordenado e realiza sucessivas divisões do espaço de busca comparando o elemento buscado com o elemento no meio do vetor. 
        Se esse elemento for a chave, a busca termina com sucesso. Se não, se o elemento do meio vier antes do elemento buscado, então a busca continua na metade posterior do vetor. Finalmente, se o elemento do meio vier depois da chave, a busca continua na metade anterior do vetor
        
        Args:
            chave: chave que será buscada
            comeco (int, optional): de onde começa a busca. Defaults to 0.

        Returns:
            comeco: índice onde a chave se encontra. Caso não ache a chave, retorna -1, indicando que a chave não está na árvore
        """
        final = self._tamanho - 1
        
        while comeco <= final:
            meio = (comeco + final ) / 2
            
            if chave < self._dados[meio]:
                final = meio - 1
            #endif
            elif chave == self._dados[meio]:
                return meio
            #endelif
            else:
                comeco = meio + 1
            #endelse
        #endwhile
        
        return -1
    #enddef
    
    
    def procurar(self, chave):
        """
        Faz a busca linear do índice da chave desejada
        
        Args:
            chave: chave para buscar na árvore

        Returns:
            índice: se achar a chave na árvore, retorna em qual índice ela está. Se não, retorna -1, mostrando que a chave não está na árvore
        """
        for indice in range(self._tamanho):
            if self._dados[indice] == chave:
                return indice
            #endif
        #endfor
        
        return -1
    #enddef
#endclass

class PaginaFolha(PaginaArvore):
    """ 
    _data = [10*, 20*, 30*, 40*, 50*]
    
    Uma lista com um único registro, então pode ser uma tupla
    
    inserir() -> Pode inserir e só depois ver se estourou o tamanho da página. Se estourar, chama o método split() na folha (somente para fins didáticos)
    """
    
    def __init__(self, chave, tamanho):
        super().__init__(chave, tamanho)
    #enddef
    
    def get_chave(self, posicao):
        return super().get_chave(posicao)
    #enddef
    
    def get_lista_chave(self):
        return super().get_lista_chave
    #enddef
    
    def get_estrutura(self, nivel=0):
        return super().get_estrutura(nivel)
    #enddef
    
    def get_esquerda(self, remove):
        return super().get_esquerda(remove)
    #enddef
    
    def get_direita(self, remove):
        return super().get_direita(remove)
    #enddef
    
    def inserir(self, registro):
        return super().inserir(registro)
    #enddef
    
    def remover(self, chave):
        return super().remover(chave)
    #enddef
    
    def procurar(self, chave):
        return super().procurar(chave)
    #enddef
    
    def dividir(self):
        return super().dividir()
    #enddef
#endclass

class PaginaNaoFolha(PaginaArvore):
    """ 
    _data = [ ■ │ 10 │ ■ │ 20 │ ■ │ 30 │ ■ ]
    
    Não pode ser uma tupla, porque além dos registros, também deve vir junto os ponteiros
    As chaves são os índices ímpares e os ponteiros são os índices pares
    """
    
    def __init__(self, chave, tamanho):
        super().__init__(chave, tamanho)
    #enddef
    
    def busca_binaria(self, chave, comeco=0):
        """
        Realiza a mesma busca binária já implementada na sua classe pai
        """
        return super().busca_binaria(chave, comeco)
    #enddef
    
    def _pegar_do_irmao(self, posicao_filho):
        print()
    #enddef
    
    def _juntar_filho(self, posicao, filho):
        print()
    #enddef
    
    def get_chave(self, posicao):
        return super().get_chave(posicao)
    #enddef
    
    def get_lista_chave(self):
        return super().get_lista_chave
    #enddef
    
    def get_esquerda(self, remove):
        return super().get_esquerda(remove)
    #enddef
    
    def get_direita(self, remove):
        return super().get_direita(remove)
    #enddef
    
    def get_estrutura(self, nivel=0):
        return super().get_estrutura(nivel)
    #enddef
    
    def inserir(self, registro):
        return super().inserir(registro)
    #enddef
    
    """ 
    Se uma página não for folha, não tem como remover dela
    """
    def remover(self, chave):
        return super().remover(chave)
    #enddef
    
    def procurar(self, chave):
        return super().procurar(chave)
    #enddef
    
    def dividir(self):
        return super().dividir()
    #enddef
#endclass

class IndiceArvore(Indice):
    """
    Índice da árvore
    
    Args:
        Indice: classe herdeira de outra classe geral Indice
    """
    def __init__(self, tamanho, log, debugging=False):
        super().__init__(tamanho, log, debugging)
    #enddef
    
    def inserir(self, registro):
        return super().inserir(registro)
    #enddef
    
    def remover(self, chave):
        return super().remover(chave)
    #enddef
    
    def procurar(self, chave):
        return super().procurar(chave)
    #enddef
#endclass        