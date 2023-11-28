import networkx as nx
import matplotlib.pyplot as plt
g=nx.DiGraph()


nodes=['parent-one','parent-two','p-1-2-child','child-c-1','child-c-2']

g.add_nodes_from(nodes)

edges=[('parent-one','p-1-2-child'),('parent-two','p-1-2-child'),('p-1-2-child','child-c-1'),('p-1-2-child','child-c-2')]

g.add_edges_from(edges)

Pos = {'parent-one': (1,5), 'parent-two': (5,5),'p-1-2-child': (3,-1),'child-c-1': (1,-5), 'child-c-2': (5,-5)}

nx.draw_networkx(g, Pos, with_labels=True, node_size=800,
node_color=['yellow', 'yellow', 'green','skyblue','skyblue'], font_size=10, font_color='black', font_weight='bold',
arrows=True)
plt.show()
