from collections import defaultdict
import queue


class DirectedGraph(object):
    def __init__(self):
        self.adjacency_list = defaultdict(lambda: set())

    def add_edge(self, v, w=None):
        if w:
            self.adjacency_list[v].add(w)
        else:
            self.adjacency_list[v] = {}

    def __str__(self):
        text = [str(key) + ' -> ' + str(value) + '\n'
                for key, value in self.adjacency_list.items()]
        return ''.join(text)

    def indegree(self, v):
        degree = 0
        for value in self.adjacency_list.values():
            if v in value:
                degree += 1
        return degree

    def top_sort(self):
        q = queue.Queue()
        indgs = dict()
        top_order = []
        counter = 0

        for vname in self.adjacency_list.keys():
            i = self.indegree(vname)
            if i == 0:
                q.put(vname)
            else:
                indgs[vname] = i

        while not q.empty():
            v = q.get()
            top_order.append(v)
            counter += 1

            for adjvtx in self.adjacency_list[v]:
                indgs[adjvtx] -= 1
                if indgs[adjvtx] == 0:
                    q.put(adjvtx)

        if counter != len(self.adjacency_list):
            print('graph has a circle')
        else:
            return top_order




dg = DirectedGraph()

dg.add_edge(1, 2)
dg.add_edge(1, 3)
dg.add_edge(1, 4)
dg.add_edge(2, 4)
dg.add_edge(2, 5)
dg.add_edge(3, 6)
dg.add_edge(4, 3)
dg.add_edge(4, 6)
dg.add_edge(4, 7)
dg.add_edge(5, 4)
dg.add_edge(5, 7)
dg.add_edge(6)
dg.add_edge(7, 6)

print(dg)

print(dg.top_sort())
