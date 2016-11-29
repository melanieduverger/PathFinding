import time
from math import sqrt

found = False;
f_x = 0;
f_y = 0;

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

def search(x, y,x_end,y_end):
        grid[x_end][y_end] = 2;
        global found
        global f_x
        global f_y
        if grid[x][y] == 2:
                found = True;
                f_x=x
                f_y=y
                return True
        elif grid[x][y] == 1:
                #print 'wall at %d,%d' % (x, y)
                return False
        elif grid[x][y] == 3:
                #print 'visited at %d,%d' % (x, y)
                return False
        grid[x][y] = 3

        if ((x < len(grid)-1 and search(x+1, y,x_end,y_end))
            or (y > 0 and search(x, y-1,x_end,y_end))
            or (x > 0 and search(x-1, y,x_end,y_end))
            or (y < len(grid)-1 and search(x, y+1,x_end,y_end))):
                return True
        return False

start_time = time.time()

search(0,0,2,2)

print "---------------------"
print("Timer : %s seconds" % (time.time() - start_time))
if found == True:
        print 'Found at %d, %d' %(f_x, f_y)
else:
        print 'Not found'
