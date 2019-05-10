import random
import numpy

my_maze = numpy.array([[1,0,1,0,1],
                       [1,0,1,1,0],
                       [1,1,1,0,1],
                       [0,0,1,1,0],
                       [1,1,0,1,1]])

m_row = 0
m_col = 0
stack = [(m_row, m_col)]
anser_list = []

while stack:
    anser_list.append((m_row, m_col))
    if m_row == 4 and m_col == 4:
        break
    my_maze[m_row, m_col] = 2
    direct_list = []
    if m_col < 4 and my_maze[m_row, m_col + 1] == 1:
        direct_list.append('R')
    if m_col > 0 and my_maze[m_row, m_col - 1] == 1:
        direct_list.append('L')
    if m_row < 4 and my_maze[m_row + 1, m_col] == 1:
        direct_list.append('D')
    if m_row > 0 and my_maze[m_row - 1, m_col] == 1:
        direct_list.append('U')

    if len(direct_list):
        dir = random.choice(direct_list)
        if dir == 'R':
            m_col = m_col + 1
            stack.append([m_row, m_col])
        if dir == 'L':
            m_col = m_col - 1
            stack.append([m_row, m_col])
        if dir == 'D':
            m_row = m_row + 1
            stack.append([m_row, m_col])
        if dir == 'U':
            m_row = m_row - 1
            stack.append([m_row, m_col])
    else:
        m_row, m_col = stack.pop()


print(anser_list)
print(my_maze)