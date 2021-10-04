from collections import defaultdict

class Graph:

    def __init__(self,v):
        self.graph = defaultdict(list)
        self.V = v

       

    def append(self,u,v):
        self.graph[u].append(v)

    def sort_util(self,v,visited,ele_stack):
        visited[v] = True
        for node in self.graph[v]:
            if visited[node] == False:
                self.sort_util(node,visited,ele_stack)
        ele_stack.insert(0,v)

    def topological_sort(self):
        visited = [False]*self.V
        ele_stack =[]
        for node in range(self.V):
            if visited[node] == False:
                self.sort_util(node,visited,ele_stack)
        print(ele_stack)

        
g = Graph(4)
g.append(4,1);
g.append(4,2);
g.append(3,2);
g.append(4,3);
g.append(1,3);


print("The Topological Sort is:  ")

g.topological_sort()
