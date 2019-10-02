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


n = int(input())
exceptions = {}
exs = []
for i in range(n):
    s = input()
    try:
        a, b = s.split(' : ')
        anc = b.split()
        exceptions[a] = anc
    except:
        exceptions[s] = s

m = int(input())
for i in range(m):
    a = input()
    exs.append(a)

for i, e in enumerate(reversed(exs)):
    for j, ex in enumerate(reversed(exs)):
        if j > i and find_path(exceptions, e, ex):
            print(e)
            break