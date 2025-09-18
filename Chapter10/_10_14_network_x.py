import networkx as nx
import matplotlib.pyplot as plt

## 그래프 객체 생성
G = nx.Graph()

## 노드(정점) 추가
G.add_nodes_from(["A", "B", "C", "D", "E"])

## 엣지(간선) 추가
G.add_edges_from([("A", "B"), ("A", "C"), ("B", "D"), ("C", "D"), ("C", "E")])

## 그래프 시각화
nx.draw(G, with_labels=True, node_size=1000)

plt.show()