def graph_coloring(graph, n):
    result = [-1] * n      # Store color of each vertex
    result[0] = 0          # Assign the first color to the first vertex
    available = [True] * n # Keep track of available colors

    # TODO Assign colors to remaining vertices
    for u in range(1, n):
        # iterate through neighbors of vertex and mark colors as unavailable
        for v in graph[u]:
            if result[v] != -1: # if != -1, it means the vertex has been colored
                available[result[v]] = False

        # Find the first available color
        for color in range(n):
            if available[color]:
                result[u] = color
                break

        # Reset the available array for the next iteration
        for v in graph[u]:
            if result[v] != -1:
                available[result[v]] = True

    # Print the result
    print("Vertex\tColor")
    for u in range(n):
        print(f"{u}\t{result[u]}")

    # Print the total number of colors used
    print("Minimum number of colors required:", max(result) + 1)


def main():
    num_edges = int(input("Enter the number of edges: "))
    print("Enter each edge as two space-separated integers (e.g., '0 1'):")

    edges = []
    max_vertex = -1

    for _ in range(num_edges):
        u, v = map(int, input().split()) # store edges into u and v
        edges.append((u, v))
        max_vertex = max(max_vertex, u, v)

    n = max_vertex + 1  # Total number of vertices
    graph = [[] for _ in range(n)] 

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # Perform graph coloring
    graph_coloring(graph, n)

if __name__ == "__main__":
    main()