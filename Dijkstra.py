#DO NOT CHANGE ANY EXISTING CODE IN THIS FILE
import sys
class Dijkstra:


    def Dijkstra_alg(self, n, e, mat, s):
         #Write your code here to calculate shortest paths and usp values from source to all vertices
		 #This method will have four inputs (Please see testcase file)
		 #This method should return a two dimensional array as output (Please see testcase file)
         priority_queue = []
         visited_set = set()
         u = [-1 for i in range(0, n+1)]
         d = [sys.maxsize for i in range(0, n+1)]
         for i in range(1, n+1):
              priority_queue.append(i)
         d[s] = 0
         u[s] = 1
         while priority_queue != []:
              v = -1
              min = sys.maxsize
              for i in priority_queue:
                   if d[i] < min:
                        min = d[i]
                        v = i
              priority_queue.remove(v)
              visited_set.add(v)
              adj = []
              for i in mat:
                   if (i[0] == i[1]) and (i[0] == v):
                        continue
                   elif i[0] == v:
                        adj.append((i[1], i[2]))
                   elif i[1] == v:
                        adj.append((i[0], i[2]))
              for i in ad:
                   if i[0] not in visited_set:
                        if d[v] + i[1] < d[i[0]]:
                             d[i[0]] = d[v] + i[1]
                             u[i[0]] = 1
                        elif d[v] + i[1] == d[i[0]]:
                             u[i[0]] = 0
         usp_mat = []
         for i in range(1, n+1):
              usp_mat.append([d[i], u[i]])

         return usp_mat

