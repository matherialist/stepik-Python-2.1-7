# функция поиска пути между двумя вершинами графа
def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not graph.__contains__(start):
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath:
                return newpath
    return None


exceptions_hierarchy = {}
exceptions = []

n = int(input())
for i in range(n):
    s = input()
    try:
        child, parents = s.split(' : ')
        parents = parents.split()
        exceptions_hierarchy[child] = parents
    except ValueError:
        exceptions_hierarchy[s] = s

m = int(input())
for i in range(m):
    e = input()
    exceptions.append(e)

for i, e in enumerate(exceptions):
    for j, ex in enumerate(exceptions):
        if j < i and find_path(exceptions_hierarchy, e, ex):
            print(e)
            break
# check
