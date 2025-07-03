
import networkx as nx
import matplotlib.pyplot as plt
import itertools
from projeto import get_grafo
from networkx.algorithms.community import greedy_modularity_communities

def desenhar_grafo(G, pos, titulo, node_color, node_size=None):
    plt.figure(figsize=(20, 16))
    nx.draw_networkx_nodes(G, pos, node_color=node_color, node_size=node_size or 1000, alpha=0.9)
    nx.draw_networkx_edges(G, pos, edge_color="gray", width=1.5, alpha=0.5)
    nx.draw_networkx_labels(G, pos, font_size=9, font_color="white")
    plt.title(titulo, fontsize=18)
    plt.axis("off")
    plt.tight_layout()
    plt.show()

def desenhar_grafo_destaque(G, pos, titulo, node_color, edge_color, node_size=None):
    plt.figure(figsize=(20, 16))
    nx.draw_networkx_nodes(G, pos, node_color=node_color, node_size=node_size or 1000, alpha=0.9)
    nx.draw_networkx_edges(G, pos, edge_color=edge_color, width=2.5, alpha=0.8)
    nx.draw_networkx_labels(G, pos, font_size=9, font_color="black")
    plt.title(titulo, fontsize=18)
    plt.axis("off")
    plt.tight_layout()
    plt.show()


def mostrar_lista_adjacencia(G):
    print("\nLista de Adjacência:")
    for no in G.nodes():
        vizinhos = list(G.neighbors(no))
        print(f"{no}: {vizinhos}")

def main():
    G = get_grafo()

    #Métricas
    graus = dict(G.degree())
    print("Grau dos vértices:")
    for no, grau in graus.items():
        print(f"{no}: {grau}")

    centralidade = nx.closeness_centrality(G)
    print("\nCentralidade (closeness):")
    for no, valor in sorted(centralidade.items(), key=lambda x: -x[1])[:5]:
        print(f"{no}: {valor:.3f}")

    componentes = list(nx.connected_components(G))
    print(f"\nNúmero de componentes conectados: {len(componentes)}")

    if nx.is_connected(G):
        diametro = nx.diameter(G)
        print("Diâmetro da rede:", diametro)
    else:
        print("O grafo não é conexo — o diâmetro não pode ser calculado diretamente.")

    
    print("\nCentralidade de Grau:")
    deg_cent = nx.degree_centrality(G)
    for no, val in sorted(deg_cent.items(), key=lambda x: -x[1])[:5]:
        print(f"{no}: {val:.3f}")

    print("\nCentralidade de Intermediação (Betweenness):")
    btw = nx.betweenness_centrality(G)
    for no, val in sorted(btw.items(), key=lambda x: -x[1])[:5]:
        print(f"{no}: {val:.3f}")

    print("\nPageRank:")
    pr = nx.pagerank(G)
    for no, val in sorted(pr.items(), key=lambda x: -x[1])[:5]:
        print(f"{no}: {val:.4f}")

    print("\nComunidades detectadas (Greedy Modularity):")
    comunidades = list(greedy_modularity_communities(G))
    for i, c in enumerate(comunidades):
        print(f"Comunidade {i+1} ({len(c)} nós): {list(c)[:5]}{'...' if len(c)>5 else ''}")

    densidade = nx.density(G)
    print(f"\nDensidade da rede: {densidade:.4f}")

    clustering = nx.average_clustering(G)
    print(f"Coeficiente de Clustering médio: {clustering:.4f}")

    assort = nx.degree_assortativity_coefficient(G)
    print(f"Coeficiente de Assortatividade: {assort:.4f}")

    #Cálculos internos
    print("\nExpansões com mais itens no CAS:")
    expansoes = [n for n, d in G.nodes(data=True) if d.get("tipo") == "expansao"]
    maiores_CAS = sorted(expansoes, key=lambda n: G.nodes[n].get("itens_no_CAS", 0), reverse=True)
    for e in maiores_CAS[:3]:
        print(f"{e}: {G.nodes[e]['itens_no_CAS']} itens")

    print("\nExpansões com mais itens no Modo Construção:")
    maiores_construcao = sorted(expansoes, key=lambda n: G.nodes[n].get("itens_modo_construcao", 0), reverse=True)
    for e in maiores_construcao[:3]:
        print(f"{e}: {G.nodes[e]['itens_modo_construcao']} itens")

    print("\nQuantidade de Sims ocultos:")
    sims_ocultos = [n for n, d in G.nodes(data=True) if d.get("tipo") == "sim" and d.get("se_e_oculto")]
    print(f"Total de Sims ocultos: {len(sims_ocultos)}")
    print("Nomes:", sims_ocultos)

    #menor caminho entre "Caleb Vatore" e "Feitiçaria"
    caminho = nx.dijkstra_path(G, source="Caleb Vatore", target="Greg")
    print("Menor caminho entre Caleb Vatore e Greg:", caminho)

    
    


    # Lista de adjacência
    #mostrar_lista_adjacencia(G)

    # Comunidades por cor
    pos = nx.kamada_kawai_layout(G)
    cores_comunidades = {}
    palette = itertools.cycle(['orange', 'lightgreen', 'lightblue', 'violet', 'pink', 'salmon', 'gold', 'red', 'cyan'])

    for comunidade, cor in zip(comunidades, palette):
        for no in comunidade:
            cores_comunidades[no] = cor

    cores_nos = [cores_comunidades[n] for n in G.nodes()]
    desenhar_grafo(G, pos, "Visualização: Comunidades (Greedy Modularity)", node_color=cores_nos, node_size=3500)

    #Dijkstra exemplo
    edge_path = list(zip(caminho, caminho[1:]))

    node_colors = ["red" if n in caminho else "lightgray" for n in G.nodes()]
    edge_colors = ["red" if (u, v) in edge_path or (v, u) in edge_path else "lightgray" for u, v in G.edges()]

    desenhar_grafo_destaque(
        G,
        pos,
        "Menor Caminho entre Caleb Vatore e Greg (Dijkstra)",
        node_color=node_colors,
        edge_color=edge_colors,
        node_size=3500
    )



if __name__ == "__main__":
    main()


 