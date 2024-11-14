import sys

class Graph:
    def read_graph(file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()

        vertex_count = int(lines[0].strip())
        graph = []

        for i in range(1, vertex_count + 1):
            weights = list(map(int, lines[i].strip().split()))
            graph.append(weights)

        return graph, vertex_count

class NegativeCycleDetector:
    def has_negative_cycle(self, graph, vertex_count):
        distances = [float('inf')] * vertex_count
        distances[0] = 0

        # Relax edges vertex_count - 1 times
        for _ in range(vertex_count - 1):
            for u in range(vertex_count):
                for v in range(vertex_count):
                    if graph[u][v] != 100000 and distances[u] != float('inf') and distances[u] + graph[u][v] < distances[v]:
                        distances[v] = distances[u] + graph[u][v]

        # Check for negative-weight cycles
        for u in range(vertex_count):
            for v in range(vertex_count):
                if graph[u][v] != 100000 and distances[u] != float('inf') and distances[u] + graph[u][v] < distances[v]:
                    return True  # Negative cycle detected

        return False  # No negative cycle detected

def main():
    try:
        graph, vertex_count = Graph.read_graph("input.txt")

        detector = NegativeCycleDetector()
        has_negative_cycle = detector.has_negative_cycle(graph, vertex_count)

        with open("output.txt", 'w') as output_file:
            output_file.write("YES" if has_negative_cycle else "NO")
        
        print("YES" if has_negative_cycle else "NO")
        
    except Exception as ex:
        print(f"An error occurred: {ex}")

if __name__ == "__main__":
    main()
