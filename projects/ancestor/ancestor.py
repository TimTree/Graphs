
'''
def earliest_ancestor(ancestors, starting_node, first_run=True):
    node_parents = []
    print(starting_node)
    for i in range(0, len(ancestors)):
        # print(ancestors[i][1])
        if ancestors[i][1] == starting_node:
            node_parents.append(ancestors[i][0])
    if len(node_parents) == 0:
        if first_run is True:
            return -1
        else:
            return starting_node
    else:
        node_parents.sort()
        for parent in node_parents:
            return earliest_ancestor(ancestors, parent, False)
'''

from graph import Graph

def earliest_ancestor(ancestors, starting_node):

    # Create graph
    graph = Graph()
    unique_nums = []

    # Add all vertices in graph by finding all the unique numbers in ancestors
    for ancestor in ancestors:
        for value in ancestor:
            if value not in unique_nums:
                graph.add_vertex(value)
                unique_nums.append(value)

    # Check if starting node exists. If not, return -1
    if starting_node not in unique_nums:
        return -1

    # Add in the graph edges. Have children pointing towards parents
    for ancestor in ancestors:
        graph.add_edge(ancestor[1], ancestor[0])

    # Verify vertices are correct
    # print(graph.vertices)

    # Run a modified bfs that returns all possible traversals from starting node
    combos = graph.bfs(starting_node)
    
    # If there's no combos, return -1
    if len(combos) == 0:
        return -1

    # Extract the combos with the most numbers (more numbers means higher ancestor)
    most_nums = 0
    for combo in combos:
        if len(combo) > most_nums:
            most_nums = len(combo)

    combos2 = []
    for combo in combos:
        if len(combo) == most_nums:
            combos2.append(combo)
    
    # From remaining combos, return lowest rightmost number in list
    lowest_num = None
    for combo in combos2:
        if lowest_num is None:
            lowest_num = combo[most_nums - 1]
        elif combo[most_nums - 1] < lowest_num:
            lowest_num = combo[most_nums - 1]
    return lowest_num

test_ancestors = [(100, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 100)]


print(earliest_ancestor(test_ancestors, 2322))