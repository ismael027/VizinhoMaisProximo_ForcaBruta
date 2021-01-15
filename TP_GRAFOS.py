import random
import time
import itertools

#Nomes: Luiza Borges Polita, Ismael Prado
#Matrículas: 18.1.8169, 18.1.8022


#cria o grafo completo
def completo(V, wMin, wMax):
    G = [[0 for i in range(V)] for i in range(V)]
    i = 0
    E = (V*(V-1))
    E = E / 2
    #E recebe o numero de arestas que um grafo completo possui
    while i < E:
        #sorteando vertices
        u = random.randint(0, V - 1)
        v = random.randint(0, V - 1)
        w = random.randint(wMin, wMax) #sorteando pesos
        if u != v and G[u][v] == 0:
            #colocando peso nas arestas
            G[u][v] = w
            G[v][u] = w
            i += 1
    return G #retorna grafo em matriz


#imprime matriz
def imprimir(matriz):
    print("-------------IMPRIMINDO MATRIZ-------------")
    for i in range(len(matriz)):
        print(matriz[i])

# converte de matriz de adjacência para Lista de Adjacência
def converter(a):
    ListaAdj = []
    for i in range(len(a)):
        for j in range(len(a[i])):
                       if a[i][j]!= 0:
                           w = a[i][j]
                           ListaAdj.append((i,j,w)) #Cria uma lista com os dados dos vertices e o peso
    return ListaAdj


#função para encontrar o peso entre dois vertices
def peso_aresta(u,v,listaAdj):
    for x,y,w in listaAdj:
        if u == x and v == y:
            return w
    print("erro") #se não foi possível encontrar o peso entre eles retorna erro


#algoritmo força bruta
def forca_bruta(grafo):
    vertices = [] #vetor que armazena os vértices
    custo_min = float('inf') #custo mínimo
    melhor_caminho = []  #vetor com o melhor caminho

    #acrescentando os nós do grafo no vetor vertices
    for i in range(len(grafo)):
        vertices.append(i)

    #criando lista com todas as permutações possíveis entre os vértices
    permutacoes = list(itertools.permutations(vertices))

    listaAdj = converter(grafo) #lista de adjacências do grafo

    #laço principal do algoritmo
    for i in permutacoes: #i será cada permutação dentro da lista de permutações
        i = list(i)       #transforma i em uma lista para conseguirmos acrescentar a posição i[0] para que se forme um ciclo
        i.append(i[0])    #acrescenta a primeira posição na lista e cria um ciclo
        custo_rota = 0    #o custo da rota "i" recebe 0 para podermos somar com cada peso nas arestas
        aux = 0           #variavel auxiliar para podermos analisar cada par de vértices da rota "i" até o fim.

        #laço que passa por todos os vértices dentro da rota "i"
        for j in i:
            u = aux                     #i[u] e i[v] serão os vértices da aresta que será analisada
            v = aux + 1

            if v <= len(vertices):                                        #se a posição v for menor que o tamanho da lista de vertices
                custo_rota = custo_rota + peso_aresta(i[u],i[v],listaAdj) #adiciona o peso da aresta analisada ao custo da rota
            aux = aux + 1    #atualiza auxiliar

        if custo_rota < custo_min:      #se o custo da rota "i" analisada for menor que o custo mínimo, o custo mínimo e o melhor caminho são atualizados
            custo_min = custo_rota
            melhor_caminho = i

    #imprimindo melhor rota e o seu custo
    print("Rota: ", melhor_caminho)
    print("Custo: ", custo_min)

#algoritmo vizinho mais próximo
def vizinhoMaisProximo(grafo):
    vertice = 0 #vertice origem
    caminho = []
    restantes = []
    listaAdj = converter(grafo) #criando lista de adjacências
    origem = 0
    custo = 0
    #cria lista de restantes
    for i in range(len(grafo)):
        restantes.append(i)

    #remove a origem dos restantes
    restantes.remove(vertice)

    #laço principal
    while restantes:
        #analisa qual o menor adj do vertice analisado
        menor = None
        for u, v, w in listaAdj:
            if u == vertice and v in restantes: #analisando os adj do vertice que estão em restantes
                if menor == None:   #menor recebe o primeiro adj para analisar o resto
                    menor = v
                    peso = w
                elif peso > w:
                    menor = v
                    peso = w
        custo = custo + peso
        #criando o caminho
        caminho.append((vertice, menor))

        #trocando o vértice analisado para o menor
        vertice = menor

        #removendo o vertice dos restantes
        restantes.remove(vertice)
    caminho.append((vertice, origem))

    print("Rota: ", caminho)
    print("Custo: ", custo)

def menu():
    print(" ")
    print("Escolha uma opção:")
    print("[1] Vizinho Mais Próximo")
    print("[2] Força Bruta")
    print("[3] Sair")
    opcao = int(input('>>>>>'))
    return opcao


def entradas():
    v = int(input('Digite o numero de vertices: '))
    wMin = int(input('Digite o peso mínimo: '))
    wMax = int(input('Digite o peso máximo: '))
    return v, wMin, wMax


#menu
opcao = 0
print("=-==-==-=BEM VINDO(A)=-==-==-=")
while opcao != 3:
    opcao = menu()
    if opcao == 1:
        v, min, max = entradas()
        print(" ")
        print("=-==-==-=VIZINHO MAIS PRÓXIMO=-==-==-=")
        inicio = time.time()
        grafo = completo(v,min,max)
        vizinhoMaisProximo(grafo)
        fim = time.time()
        tempo = (fim-inicio)
        print("Tempo: %.3f" %tempo)

    elif opcao == 2:
        v, min, max = entradas()
        print(" ")
        print("=-==-==-=FORÇA BRUTA=-==-==-==-=")
        inicio = time.time()
        grafo = completo(v, min, max)
        forca_bruta(grafo)
        fim = time.time()
        tempo = (fim - inicio)
        print("Tempo: %.3f" %tempo)

    elif opcao == 3:
        print("Finalizando...")

    else:
        print("Digite uma opção válida.")
    print('=-=' * 13)




