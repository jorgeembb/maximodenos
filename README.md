## 1. Estratégia de Implementação
  Optei por uma abordagem que prioriza:

  -Clareza: Código simples de compreender e manter

  -Eficiência: Algoritmos aprimorados para melhor eficácia
  
  -Modularidade: Partes autônomas com funções claramente estabelecidas

## 2. Decisões de Projeto.
 2.1. Representação da Árvore
   ```bash
   class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

-Segue o padrão clássico de estruturas de dados

-Permite representação recursiva natural

-Simples e eficiente em termos de memória

  2.2. Construção da Árvore
  ```bash
  def build_tree(level_order):
    # Implementação com fila (BFS)
```
-A entrada chega em ordem de nível (BFS natural)

-Garante fidelidade à estrutura especificada

-Complexidade O(n) - ideal para o problema

  2.3. Implementação das Travessias
```bash
def preorder_traversal(root):
    # Visita raiz antes dos filhos

def inorder_traversal(root):
    # Visita raiz entre os filhos

def postorder_traversal(root):
    # Visita raiz após os filhos
```
-Código mais legível e auto-documentado

-Agiliza a manutenção e a resolução de problemas

-Possibilita melhorias específicas para cada situação

## 3. Tratamento de Entradas

-Conversão robusta de strings para a estrutura de dados

-Suporte a múltiplos formatos (None, null, vazio)

-Mensagens de erro claras e úteis

Alternativas consideradas e rejeitadas:

Uso de eval(): risco de segurança

Parsing manual muito complexo: manutenção difícil

## 4. Interface do Usuário
Características implementadas:

-Feedback imediato sobre operações

-Menu interativo intuitivo

-Fluxo de execução claro

## 5. Análise de Desempenho
Todas as operações principais apresentam complexidade O(n), garantindo:

-Boa performance mesmo com árvores grandes

-Escalabilidade adequada

-Consistência nos tempos de execução
