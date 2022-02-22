from queue import PriorityQueue as pqs

from numpy import empty, put, true_divide

v=14
grapg=[[] for i in range(v)]






def bf_search(source,target,n):
	visited=[False]*n
	visited[source]=True
	pq = pqs()
	pq.put((0,source))
	while pq.empty()==False:
		u=pq.get()[1]

		print (u,end=" ")
		if u == target :
			break

		for v,c in grapg[u]:
			if visited[v]==False:
				visited[v]= True
				pq.put((c,v))
	print()



def add_edges(x,y,cost):
	grapg[x].append((y,cost))
	grapg[y].append((x,cost))

	





add_edges(0,1,3)
add_edges(0,2,6)
add_edges(0,3,5)
add_edges(1,4,9)
add_edges(1,5,8)
add_edges(2,6,12)
add_edges(2,7,14)
add_edges(3,8,7)
add_edges(8,9,5)
add_edges(8,10,6)
add_edges(9,11,1)
add_edges(9,12,10)
add_edges(9,13,2)
source=0
destination=9

bf_search(source,destination,v)

