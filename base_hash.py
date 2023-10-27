""" 
Algoritmo de implementação de Hash estático
Nome: Clara Araújo Maia e Nicolas Augusto Montovani
Curso: Engenharia da Computação
Matrícula: 0065609, 0065527
"""
from base_tree import Pagina, Indice, get_tamanho, get_argumentos

LOG = '/tmp/static_hash.log'

class Bucket(Pagina):
    """
    Bucket de Dados

    Args:
        Pagina (classe): herda da classe Pagina
    """
    def __init__(self, tamanho, dados=None):
        """
        Construtor parametrizado da classe Bucket
        
        Args:
            tamanho (int): tamanho da página de dados
        """
        super().__init__(tamanho)
        
        self._overflow = None   #Começando sem overflow
        self._dados = []
        
        if dados is not None:
            self._dados = dados
        #endif
    #enddef
    
    @property
    def overflow(self):
        """
        Páginas de overflow (característica do hash)
        """
        return self._overflow
    #enddef
    
    def set_overflow(self, bucket):
        self._overflow = bucket
    #enddef
    
    def procurar(self, chave):
        """
        Procura pela chave especificada
        
        Args:
            chave: chave que deseja procurar

        Returns:
            resultado: lista de registros
        """
        resultado = list()
        atual = self
        
        while atual is not None:
            #Para cada registro armazenado
            for registro in atual._dados:
                #Checar se o registro tem a chave procurada
                if registro[0] == chave:
                    resultado.append(registro)  #Adiciona o registro à lista de registros
                #endif
            #endfor
            
            atual = atual.overflow
        #endwhile
        
        return resultado
    #enddef
    
    def consegue_inserir(self, registro):
        """
        Verifica se a inserção é possível

        Args:
            registro: dado a ser verificado

        Raises:
            Exception: o registro é maior do que o tamanho máximo da página

        Returns:
            bool: se o registro for menor ou igual ao tamanho da página - o espaço usado, retorna True (1). Caso contrário, retorna False (0)
        """
        if get_tamanho(registro) > self._tamanho:   #Verifica se o tamanho do registro é maior do que aquele da página
            raise Exception('Registro maior do que o tamanho da página.')
        #endif
        
        if get_tamanho(registro) <= self._tamanho - self.espaco_usado:  #Verifica se há espaço suficiente para a inserção do registro
            return True
        #endif
        
        return False
    #enddef
    
    def inserir(self, registro):
        """
        Insere o registro na página
        
        Args:
            registro: dado a ser inserido
        """
        #Tenta inserir o registro no Bucket atual
        if self.consegue_inserir(registro):
            self._dados.append(registro)
        #endif
        else:   #Se o Bucket atual está cheio, faça um overflow
            if self._overflow is None:  #Se não tiver overflow, crie um
                self._overflow = Bucket(self._tamanho)
            #endif
            
            self._overflow.inserir(registro)    #Insere registro no overflow
        #endelse
    #enddef
     
    def remover(self, chave):
        """
        Remove o registro com a chave informada
        
        Args:
            chave: chave que contém o registro que deseja remover
        """
        atual = self
        
        while atual is not None:
            dadosFicar = []     #Dados a serem mantidos após a remoção
            
            for registro in atual._dados:
                if registro[0] != chave:    #Verifica se o registro não será removido
                    dadosFicar.append(registro)     #Armazena o registro na lista de registros a serem mantidos
                #endif
            #endfor
            
            #Atualizando os dados armazenados
            atual.set_dados(dadosFicar)
            atual = atual.overflow
        #endwhile
    #enddef
    
    def __repr__(self):
        """
        Representação para str
        
        Returns:
            texto: texto a ser representado
        """
        texto = ''
        
        if len(self._dados) > 0 and hasattr(self._dados[0], '__getitem__'):
            texto = '|'.join([str(registro[0]) for registro in self._dados])
        #endif
        
        texto = '[' + texto + ']'
            
        if self._overflow is not None:
            texto += '->' + str(self._overflow)
        #endif
        
        return texto
    #enddef
#endclass

class Diretorio():
    """
    Diretório de Buckets
    """
    def __init__(self, tamanho, dados=None):
        self._buckets = []  #Lista de buckets
        self._contador = tamanho // get_tamanho(Bucket(tamanho))    #Quantidade de buckets (divisão inteira)
        self._dados = []
        
        if dados is not None:
            self._dados = dados
        #endif
        
        #Criando um bucket para cada espaço
        for _ in range(self._contador):     
            self._buckets.append(Bucket(tamanho))
        #endfor
    #enddef
    
    def get_bucket(self, chave):
        """
        Pega o bucket para uma chave

        Args:
            chave: chave que deseja pegar um bucket

        Returns:
            dados: resto da divisão entre a chave e a quantidade de buckets
        """
        return self._dados[chave % self._contador]
    #enddef
    
    def __repr__(self):
        """
        Representação para str
        
        Returns:
            texto: texto representado para string
        """
        texto = 'Diretório: ' + str(len(self._dados)) + ' buckets'
        
        for posicao, bucket in enumerate(self._dados):
            if len(bucket) > 0:
                texto += '\n' + str(posicao) + ': ' + str(bucket)
            #endif
        #endfor
        
        return texto
    #enddef
    
    def __len__(self):
        """
        Representação para len()
        
        Returns:
            len(dados): tamanho dos dados
        """
        return len(self._dados)
    #enddef
#endclass

class IndiceHash(Indice):
    """
    Índice de Hash
    
    Args:
        Indice: essa classe é herdeira de outra classe chamada Indice
    """
    def __init__(self, tamanho, log, debugging=False):
        super().__init__(tamanho, log, debugging)
        
        #Criando um diretório
        self._debug('Criando diretório...')
        self._diretorio = Diretorio(tamanho)
        self._debug(f'{len(self._diretorio)} buckets criados')
    #enddef
    
    def inserir(self, registro):
        """
        Inserir registro no diretório
        
        Args:
            registro: registro que se deseja inserir no diretório
        """
        self._debug(f'Inserindo: {registro}')
        
        bucket = self._diretorio.get_bucket(registro[0])
        bucket.insert(registro)
    #enddef
    
    def remover(self, chave):
        """
        Remove o registro do diretório
        
        Args:
            chave: chave em que se encontra o registro para ele ser removido
        """
        self._debug(f'Removendo: {chave}')
        bucket = self._diretorio.get_bucket(chave)
        bucket.remove(chave)
    #enddef
    
    def procurar(self, chave):
        """
        Busca pela chave
        
        Args:
            chave: chave que se encontra o registro que se deseja procurar

        Returns:
            bucket: bucket que se encontra o registro desejado
        """
        bucket = self._diretorio.get_bucket(chave)
        
        return bucket.search(chave)
    #enddef
    
    def __repr__(self):
        """
        Representação para str, o mesmo que se usa em Diretorio
        
        Returns:
            str(diretorio): o mesmo tipo de texto usado no Diretorio
        """
        return str(self._diretorio)
    #enddef
#endclass

def main():
    """
    Função main
    """
    args = get_argumentos('Índice de Hash Estático')
    
    indice = IndiceHash(args.tamanho, LOG, args.debug)
    
    if args.file():
        indice.carregar_arquivo(args.file())
    #endif
    else:
        indice.menu()
    #endelse
#enddef

if __name__ == '__main__':
    main()
#endif