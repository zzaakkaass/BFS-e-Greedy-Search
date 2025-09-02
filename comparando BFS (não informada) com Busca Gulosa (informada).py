from collections import deque
import heapq
import matplotlib.pyplot as plt
import time
#comparando BFS (não informada) com Busca Gulosa (informada)

# Grafo simples de exemplo (mapa de cidades)
grafo = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F", "G"],
    "D": ["B", "H"],
    "E": ["B", "I"],
    "F": ["C", "J"],
    "G": ["C"],
    "H": ["D", "J"],
    "I": ["E", "J"],
    "J": ["F", "H", "I"]  # J é o objetivo
}

# Heurística (distância estimada até J)
heuristica = {
    "A": 4, "B": 3, "C": 3,
    "D": 2, "E": 2, "F": 1,
    "G": 4, "H": 1, "I": 1, "J": 0
}

# --- BFS (Busca em Largura) - Não Informada ---
def bfs(grafo, inicio, objetivo):
    fila = deque([[inicio]])  # Fila com caminhos que começam no nó inicial
    visitados = set()  # Conjunto para não revisitar nós
    nos_visitados = 0  # Contador de nós expandidos

    while fila:
        caminho = fila.popleft()  # Pega o primeiro caminho da fila
        no = caminho[-1]  # Último nó do caminho atual
        nos_visitados += 1

        if no == objetivo:  # Chegamos ao destino!
            return caminho, nos_visitados

        if no not in visitados:
            visitados.add(no)
            # Para cada vizinho, cria um novo caminho e adiciona na fila
            for vizinho in grafo[no]:
                fila.append(caminho + [vizinho])
    
    return None, nos_visitados

# --- Busca Gulosa - Informada ---
def gulosa(grafo, inicio, objetivo, heuristica):
    # Fila de prioridade ordenada pela heurística (menor valor primeiro)
    fila = [(heuristica[inicio], [inicio])]
    visitados = set()
    nos_visitados = 0

    while fila:
        _, caminho = heapq.heappop(fila)  # Pega o caminho com menor heurística
        no = caminho[-1]
        nos_visitados += 1

        if no == objetivo:  # Chegamos ao destino!
            return caminho, nos_visitados

        if no not in visitados:
            visitados.add(no)
            # Para cada vizinho, cria novo caminho e adiciona na fila prioritária
            for vizinho in grafo[no]:
                heapq.heappush(fila, (heuristica[vizinho], caminho + [vizinho]))
    
    return None, nos_visitados

# --- Execução e Comparação ---
inicio, objetivo = "A", "J"

# Executa BFS
t0 = time.time()
caminho_bfs, visitados_bfs = bfs(grafo, inicio, objetivo)
tempo_bfs = time.time() - t0

# Executa Busca Gulosa
t0 = time.time()
caminho_gulosa, visitados_gulosa = gulosa(grafo, inicio, objetivo, heuristica)
tempo_gulosa = time.time() - t0

# Mostra resultados
print("=== COMPARAÇÃO DE ALGORITMOS DE BUSCA ===")
print(f"BFS (Não Informada):")
print(f"  Caminho: {' → '.join(caminho_bfs)}")
print(f"  Nós visitados: {visitados_bfs}")
print(f"  Tempo: {tempo_bfs:.6f} segundos\n")

print(f"Busca Gulosa (Informada):")
print(f"  Caminho: {' → '.join(caminho_gulosa)}")
print(f"  Nós visitados: {visitados_gulosa}")
print(f"  Tempo: {tempo_gulosa:.6f} segundos\n")

# --- Gráfico Comparativo ---
plt.figure(figsize=(10, 5))

# Gráfico 1: Nós visitados
plt.subplot(1, 2, 1)
plt.bar(["BFS", "Gulosa"], [visitados_bfs, visitados_gulosa], color=["blue", "red"])
plt.title("Nós Visitados") 
plt.ylabel("Quantidade")

# Gráfico 2: Tempo de execução
plt.subplot(1, 2, 2)
plt.bar(["BFS", "Gulosa"], [tempo_bfs, tempo_gulosa], color=["blue", "red"])
plt.title("Tempo de Execução")
plt.ylabel("Segundos")

plt.tight_layout()
plt.show()