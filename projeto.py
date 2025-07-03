import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.lines import Line2D
from definicao_nos import adicionar_nos

G = nx.Graph()
adicionar_nos(G)


#Definição das cores dos vértices
cores = []
for _, attr in G.nodes(data=True):
    tipo = attr.get("tipo")
    cores.append({
        "base": "cyan",
        "expansao": "lightblue",
        "mundo": "green",
        "mecanica": "orange",
        "sim": "purple",
        "carreira": "red"
    }.get(tipo, "gray"))  


#Modelagem do grafo
pos = nx.kamada_kawai_layout(G)



#Cores para as arestas
cores_arestas_mapa = {
    "expansão_de": "black",
    "mundo_de": "green",
    "traz": "orange",
    "sims": "purple",
    "moram": "brown",
    "trabalha_em": "red",
    "usam": "lightgreen",
    "usa_mec": "blue",
    "usa_mec_para_trabalho": "deepskyblue",
    "trabalhos_adicionados": "darkred",
    "oculto": "violet"
}
#Definição das cores ativas
cores_arestas = [
    cores_arestas_mapa.get(d.get("relacao", ""), "gray")
    for u, v, d in G.edges(data=True)
]


plt.figure(figsize=(24, 18))

#Para os nós
nx.draw_networkx_nodes(G, pos, node_color=cores, node_size=3500, alpha=0.9)
nx.draw_networkx_edges(G, pos, edge_color="gray", width=0.7, alpha=0.9)
nx.draw_networkx_labels(G, pos, font_size=10, font_color="black")

#Para as arestas
edge_labels = nx.get_edge_attributes(G, "relacao")
nx.draw_networkx_edges(G, pos, edge_color=cores_arestas, width=2.0, alpha=0.8)


legenda_nos = [
    mpatches.Patch(color="black", label="Jogo Base"),
    mpatches.Patch(color="blue", label="Expansão"),
    mpatches.Patch(color="green", label="Mundo"),
    mpatches.Patch(color="orange", label="Mecânica"),
    mpatches.Patch(color="purple", label="Sim"),
    mpatches.Patch(color="red", label="Carreira")
]


legenda_arestas = [
    Line2D([0], [0], color=cor, lw=2, label=rel)
    for rel, cor in cores_arestas_mapa.items()
]

leg1 = plt.legend(handles=legenda_nos, loc="lower left", fontsize=10, title="Tipos de Nós")
plt.gca().add_artist(leg1)

plt.legend(handles=legenda_arestas, loc="lower right", fontsize=10, title="Tipos de Relação")

# Título
plt.title("Rede de Conexões do The Sims 4", fontsize=14)
plt.axis("off")
plt.tight_layout()
plt.show()



def get_grafo():
    G = nx.Graph()
    adicionar_nos(G)
    return G
