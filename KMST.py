# Kruskals Algorithm for Minimum Spanning Tree

# Pseudo Code
# def KruskalsMST(Graph G, Weigths_array W,){
#     Sort(W) #sort edges by weight in increasing order
#     Initialize MST T = empty
#     Initialize counter i = 1
#     while(number of edges in T < n-1){
#         if(adding edge e[i] to T does not create cycle){
#             T.add(e[i])
#         }
#         i++
#     }
#     return T
# }


# Implemenation
import time


class Kruskals:
    # Add edge weight array here, this is an array of arrays in the format [u , v , w]
    edges_arr = []

    # print(edges_arr)

    def __init__(self, vertices):
        self.n = vertices
        self.m = len(self.edges_arr)

        # my input nodes start from 0 not 1 so range() exclusivitiy is fine
        self.parent = [i for i in range(vertices)]
        self.rank = [0 for i in range(vertices)]

    # Union-Find Find() implemenation without path compression
    def find(self, i):
        if self.parent[i] == i:
            return i
        else:
            leader_node = self.find(self.parent[i])
            return leader_node

    # Union-Find Union() implementation
    def union(self, parent, u, v):
        u_rep, v_rep = self.find(u), self.find(v)
        if self.rank[u_rep] < self.rank[v_rep]:
            parent[u_rep] = v_rep
        elif self.rank[u_rep] > self.rank[v_rep]:
            parent[v_rep] = u_rep
        else:
            parent[v_rep] = u_rep
            self.rank[u_rep] += 1

    # Kruskals
    def kruskals(self):
        start_time = time.time_ns()
        # The sorted() function in python uses Timsort, a nlogn time complexity sort
        self.edges_arr = sorted(self.edges_arr, key=lambda fn: fn[2])

        mst = []
        i = 0
        while len(mst) < self.n - 1:
            u, v, w = self.edges_arr[i]

            if self.find(u) != self.find(v):
                mst.append([u, v, w])
                self.union(self.parent, u, v)

            i += 1
        print(mst)
        print(time.time_ns() - start_time)


# Calling my function and instantiating a graph object with the number of vertices
graph = Kruskals(31)
graph.kruskals()
# I print out the number of edges just for read easibility
print(len(graph.edges_arr))
