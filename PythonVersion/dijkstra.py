import time
from math import sqrt
from functions import load_matrix

found = False;
f_x = 0;
f_y = 0;

grid = load_matrix("matrix.txt", 2)

def search(x, y,x_end,y_end):
        grid[x_end][y_end] = 2;
        global found
        global f_x
        global f_y
        # DEBUG- ffichage de la matrice à chaque déplacement
        ###print grid[0];print grid[1];print grid[2];
        ###print "---"

        #Afficher les déplacements

        print '(%d, %d), ' % (x, y)
        
        
        if grid[x][y] == 2:
                found = True;
                f_x=x
                f_y=y
                return True
        elif grid[x][y] == 1:
                return False
        elif grid[x][y] == 3:
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


