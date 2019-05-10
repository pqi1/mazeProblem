import random
import numpy
import matplotlib.pyplot as pyplot

def maze_info(height = 61, width = 91):
    shape = (height, width)
    maze_matrix = numpy.ones(shape)

    for i in range(0, height, 2):
        maze_matrix[i, :] = 0

    for j in range(0, width, 2):
        maze_matrix[:, j] = 0

    m_row = 1
    m_col = 1
    stack = [(m_row, m_col)]

    while stack:
        maze_matrix[m_row, m_col] = 2
        direct_list = []
        if m_col < (width - 2) and maze_matrix[m_row, m_col + 2] == 1:
            direct_list.append('R')
        if m_col > 2 and maze_matrix[m_row, m_col - 2] == 1:
            direct_list.append('L')
        if m_row < (height - 2) and maze_matrix[m_row + 2, m_col] == 1:
            direct_list.append('D')
        if m_row > 2 and maze_matrix[m_row - 2, m_col] == 1:
            direct_list.append('U')

        if len(direct_list):
            dir = random.choice(direct_list)
            if dir == 'R':
                maze_matrix[m_row, m_col + 2] = 2
                maze_matrix[m_row, m_col + 1] = 2
                m_col = m_col + 2
                stack.append([m_row, m_col])
            if dir == 'L':
                maze_matrix[m_row, m_col - 2] = 2
                maze_matrix[m_row, m_col - 1] = 2
                m_col = m_col - 2
                stack.append([m_row, m_col])
            if dir == 'D':
                maze_matrix[m_row + 2, m_col] = 2
                maze_matrix[m_row + 1, m_col] = 2
                m_row = m_row + 2
                stack.append([m_row, m_col])
            if dir == 'U':
                maze_matrix[m_row - 2, m_col] = 2
                maze_matrix[m_row - 1, m_col] = 2
                m_row = m_row - 2
                stack.append([m_row, m_col])
        else:
            m_row, m_col = stack.pop()

    maze_matrix[0, 0] = 2
    maze_matrix[0, 1] = 2
    maze_matrix[height - 1, width - 1] = 2
    maze_matrix[height - 1, width - 2] = 2

    return maze_matrix

ini_height = int(input("Height: "))
ini_width = int(input("Width: "))
ini_height = (ini_height // 2) * 2 + 1
ini_width = (ini_width // 2) * 2 + 1

pyplot.figure(figsize=(12,8))
pyplot.imshow(maze_info(ini_height, ini_width),cmap='Greys_r')
pyplot.xticks([]), pyplot.yticks([])
pyplot.show()

