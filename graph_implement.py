from graph import Graph
graph = Graph()
print("Enter the edges of graph in u->v format and enter stop when done:\n")
while True:
    k = input()
    if k.lower() == "stop":
        break
    u, v = int(k.split("->")[0]), int(k.split("->")[1])
    graph.add_edge(u, v)

print("\nThe vertices in Graph are:")
for i in graph.v:
    print(i, end=" ")
print(f"\nThe graph has {graph.number_edges} edges")
print("\n\nSelect the source vertex for Breadth First Search Traversal:")
k = int(input())
print("\nThe BFS traversal is:")
graph.bfs(k)
print("\n\nSelect the source vertex for Depth First Search Traversal:")
k = int(input())
print("\nThe DFS traversal is:")
graph.dfs(k)
print("Testing merge")

