import random
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.cm as cm

num_rows = int(input("Rows: ")) # number of rows
num_cols = int(input("Columns: ")) # number of columns

M = np.zeros((num_rows,num_cols,4), dtype=np.uint8)

image = np.zeros((num_rows*10,num_cols*10), dtype=np.uint8)

wall_list = set();
# up down left right
count = 0;
record = dict();
for i in range(num_rows):
    for j in range(num_cols):
        if i > 0:
            wall_list.add((i,j,0))
        if i < num_rows - 1:
            wall_list.add((i,j,1))
        if j > 0:
        	wall_list.add((i,j,2))
        if j < num_cols - 1:
        	wall_list.add((i,j,3))
        record[(i,j)] = count;
        count += 1;

while wall_list:
    r,c,w = random.choice(tuple(wall_list))
    wall_list.remove((r,c,w))
    x = r
    y = c
    z = w
    if w == 0:
        x -= 1
        z = 1
    elif w == 1:
    	x += 1
    	z = 0
    elif w == 2:
    	y -= 1
    	z = 3
    elif w == 3:
    	y += 1
    	z = 2
    if (record[(r,c)] == record[(x,y)]):
    	continue
    tmp = record[(x,y)]
    for key in record:
    	if record[key] == tmp:
    		record[key] = record[(r,c)]
    M[r,c,w] = 1
    M[x,y,z] = 1



# Open the walls at the start and finish
M[0,0,2] = 1
M[num_rows-1,num_cols-1,3] = 1

# Generate the image for display
for row in range(0,num_rows):
    for col in range(0,num_cols):
        cell_data = M[row,col]
        for i in range(10*row+2,10*row+8):
            image[i,range(10*col+2,10*col+8)] = 255
        if cell_data[2] == 1:
            image[range(10*row+2,10*row+8),10*col] = 255
            image[range(10*row+2,10*row+8),10*col+1] = 255
        if cell_data[0] == 1:
            image[10*row,range(10*col+2,10*col+8)] = 255
            image[10*row+1,range(10*col+2,10*col+8)] = 255
        if cell_data[3] == 1:
            image[range(10*row+2,10*row+8),10*col+9] = 255
            image[range(10*row+2,10*row+8),10*col+8] = 255
        if cell_data[1] == 1:
            image[10*row+9,range(10*col+2,10*col+8)] = 255
            image[10*row+8,range(10*col+2,10*col+8)] = 255


# Display the image
plt.imshow(image, cmap = cm.Greys_r)
plt.show()
