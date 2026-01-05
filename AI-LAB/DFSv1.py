Tree = {
5 : [3,7],
3 : [2,4],
7 : [8],
2 : [],
4 : [],
8 : []
}
visited = []
def dfs(Tree , root):
  stack = [root]
  while stack:
    m = stack.pop(0)
    visited.append(m)
    for child in Tree[m]:
      dfs(Tree , child)
  return visited
dfs(Tree,5)
print('DFS traversal=',visited)