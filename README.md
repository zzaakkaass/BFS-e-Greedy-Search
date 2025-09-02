descrição

esse script compara dois algoritmos de busca em grafos:

bfs (não informada): explora em largura, sem usar informação extra.

busca gulosa (informada): usa uma heurística (distância estimada até o objetivo) e escolhe sempre o nó com menor custo heurístico.

o código também mede tempo de execução e nós visitados, além de gerar gráficos comparativos com matplotlib.

- funcionamento

1. grafo e heurística

- grafo é um conjunto de cidades conectadas.

- heurística define um "custo estimado até o objetivo J".

2. bfs

- igual ao algoritmo 1, mas aqui também conta quantos nós foram visitados.

3. busca gulosa

- usa heapq pra manter uma fila de prioridade ordenada pela heurística.

- sempre expande o nó que parece mais próximo do objetivo.

4. comparação

- executa bfs e gulosa do nó A até J.

- mede tempo de execução.

- conta nós visitados.

- mostra resultados no terminal.

gera dois gráficos:

- quantidade de nós visitados.

- tempo de execução.

 5. saída

- imprime no terminal os caminhos encontrados, número de nós visitados e tempo de cada algoritmo.

- exibe gráfico comparando desempenho.

- como executar
python "comparando BFS (não informada) com Busca Gulosa (informada).py"
