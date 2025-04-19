'''
Link do vídeo: https://drive.google.com/file/d/1buwccBuWPh0ZO6dw2Iy4zGXXt1RPEfTK/view?usp=sharing
Estudantes: Gabriel Gonzaga Seabra Câmara e Pedro Paulo Moreira de Freitas
'''

class Grafo:
    def __init__(self):
        self.vertices = {}  # Dicionário para armazenar os vértices e suas arestas
        self.num_vertices = 0  # Contador de vértices
        self.max_vertices = 20  # Limite máximo de vértices
        self.arestas = []  # Lista de arestas
        self.vertice_indices = {}  # Dicionário para mapear vértices aos seus índices
        self.indice_vertices = {}  # Dicionário para mapear índices aos seus vértices

    def adicionar_vertice(self, vertice):
        if vertice > 0 and self.num_vertices < self.max_vertices:
            self.vertices[vertice] = {}  # Inicializa o vértice com um dicionário vazio de arestas
            self.vertice_indices[vertice] = self.num_vertices  # Mapeia o vértice ao seu índice
            self.indice_vertices[self.num_vertices] = vertice  # Mapeia o índice ao seu vértice
            self.num_vertices += 1  # Incrementa o contador de vértices
            print(f"Vértice {vertice} adicionado com sucesso.\n")
        else:
            print("Erro: Vértice inválido ou limite de vértices alcançado.\n")

    def adicionar_aresta(self, origem, destino, peso):
        if origem in self.vertices and destino in self.vertices and peso > 0:
            self.vertices[origem][destino] = peso  # Adiciona a aresta no dicionário de arestas do vértice origem
            self.vertices[destino][origem] = peso  # Adiciona a aresta no dicionário de arestas do vértice destino
            self.arestas.append((peso, origem, destino))  # Adiciona a aresta à lista de arestas
            print(f"Aresta de {origem} para {destino} com peso {peso} adicionada.\n")
        else:
            print("Erro: Origem ou destino inválidos, ou peso não positivo.\n")

    def mostrar_dados(self):
        print("Vértices e suas arestas:")
        for vertice, arestas in self.vertices.items():
            print(f"Vértice {vertice}: pesos {arestas}")
        print()

    def dijkstra(self, origem, destino):
        distancias = {vertice: float('inf') for vertice in self.vertices}  # Inicializa as distâncias como infinito
        distancias[origem] = 0  # A distância até o vértice de origem é 0
        vertices_nao_visitados = set(self.vertices.keys())  # Conjunto de vértices não visitados
        rota = {vertice: [] for vertice in self.vertices}  # Inicializa a rota

        while vertices_nao_visitados:
            vertice_atual = min(vertices_nao_visitados, key=lambda v: distancias[v])  # Seleciona o vértice com a menor distância
            vertices_nao_visitados.remove(vertice_atual)  # Marca o vértice como visitado

            if vertice_atual == destino:
                break  # Encerra se o destino for alcançado

            for vizinho, peso in self.vertices[vertice_atual].items():
                dist_total = distancias[vertice_atual] + peso  # Calcula a distância total
                if dist_total < distancias[vizinho]:  # Verifica se a nova distância é menor
                    distancias[vizinho] = dist_total  # Atualiza a distância
                    rota[vizinho] = rota[vertice_atual] + [vertice_atual]  # Atualiza a rota

        return distancias[destino], rota[destino] + [destino]

    def kruskal(self):
        
        #Função recursiva para encontrar o índice da raiz do vértice "i"
        def encontrar(pais, i):
            if pais[i] == i:
                return i
            return encontrar(pais, pais[i])

        #Função para unir dois conjuntos de vértices
        def unir(pais, rank, x, y):
            #Busca o índice dos dois conjuntos a serem unidos
            raiz_x = encontrar(pais, x)
            raiz_y = encontrar(pais, y)
            if rank[raiz_x] < rank[raiz_y]:
                pais[raiz_x] = raiz_y
            elif rank[raiz_x] > rank[raiz_y]:
                pais[raiz_y] = raiz_x
            else:
                pais[raiz_y] = raiz_x
                rank[raiz_x] += 1

        resultado = []  # Lista para armazenar as arestas da AGM
        pais = []  # Lista para armazenar o pai de cada vértice
        rank = []  # Lista para armazenar o rank de cada vértice

        for vertice in range(self.num_vertices):
            pais.append(vertice)  # Inicializa cada vértice como seu próprio pai
            rank.append(0)  # Inicializa o rank de cada vértice como 0

        # Ordena as arestas por peso
        self.arestas.sort()

        for aresta in self.arestas:
            #Dividir as informações dos índices da aresta em variáveis diferentes
            peso, vertice_origem, vertice_destino = aresta
            indice_origem = self.vertice_indices[vertice_origem]
            indice_destino = self.vertice_indices[vertice_destino]
            raiz_origem = encontrar(pais, indice_origem)
            raiz_destino = encontrar(pais, indice_destino)

            if raiz_origem != raiz_destino:
                resultado.append((vertice_origem, vertice_destino, peso))
                unir(pais, rank, raiz_origem, raiz_destino)

        custo_minimo = 0
        print("Arestas na árvore geradora mínima:")
        for origem, destino, peso in resultado:
            custo_minimo += peso
            print(f"{origem} -- {destino} == {peso}")
        print(f"Custo total da árvore geradora mínima: {custo_minimo}")


# Cria um grafo vazio
grafo = Grafo()

grafo.adicionar_vertice(1)
grafo.adicionar_vertice(2)
grafo.adicionar_vertice(3)
grafo.adicionar_vertice(4)
grafo.adicionar_vertice(5)
grafo.adicionar_vertice(6)
grafo.adicionar_vertice(7)
grafo.adicionar_vertice(8)
grafo.adicionar_vertice(9)
grafo.adicionar_aresta(1, 2, 4)
grafo.adicionar_aresta(1,8,8)
grafo.adicionar_aresta(2,3, 8)
grafo.adicionar_aresta(2, 8, 11)
grafo.adicionar_aresta(3, 4, 7)
grafo.adicionar_aresta(3, 6, 4)
grafo.adicionar_aresta(3, 9, 2)
grafo.adicionar_aresta(4, 5, 9)
grafo.adicionar_aresta(4, 6, 14)
grafo.adicionar_aresta(5, 6, 10)
grafo.adicionar_aresta(6, 7, 2)
grafo.adicionar_aresta(7, 8, 1)
grafo.adicionar_aresta(7, 9, 6)
grafo.adicionar_aresta(8, 9, 7)
grafo.kruskal()

'''
if __name__ == "__main__":
    menu = 1
    while menu != "6":
        print("O que você deseja fazer?")
        print("1 - Adicionar vértice")
        print("2 - Adicionar aresta")
        print("3 - Mostrar dados")
        print("4 - Calcular caminho mínimo entre dois vértices")
        print("5 - Gerar AGM (Algoritmo de Kruskal)")
        print("6 - Sair")
        menu = input()

        if menu == "1":
            vertice = int(input("Digite o vértice: "))
            grafo.adicionar_vertice(vertice)

        if menu == "2":
            origem = int(input("Digite a origem: "))
            destino = int(input("Digite o destino: "))
            peso = int(input("Digite o peso: "))
            grafo.adicionar_aresta(origem, destino, peso)

        if menu == "3":
            grafo.mostrar_dados()

        if menu == "4":
            origem = int(input("Digite o vértice de origem: "))
            destino = int(input("Digite o vértice de destino: "))
            distancia, rota = grafo.dijkstra(origem, destino)
            if distancia == float('inf'):
                print(f"Não existe caminho entre os vértices {origem} e {destino}.\n")
            else:
                print(f"O caminho mínimo entre {origem} e {destino} é {distancia}")
                print("Rota: \n", rota)

        if menu == "5":
            grafo.kruskal()
'''