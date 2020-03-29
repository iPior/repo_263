'''
CSC263 Winter 2020
Problem Set 3 Starter Code
University of Toronto Mississauga
'''

# Do NOT add any "import" statements
# Do NOT use Python dictionaries
#Graph Class
class Graph():
    def __init__(self):
        self.E = []
        self.V = []

    def add_edge(self, u, v):
        if v in self.V:
            i = self.V.index(v)
            self.E[i].append(u)
        else:
            self.V.append(v)
            i = self.V.index(v)
            self.E.append([u])
#Helpers
def cycle_helper(graph, v_index, visited, recur_visit):
    '''
    Pre:  graph is the given graph with V verticies and E edges
          v_index is index of visiting vertex in graph.V
          visited is lst of vertices with visiting status
          recur_visit is used for recursion visiting
    
    Post: return whether there exists a cycle
    '''    
    visited[v_index] = True
    recur_visit[v_index] = True
    #For every neighbour check if it has been visited
    for neighbour in graph.E[v_index]:
        neighbour_i = graph.V.index(neighbour)
        
        #If not visited, recurse in neighbour
        if visited[neighbour_i] == False:
            if cycle_helper(graph, neighbour_i, visited, recur_visit) == True:
                return True
            
        elif recur_visit[neighbour_i] == True:
            return True
        
    #Remove v from recursive visit
    recur_visit[v_index] = False
    return False
            
def check_cycle(graph):
    '''
    Pre:  graph is the given graph with V verticies and E edges
    
    Post: return whether there exists a cycle
    '''
    visited = [False] * len(graph.V)
    recur_visit = [False] * len(graph.V)
    for vertex in graph.V:
        i = graph.V.index(vertex)
        if visited[i] == False:
            if cycle_helper(graph, i, visited, recur_visit) == True:
                return True
    return False
    
def can_visit_all_cities(numCities, dependencies):
    '''
      Pre:  numCities is the number of cities to be visited
            dependencies is a list of 2-tuples representing (city1,city2) with city1 can only be visited after city2
      Post: return whether visiting all cities is possible or not

      '''
      #Build graph of dependencies
    g = Graph()
    for edge in dependencies:
        g.add_edge(edge[0], edge[1])
    for edge in dependencies:
        if edge[0] not in g.V:
            g.V.append(edge[0])
            g.E.append([])
    #Check for cycle. If there is a cycle return true
    start = g.V[0]
    if check_cycle(g):
        return 0
    #If no cycle, check if number of cities in graph == numCities
    else:
        if len(g.V) == numCities:
            return 0
    return 1
if __name__ == '__main__':
    # some small test cases
    # Case 1

    numCities1: int = 25
    dependencies1 = [('reykjavik', 'stjohns'), ('limerick', 'dublin'), ('london', 'dublin'), ('brighton', 'london'),
                    ('heidelberg', 'frankfurt'),('frankfurt', 'london'), ('frankfurt', 'dublin'),
                    ('batam', 'singapore'), ('newcastle', 'sydney'),('sandiego', 'honolulu')]

    # Case 2
    numCities2: int = 10
    dependencies2 = [('paris','madrid'),('madrid','lisbon'),('lisbon','paris')]

    assert 1 == can_visit_all_cities(numCities1, dependencies1)
    assert 0 == can_visit_all_cities(numCities2, dependencies2)
    