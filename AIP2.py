# Generated from: AIP2.ipynb
# Converted at: 2026-08-18T02:45:07.775Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

print("hello this is treasure hunt")
print("let's find outout the treasure")


rooms = {
    "A": ["B","C"],
    "B": ["D"],
    "C": ["D"],
    "D": ["G"],
    "G": [""]
    }
print( "          A          ")
print( r"         / \         ")
print( "        B   C        ")
print( r"         \ /         ")
print( "          D         " )
print( "          |         " )
print( "          G         " )
print("rooms that are mapped:",rooms)

def bfs(start,goal):
  to_do = [start]
  visited=[]
  order = []
  while to_do:
    room = to_do.pop(0)
    if room in visited:
      continue
    visited.append(room)
    order.append(room)
    if (room==goal):
      return order
    for nxt in rooms[room]:

        to_do.append(nxt)
  print( bfs('A','G') )
  print(order)
  print(len(order))



#dfs
def dfs(start,goal):
  to_do = [start]
  visited=[]
  order = []
  while to_do:
    room = to_do.pop()
    if room in visited:
      continue
    visited.append(room)
    order.append(room)
    if (room==goal):
      return order
    for nxt in rooms[room]:

        to_do.append(nxt)
  print( dfs('A','G') )
  print( order)
  print(len(order))


from os import path

rooms = {
    "A": ["B","C"],
    "B": ["D"],
    "C": ["D"],
    "D": ["G"],
    "G": [""]
    }

door_cost ={("A","B"):1,
("B","D"):1,
("A","C"):5,
("C","D"):1,
("D","G"):1,
("B","C"):1 # Added missing door cost
}

def path_cost(path):
  total_cost = 0
  for i in range (len(path)-1):
    door=(path[i],path[i+1])
    total_cost=total_cost+door_cost[door]
  return total_cost

# Corrected BFS function
def bfs(start,goal):
  to_do = [start]
  visited=[]
  order = []
  while to_do:
    room = to_do.pop(0)
    if room in visited:
      continue
    visited.append(room)
    order.append(room)
    if (room==goal):
      return order
    for nxt in rooms[room]:
        if nxt and nxt not in visited and nxt not in to_do: # Handle empty string and avoid re-adding
          to_do.append(nxt)
  return order

# Corrected DFS function
def dfs(start,goal):
  to_do = [start]
  visited=[]
  order = []
  while to_do:
    room = to_do.pop()
    if room in visited:
      continue
    visited.append(room)
    order.append(room)
    if (room==goal):
      return order
    for nxt in rooms[room]:
        if nxt and nxt not in visited and nxt not in to_do: # Handle empty string and avoid re-adding
          to_do.append(nxt)
  return order


path1=["A","B","C","D","G"]
path2=["A","C","D","G"]
print("path1 A->B->D->G costs:",path_cost(path1))
print("path2 A->C->D->G costs:",path_cost(path2))
cost1=path_cost(path1)
cost2=path_cost(path2)
if cost1<cost2:
  best_path=path1
  best_cost=cost1 # Corrected: assigned cost instead of path
else:
  best_path=path2
  best_cost=cost2 # Corrected: assigned cost instead of path
print("path1 cost:",cost1)
print("path2 cost:",cost2)
print()
print("the cheapest path is:",best_path,"with cost:",best_cost)

bfs_order=bfs('A','G')
dfs_order=dfs('A','G') # Ensured dfs_order is also calculated
print(bfs_order) # Corrected: used bfs_order instead of undefined 'result'
print("-"*40)
print("BFS(nearest first)checked:",len(bfs_order),"rooms->",bfs_order)
print("DFS(deepest first)checked:",len(dfs_order),"rooms->",dfs_order)
print("cheapest path:",best_path,"with cost",best_cost)
print("-"*40)
print()
print("what we learned:")
print("BFS checks  the nearest rooms first(spread out).")
print("DFS dives deep down one path first.")
print("cheapest path counts door costs and pucks the lowest total.")
door_cost[("A","B")] = 4
door_cost[("A","C")] = 1
cost1=path_cost(["A","B","D","G"])
cost2=path_cost(["A","C","D","G"])
print("now path1 (through B)costs:",cost1)
print("now path1 (through B)costs:",cost1)
if cost1<cost2:
  print("cheapest path is now path1:A->B->D->G")
else:
  print("cheapest path is now path2:A->C->D->G")