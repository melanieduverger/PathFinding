from math import *


def r3(x):
    if x == 0:
        return 0
    return int(exp(log(x) / 3))

def load_matrix(filename, dimensions):
        
        #taille de la matrice
        f = open(filename)
        current_line  = f.readline()
        counter = 0
        while current_line:
                counter+=1
                current_line  = f.readline()
        f.close()
        print "Nombre de cases : %d "%counter;

        if(dimensions == 2):
                print "Matrice sur %d dimensions"%dimensions;
                print "Matrice de %d par %d" %(int(sqrt(counter)), int(sqrt(counter)))
                #initialisation de la matrice
                grid = [[0] * int(sqrt(counter)) for i in range(int(sqrt(counter)))]

                f = open(filename)
                current_line  = f.readline()

                while current_line:
                    #traitement de la ligne courante
                    split = current_line.split(" ");
                    grid[int(split[0])][int(split[1])] = int(split[2]);
                        #     x                             y                                       0 ou 1
                    current_line = f.readline()
                f.close()

        elif(dimensions == 3):
                print "Matrice sur %d dimensions"%dimensions;
                print "Matrice de %d par %d par %d" %(r3(counter),r3(counter),r3(counter))
        
        print "---------------------"

        return grid;
       
#or line in grid:
#        for case in line:              
