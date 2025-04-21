import networkx as nx
import matplotlib.pyplot as plt
from dfs_iterative import dfs_iterative
from bfs_iterative import bfs_iterative
from dijkstra import dijkstra

G = nx.Graph()

G.add_edge("Київ", "Львів", weight=540)
G.add_edge("Київ", "Харків", weight=480)
G.add_edge("Київ", "Одеса", weight=475)
G.add_edge("Київ", "Дніпро", weight=480)
G.add_edge("Львів", "Івано-Франківськ", weight=150)
G.add_edge("Львів", "Ужгород", weight=270)
G.add_edge("Харків", "Дніпро", weight=210)
G.add_edge("Харків", "Запоріжжя", weight=280)
G.add_edge("Дніпро", "Запоріжжя", weight=85)
G.add_edge("Дніпро", "Миколаїв", weight=310)
G.add_edge("Миколаїв", "Одеса", weight=130)
G.add_edge("Чернігів", "Київ", weight=150)
G.add_edge("Полтава", "Харків", weight=140)
G.add_edge("Вінниця", "Київ", weight=260)
G.add_edge("Житомир", "Київ", weight=140)
G.add_edge("Чернівці", "Івано-Франківськ", weight=130)
G.add_edge("Тернопіль", "Львів", weight=140)

print("Аналіз характеристик графа")
print("Кількість вершин:", G.number_of_nodes())
print("Кількість ребер:", G.number_of_edges())
print("Ступінь вершин (зв'язки кожної вершини):")
for node, degree in G.degree():
    print(f"Вершина {node} має ступінь {degree}")
degree_centrality = nx.degree_centrality(G)
print("Ступінь центральності:\n", degree_centrality)
closeness_centrality = nx.closeness_centrality(G)
print("Близькість вузла:\n", closeness_centrality)
betweenness_centrality = nx.betweenness_centrality(G)
print("Посередництво вузла:\n", betweenness_centrality)

adj_list = {node: dict(G[node]) for node in G.nodes}
print("Cписок суміжності:\n", adj_list)

print("Алгоритму DFS:")
dfs_iterative(adj_list, 'Ужгород')
print("\nАлгоритму BFS:")
bfs_iterative(adj_list, 'Ужгород')

# Застосування алгоритму Дейкстри
shortest_paths = nx.single_source_dijkstra_path(G, source='Запоріжжя')
shortest_path_lengths = nx.single_source_dijkstra_path_length(G, source='Запоріжжя')

print(shortest_paths)  # виведе найкоротші шляхи від вузла 'N' до всіх інших вузлів
print(shortest_path_lengths)  # виведе довжини найкоротших шляхів від вузла 'N' до всіх інших вузлів
dijkstra(adj_list, 'Запоріжжя')

pos = nx.spring_layout(G)
options = {
    "node_color": "lightgreen",
    "edge_color": "lightblue",
    "node_size": 500,
    "font_size": 10,
    "font_weight": "normal",
    "width": 2,
    "with_labels": True
}
nx.draw(G, pos, **options)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.title("Транспортна мережа обласних центрів України")
plt.show()

