#Program1* 
#Simple Program for BFS Traversal without using Functions*
Tree = {
  5 : [3,7],
  3 : [2,4],
  7 : [8],
  2 : [],
  4 : [],
  8 : []
  }

queue = [5]
visited = []
while queue:
  m = queue.pop(0)
  visited.append(m)
  for child in Tree[m]:
    queue.append(child) 

print(visited)