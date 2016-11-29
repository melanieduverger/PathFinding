import time
import numpy
from heapq import *
from math import sqrt

#taille de la matrice
f = open('matrix.txt')
current_line  = f.readline()
counter = 0
while current_line:
        counter+=1
        current_line  = f.readline()
f.close()

print "Nombre de cases : %d "%counter;
print "Matrice de %d par %d" %(int(sqrt(counter)), int(sqrt(counter)))
print "---------------------"

#initialisation de la matrice
grid = [[0] * int(sqrt(counter)) for i in range(int(sqrt(counter)))]

f = open('matrix.txt')
current_line  = f.readline()

while current_line:
    #traitement de la ligne courante
    grid[int(current_line[:1])][int(current_line[1:2])] = int(current_line[2:3]);
        #     x                             y                                       0 ou 1
    current_line = f.readline()
f.close()

def heuristic(a, b):
    return (b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2

def astar(array, start, goal):

    voisins = [(0,1),(0,-1),(1,0),(-1,0)]

    close_set = set()
    precedent_location = {}
    gscore = {start:0}
    fscore = {start:heuristic(start, goal)}
    oheap = []

    heappush(oheap, (fscore[start], start))
    
    while oheap:

        current_location = heappop(oheap)[1]

        if current_location == goal:
            data = []
            while current_location in precedent_location:
                data.append(current_location)
                current_location = precedent_location[current_location]
            return data

        close_set.add(current_location)
        for i, j in voisins:
            neighbor = current_location[0] + i, current_location[1] + j            
            tentative_g_score = gscore[current_location] + heuristic(current_location, neighbor)
            if 0 <= neighbor[0] < array.shape[0]:
                if 0 <= neighbor[1] < array.shape[1]:                
                    if array[neighbor[0]][neighbor[1]] == 1:
                        continue
                else:
                    # array bound y walls
                    continue
            else:
                # array bound x walls
                continue
                
            if neighbor in close_set and tentative_g_score >= gscore.get(neighbor, 0):
                continue
                
            if  tentative_g_score < gscore.get(neighbor, 0) or neighbor not in [i[1]for i in oheap]:
                precedent_location[neighbor] = current_location
                gscore[neighbor] = tentative_g_score
                fscore[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                heappush(oheap, (fscore[neighbor], neighbor))
                
    return False


nmap = numpy.array(grid)

start_time = time.time()

print astar(nmap, (0,0), (2,2))

end_time = time.time()

print "---------------------"
print("Timer : %s seconds" % (end_time - start_time))
