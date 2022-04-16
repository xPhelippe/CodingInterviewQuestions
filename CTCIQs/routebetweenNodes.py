
graph = {
  'a':['b','c'],
  'b':[],
  'c':['f','d','e','b'],
  'd': [],
  'e':['g'],
  'f':[],
  'g':[]
}

def RouteBetweenNodes(n1, n2, graph):
  start = graph['a']

  doesRouteExist = False

  if n1 == 'a' or n2 == 'a':
    for node in graph['a']:
      doesRouteExist = doesRouteExist or RouteBetweenNodeshelp(n1,n2,graph,node,True)

  else:
    for node in graph['a']:
      doesRouteExist = doesRouteExist or RouteBetweenNodeshelp(n1,n2,graph,node,False)

  return doesRouteExist

def RouteBetweenNodeshelp(n1,n2, graph, curNode,foundOneYet):

  doesRouteExist = False
  if curNode == n1 or curNode == n2:
    if foundOneYet:
      return True
    else:
      for node in graph[curNode]:
        doesRouteExist = doesRouteExist or RouteBetweenNodeshelp(n1,n2,graph,node,True)
  else:
    if foundOneYet:
      for node in graph[curNode]:
        doesRouteExist = doesRouteExist or RouteBetweenNodeshelp(n1,n2,graph,node,True)
    else:
      for node in graph[curNode]:
        doesRouteExist = doesRouteExist or RouteBetweenNodeshelp(n1,n2,graph,node,False)
  return doesRouteExist
    





print(RouteBetweenNodes('e','d',graph))