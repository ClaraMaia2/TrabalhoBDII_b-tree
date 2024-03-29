# Trabalho de Banco de Dados II
Trabalho final da disciplina de Banco de Dados II, do curso de Engenharia da Computação, IFMG - Campus Bambuí.

# Criadores:
Clara Araújo Maia

Nicolas Augusto Montovani

## Árvore B+
Possui a estrutura semelhante à da árvore B, porém armazena os dados somente em suas folhas, além de elas são encadeadas, ou seja, fazem o armazenamento de dados em um arquivo e o do índice em outro.
<ul>
  <li>
    Alterações sempre mantêm a árvore balanceada
  </li>
  <li>
    A ocupação mínima das páginas deve ser de 50% (menos a raiz)
  </li>
  <li>
    Pode ter repetição de valores
  </li>
  <li>
    Páginas folha são duplamente ligadas, ou seja, estão ligadas com sua página pai e com seus irmãos
  </li>
  <ul style="square">
    <li>Cada página tem m entradas, em que d ≤ m ≤ 2d</li>
    <li>A raiz tem 1 ≤ m ≤ 2d registros</li>
  </ul>
</ul>

### Inserir dados
A inserção sempre acontece em um nó folha

<ol>
  <li>Localizar a folha dentro da qual a chave será inserida</li>
  <li>Localizar a posição de inserção dentro da folha</li>
  <li>Inserir a chave</li>
  <li>Se, após a inserção, a folha estiver completa; deverá ser feita a cisão da página</li>
  <ol>
    <li>As m - 1 chaves são divididas em dois grupos:</li>
    <ul>
      <li>(m - 1) / 2 chaves menores ficam na folha da esquerda</li>
      <li>(m - 1) / 2 chaves maiores ficam na folha da direita</li>
    </ul>
    <li>A maior chave da esquerda é copiada para o nó pai</li>
  </ol>
</ol>

### Excluir dados
Podem ocorrer de duas maneiras diferentes:
<ol>
  <li>Caso 1: A chave aparece apenas em um nó da folha</li>
  <ol>
    <li>A chave é simplesmente removida e a folha é reorganizada</li>
  </ol>
  <li>Caso 2: A chave aparece também nos nós internos</li>
  <ol>
    <li>A chave é removida, porém não é removida dos nós internos</li>
    <li>A folha é reorganizada</li>
    <li>Quando uma chave é retirada de um nó folha, a página pode ter uma ocupação abaxio do mínimo. Com isso, pode-se fazer uma das </li>
  </ol>
</ol>
