g={
    0:[1,2],
    1:[0,3,4],
    2:[0,3],
    3:[1,2,4],
    4:[3,1]
}
def dfs(g,s):
  vis[s]=1
  print(s)
  for c in g[s]:
    if(vis[c]!=1):
      dfs(g,c)
vis=[0]*5
dfs(g,0)


def bfs(g,s):
  q=[s];
  vis=[s];
  while q:
    curr=q.pop(0)
    print(curr)
    for c in g[curr]:
      if c not in vis:
        q.append(c)
        vis.append(c)
bfs(g,0)
