def build_graph(A, B, num_nodes):
    graph_built = [[] for i in range(num_nodes)]
    graph_degree_nodes = num_nodes * [0]
    IsStar = False

    for i in range(len(A)):
        graph_built[A[i]].append(B[i])
        graph_built[B[i]].append(A[i])
        graph_degree_nodes[A[i]] += 1
        graph_degree_nodes[B[i]] += 1

    Hig_degree = [val for val in graph_degree_nodes if val > 1]

    if len(Hig_degree) == 1:
        IsStar = True

    return graph_built, IsStar


# def star(graph_built, num_nodes):
#     num = 0
#     for i in range(len(graph_built)):
#         if len(graph_built[i]) > 1:
#             num += 1
#             if num > 1:
#                 return False
#     else:
#         return True


def search_node_degree_1(graph_built):
    for i in range(len(graph_built)):
        if len(graph_built[i]) == 1:
            return i


def is_even(number):
    if number % 2 == 1:
        return True
    else:
        return False


def compute_odd_routes(graph_built, first_node, num_nodes):
    distances = num_nodes*[0]
    count = 0
    followers = []
    nodes_to_visit = [first_node]

    while nodes_to_visit:
        node_to_analize = nodes_to_visit.pop(0)
        followers = graph_built[node_to_analize].copy()

        for next_node in followers:
            distances[next_node] = distances[node_to_analize] + 1
            if is_even(distances[next_node]):
                count += 1
            graph_built[node_to_analize].remove(next_node)
            graph_built[next_node].remove(node_to_analize)
            nodes_to_visit.append(next_node)

    return count


def solution(A, B):
    num_nodes = len(A) + 1
    if (num_nodes == 1):
        return 0
    elif (num_nodes == 2):
        return 1
    else:
        graph_built, IsStar = build_graph(A, B, num_nodes)
        if IsStar:
            return (num_nodes-1)
        else:
            node_degree_1 = search_node_degree_1(graph_built)
            odd_routes_node_degree_1 = compute_odd_routes(
                graph_built, node_degree_1, num_nodes)
            return ((num_nodes - odd_routes_node_degree_1) *
                    odd_routes_node_degree_1)
