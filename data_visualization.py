import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

vertices = ["Blue Whale", "Killer Whale", "Leopard Seal", "Penguin",
            "Elephant Seal", "Squid", "Seagull", "Fish", "Krill",
            "Zooplankton", "Phytoplankton", "Crab", "Seaweed"]

G.add_nodes_from(vertices)

edges = [
         ("Elephant Seal", "Killer Whale", 0.13),
         ("Leopard Seal", "Killer Whale", 0.09),
         ("Penguin", "Killer Whale", 0.05),
         ("Penguin", "Leopard Seal", 0.22),
         ("Squid", "Penguin", 0.38),
         ("Squid", "Elephant Seal", 0.21),
         ("Crab", "Squid", 0.32),
         ("Seaweed", "Crab", 0.64),
         ("Seagull", "Leopard Seal", 0.14),
         ("Fish", "Leopard Seal", 0.29),
         ("Fish", "Seagull", 0.37),
         ("Zooplankton", "Fish", 0.55),
         ("Krill", "Blue Whale", 0.45),
         ("Phytoplankton", "Krill", 0.7),
		 ("Krill", "Fish", 0.2),
         ("Phytoplankton", "Zooplankton", 0.9),
         ]

def printAdjMatrix(matrix):
    for i in range(len(matrix)):
        for k in range(len(matrix[0])):
            print(matrix[i][k], " ", end='')
        print('')

edge_prey=[4,2,3,3,5,5,11,12,6,7,7,9,8,10,8,10]
edge_pred=[1,1,1,2,3,4,5,11,2,2,6,7,0,8,7,9]

n = G.number_of_nodes()

adjMatrix = [[0 for i in range(n)] for k in range(n)]

for i in range(len(edge_pred)):
    u=edge_prey[i]
    v=edge_pred[i]
    adjMatrix[u][v]=1

print("Adjacency Matrix")
printAdjMatrix(adjMatrix)
    
G.add_weighted_edges_from(edges)
print("Number of nodes",G.number_of_nodes())

print("Number of edges", G.number_of_edges())

pos = nx.spring_layout(G)  # positions for all nodes

nx.draw_networkx_nodes(G, pos, node_size=500)

nx.draw_networkx_edges(G, pos)

# labels
nx.draw_networkx_labels(G, pos)

plt.axis('off')

plt.show()

