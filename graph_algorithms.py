def bfs(graph, start_node, search_node=None):
    # graph: a dictionary representing the graph to be traversed.
    # start_node: a string representing the starting node of the traversal.
    # search_node: an optional string representing the node being searched for in the graph.
    # Note: If the given start_node belongs to one strongly connected component then the other nodes belong to that
           # particular component can only be traversed. But the nodes belonging to other components must not be traversed
           # if those nodes were not reachable from the given start_node.

    #The output depends on whether the search_node is provided or not:
        #1. If search_node is provided, the function returns 1 if the node is found during the search and 0 otherwise.
        #2. If search_node is not provided, the function returns a list containing the order in which the nodes were visited during the search.

    #Useful code snippets (not necessary but you can use if required)
    visited = set()
    queue = [start_node] 
    if search_node and start_node == search_node:
        
        return 1  # search node found
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
        for child_nodes in sorted(graph[node]):
            if child_nodes not in visited:
                queue.append(child_nodes)
                visited.add(child_nodes)
            
            if search_node and child_nodes == search_node:
                return 1
                
    if search_node is not None:
        return 0  # search node not found
    else: 
        path = list(visited)
        return path  # search node not provided, return entire path [list of nconst values of nodes visited]


def dfs(graph, start_node, visited=None, path=None, search_node=None):
    # graph: a dictionary representing the graph
    # start_node: the starting node for the search
    # visited: a set of visited nodes (optional, default is None)
    # path: a list of nodes in the current path (optional, default is None)
    # search_node: the node to search for (optional, default is None)
    # Note: If the given start_node belongs to one strongly connected component then the other nodes belong to that
           # particular component can only be traversed. But the nodes belonging to other components must not be traversed
           # if those nodes were not reachable from the given start_node.

    # The function returns:
        # 1. If search_node is provided, the function returns 1 if the node is found and 0 if it is not found.
        # 2. If search_node is not provided, the function returns a list containing the order in which the nodes were visited during the search.
    
    #Useful code snippets (not necessary but you can use if required)
    if visited is None:
        visited = set()
    if path is None:
        path = []
    stack = [start_node]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            path.append(node)
            if node == search_node:
                return 1
            for child_nodes in sorted(graph[node]):
                if child_nodes not in visited:
                    stack.append(child_nodes)
                    
    if search_node is not None:
        return 0
    else:
        #print(path)
        return path  # search node not provided, return entire path [list of nconst id's of nodes visited]

    
    
    



def dijkstra(graph, start_node, end_node):
    # graph: a dictionary representing the graph where the keys are the nodes and the values
            # are dictionaries representing the edges and their weights.
    # start_node: the starting node to begin the search.
    # end_node: the node that we want to reach.

    # Outputs:
        #1. If the end_node is not reachable from the start_node, the function returns 0.

        #2. If the end_node is reachable from the start_node, the function returns a list containing three elements:
                #2.1 The first element is a list representing the shortest path from start_node to end_node.
                     #[list of nconst values in the visited order]
                #2.2 The second element is the total distance of the shortest path.
                     #(summation of the distances or edge weights between minimum visited nodes)
                #2.3 The third element is Hop Count between start_node and end_node.

    # Return the shortest path and distances
    # return [path, distance, hop_count]
    return 1


def dfs_discover(graph, node, visited, stack):
    visited.add(node)
    for child_nodes in graph[node]:
        if child_nodes not in visited:
            dfs_discover(graph, child_nodes, visited, stack)
    stack.append(node)
def transpose_graph(graph):
    transposed_graph = {}
    for node in graph:
        for child_nodes in graph[node]:
            if child_nodes not in transposed_graph:
                transposed_graph[child_nodes] = set()
            transposed_graph[child_nodes].add(node)
    return transposed_graph
def kosaraju_dfs(graph, node, visited, scc):
    visited.add(node)
    scc.add(node)
    for child_nodes in graph[node]:
        if child_nodes not in visited:
            kosaraju_dfs(graph, child_nodes, visited, scc)
# (strongly connected components)
def kosaraju(graph):
    # graph: a dictionary representing the graph where the keys are the nodes and the values
            # are dictionaries representing the edges and their weights.
    #Note: Here you need to call dfs function multiple times so you can Implement seperate
         # kosaraju_dfs function if required.
    stack = []
    visited = set()
    for node in graph:
        if node not in visited:
            dfs_discover(graph, node, visited, stack)

    transposed_graph = transpose_graph(graph)

    # Step 3: Perform DFS in the order determined by the stack and output each strongly connected component
    visited = set()
    component_list = []
    while stack:
        node = stack.pop()
        if node not in visited:
            component = set()
            kosaraju_dfs(transposed_graph, node, visited, component)
            component_list.append(component)
    return component_list
    #The output:
        #list of strongly connected components in the graph,
          #where each component is a list of nodes. each component:[nconst2, nconst3, nconst8,...] -> list of nconst id's.
    # return components
