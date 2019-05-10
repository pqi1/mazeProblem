from collections import deque
import numpy

my_maze = numpy.array([[1,0,1,0,1],
                       [1,0,1,1,0],
                       [1,1,1,0,1],
                       [0,0,1,1,0],
                       [1,1,0,1,1]])

m_row = 0
m_col = 0
queue = deque([(m_row, m_col)])
anser_list = []

while queue:
    m_row, m_col = queue.popleft()
    anser_list.append((m_row,m_col))
    my_maze[m_row, m_col] = 2
    if m_row == 4 and m_col == 4:
        break
    if m_col < 4 and my_maze[m_row, m_col + 1] == 1:
        queue.append([m_row, m_col + 1])
    if m_col > 0 and my_maze[m_row, m_col - 1] == 1:
        queue.append([m_row, m_col - 1])
    if m_row < 4 and my_maze[m_row + 1, m_col] == 1:
        queue.append([m_row+1, m_col])
    if m_row > 0 and my_maze[m_row - 1, m_col] == 1:
        queue.append([m_row - 1, m_col])

print(anser_list)
print(my_maze)
