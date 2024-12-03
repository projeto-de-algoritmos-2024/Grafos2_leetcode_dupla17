    
def dfs(matrix, visited, m, n, x, y): # um DFS pra pegar os caminhos e as distancias
    if visited[x][y] != -1:
        return visited[x][y] # checa se o local já foi visitado e se for retorna o valor

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    max_path = 1

    for dx, dy in directions:
        nx, ny = x + dx, y + dy # nx e ny são as direcões novas de X e Y
        if 0 <= nx < m and 0 <= ny < n and matrix[nx][ny] > matrix[x][y]: # se o tamanho do seguinte for maior continua a ¨busca¨
            max_path = max(max_path, 1 + dfs(matrix, visited, m, n, nx, ny))

    visited[x][y] = max_path # coloquei isso aqui e se tirar o código quebra :D não sei o porque, já que tecnicamente nao modifica a lista completa, mas pelo visto modifica
    
    return max_path # retorna o maior tamanho

matrix = [[9,9,4],[6,6,8],[2,1,1]]

m = len(matrix)
n = len(matrix[0])
visited = [[-1] * n for _ in range(m)] # faz um vetor para representar os visitados
print(max(dfs(matrix, visited, m, n, i, j) for i in range(m) for j in range(n))) # retorna o maior valor dos recebidos

# pra rodar no leetcode so colocar a parte fora da funcao na classe( e tirar o matrix)
# e colocar a funcao fora

"""

#CODIGO ANTERIOR NAO OTIMIZADO:

# DFS com umas formatacoes estranhas que usei para calcular o tamanho
def path_size(graph, pos, visited):
    bigger = 1
    for node in graph[pos]:
        if node == -1 or node in visited:
            visited.append(node)
            break
        aux = 1
        aux += path_size( graph, node, visited)
        #print(pos, aux, bigger, graph[pos])
        if aux > bigger:
            bigger = aux
    #print(graph)
    return bigger

# matrix de teste(da runtime error, por isso tive que refazer)
matrix = [[5,5,7,8,7,14,18,2,1,9,7,9,3,14,13,4,0],[11,18,17,4,0,0,15,18,18,5,8,9,17,0,9,3,3],[3,0,8,6,2,17,6,13,9,5,6,19,11,19,15,6,11],[4,7,0,3,3,1,0,1,10,18,0,14,4,1,3,19,12],[3,6,14,19,9,15,5,18,3,10,2,7,17,8,6,9,5],[14,1,15,0,12,9,3,0,3,15,9,4,12,3,4,10,7],[2,11,9,9,13,4,6,10,2,9,17,2,0,17,14,11,17],[0,3,0,11,7,5,2,3,3,11,4,6,12,14,8,3,9],[19,1,14,15,7,0,3,0,16,8,6,7,6,10,0,17,5],[1,8,6,15,11,11,3,14,18,1,16,11,18,12,11,6,16],[16,3,10,19,6,10,10,10,3,6,17,19,8,0,3,4,0],[17,9,9,14,12,14,9,0,8,13,8,13,15,3,18,15,17],[15,11,14,0,17,16,2,16,0,7,3,15,8,11,2,14,2]]
# 0
# 1
# 5
# 5
links = []
m = len(matrix)
n = len(matrix[m-1])
max_size = 0

# transforma a matriz em um grafo em forma de lista, eu acho mais facil mexer assim, mas consome muito processamento, tempo e memoria fazer isso por causa da redundancia, principalmente em matrizes maiores
aux = 0
# matrix to graph
for j in range(m):
    for i in range(n):
        links.append([])
        #print(matrix[j][i], ' ',  m*j + i )        
        if i < n - 1:
            if matrix[j][i] < matrix[j][i + 1]:
                #links[aux].append([j,i + 1])
                links[aux].append( n*j + i +1)
        if i > 0:
            if matrix[j][i] < matrix[j][i - 1]:
                #links[aux].append([j,i - 1])
                links[aux].append( n*j + i -1)
            
        if j < m - 1:
            if matrix[j][i] < matrix[j + 1][i]:
                #links[aux].append([j + 1,i])
                links[aux].append( n*(j+1) + i)
        if j > 0:
            if matrix[j][i] < matrix[j - 1][i]:
                #links[aux].append([j - 1,i])
                links[aux].append( n*(j-1) + i)
        if links[aux] == []:
            links[aux].append(-1)
        #print(links[aux])
        aux += 1

# a funcao que pega os resultados e retorna o maior, depois descobri que da pra usar o max() e colocar o for dentro, provavelmente esta escrito em C++ entao deve ser mais rapido

for x in range(len(links)):
    graph = links
    #print(links)
    size = path_size(graph, x, [])
    #print(size)
    if size > max_size:
        max_size = size
print(max_size)

"""
