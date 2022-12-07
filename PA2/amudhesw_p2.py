
class Graph:
 
    def __init__(self, vertices):
        '''
        Initialize
            initialize list "graph"
            initialze no. of vertices V
        '''
        self.V = vertices  
        self.graph = []

    def addEdge(self, u, v, w):
        '''
        Append into graph, a List containing 
            u : Source Vertex  
            v : Destination vertex 
            w : the weight of the edge between the two 
        '''
        self.graph.append([u, v, w])
 
    
    def find(self, parent, i):
        '''
        A utility function to find set of an element i
        (truly uses path compression technique)
        '''
        if parent[i] != i:
          # Reassignment of node's parent to root node as
          # path compression requires
            parent[i] = self.find(parent, parent[i])
        return parent[i]
 
    
    def union(self, parent, rank, x, y):
        '''
        A function that does union of two sets of x and y
        (uses union by rank)
        '''
        
        # Attach smaller rank tree under root of
        # high rank tree (Union by Rank)
        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[x] > rank[y]:
            parent[y] = x
 
        # If ranks are same, then make one as root
        # and increment its rank by one
        else:
            parent[y] = x
            rank[x] += 1
 
    
    def KruskalMST(self):
 
        result = []  # This will store the resultant MST
 
        # An index variable, used for sorted edges
        i = 0
 
        # An index variable, used for result[]
        e = 0
 
        # Step 1:  Sort all the edges in
        # non-decreasing order of their
        # weight.  If we are not allowed to change the
        # given graph, we can create a copy of graph
        self.graph = sorted(self.graph,
                            key=lambda item: item[2])
 
        parent = []
        rank = []
 
        # Create V subsets with single elements
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
 
        # Number of edges to be taken is equal to V-1
        while e < self.V - 1:
 
            # Step 2: Pick the smallest edge and increment
            # the index for next iteration
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
 
            # If including this edge doesn't
            # cause cycle, then include it in result
            # and increment the index of result
            # for next edge
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
            # Else discard the edge
 
        minimumCost = 0
        for u, v, weight in result:
            minimumCost += weight
            # print("%d -- %d == %d" % (u, v, weight))
        # print("Minimum Spanning Tree", minimumCost)
        return minimumCost


 


def main():
    n, m = input().split()
    edges = []

    for i in range(int(m)):
      src, dest, weight = input().split()
      edges.append((int(src), int(dest), int(weight)))

    g = Graph(int(n))
    for edge in edges:
      g.addEdge(edge[0]-1, edge[1]-1, edge[2])
    print(g.KruskalMST())

if __name__ == "__main__":
    main()