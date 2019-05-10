import random
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.cm as cm

num_rows = int(input("Rows: ")) # number of rows
num_cols = int(input("Columns: ")) # number of columns

#C[l,u,r,d,visited]
C = np.zeros((num_rows,num_cols,5), dtype=np.uint8)

image = np.zeros((num_rows*10,num_cols*10), dtype=np.uint8)

# Set the entry and the exit
C[0,0,0] = 1
C[num_rows-1,num_cols-1,2] = 1

r = 0
c = 0
cell_set = [(r,c)] #The stack of visited locations

while cell_set:
    #random choose a candidate cell from the cell set
    r,c = random.choice(cell_set)
    C[r,c,4] = 1 # designate this location as visited
    cell_set.remove((r,c)) #remove the chosen cell from the cell set
    
    edges = []  #the edges set
    if c > 0:
        if C[r,c-1,4] == 1:
            edges.append('L')
        elif C[r,c-1,4] == 0:
            cell_set.append((r,c-1))
            C[r,c-1,4] = 2
    if r > 0:
        if C[r-1,c,4] == 1:
            edges.append('U')
        elif C[r-1,c,4] == 0:
            cell_set.append((r-1,c))
            C[r-1,c,4] = 2
    if c < num_cols-1:
        if C[r,c+1,4] == 1:
            edges.append('R')
        elif C[r,c+1,4] == 0:
            cell_set.append((r,c+1))
            C[r,c+1,4] = 2
    if r < num_rows-1:
        if C[r+1,c,4] == 1:
            edges.append('D')
        elif  C[r+1,c,4] == 0:
            cell_set.append((r+1,c))
            C[r+1,c,4] = 2

    # Randomly select one of these edges.
    if len(edges):
        move_direction = random.choice(edges)
        if move_direction == 'L':
            C[r,c,0] = 1
            c = c-1
            C[r,c,2] = 1
        if move_direction == 'U':
            C[r,c,1] = 1
            r = r-1
            C[r,c,3] = 1
        if move_direction == 'R':
            C[r,c,2] = 1
            c = c+1
            C[r,c,0] = 1
        if move_direction == 'D':
            C[r,c,3] = 1
            r = r+1
            C[r,c,1] = 1

# Generate the image for display
for row in range(0,num_rows):
    for col in range(0,num_cols):
        cell_data = C[row,col]
        for i in range(10*row+2,10*row+8):
            image[i,range(10*col+2,10*col+8)] = 255
        if cell_data[0] == 1:
            image[range(10*row+2,10*row+8),10*col] = 255
            image[range(10*row+2,10*row+8),10*col+1] = 255
        if cell_data[1] == 1:
            image[10*row,range(10*col+2,10*col+8)] = 255
            image[10*row+1,range(10*col+2,10*col+8)] = 255
        if cell_data[2] == 1:
            image[range(10*row+2,10*row+8),10*col+9] = 255
            image[range(10*row+2,10*row+8),10*col+8] = 255
        if cell_data[3] == 1:
            image[10*row+9,range(10*col+2,10*col+8)] = 255
            image[10*row+8,range(10*col+2,10*col+8)] = 255

# Display the image
plt.imshow(image, cmap = cm.Greys_r)
plt.show()
