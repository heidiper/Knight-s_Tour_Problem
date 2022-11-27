import numpy as np

class KnightTour():
  DIRECTIONS = [(-2, 1), (-1, 2), (1, 2), (2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
  def print_board(self, board):
    for i in range(0, len(board)):
        for j in range(0, len(board)):print('%3d ' % board[i][j], end='')
        print('\n')
        
  def is_inside_board(self, r, c, size):return 0 <= r < size and 0 <= c < size
  def get_degree_map(self, size):
    degree_map = np.zeros((size, size))
    for r in range(size):
      for c in range(size):
        for dr, dc in self.DIRECTIONS:
          if self.is_inside_board(r + dr, c + dc, size):degree_map[r, c] = degree_map[r, c] + 1
    return degree_map

  def get_next_move_and_degree(self, cur_row, cur_col, size, degree_map):
    min_deg = float('inf')
    for dr, dc in self.DIRECTIONS:
      nr, nc = cur_row + dr, cur_col + dc
      if not self.is_inside_board(nr, nc, size):
        continue
      new_deg = degree_map[nr, nc] - 1
      degree_map[nr, nc] = new_deg
      if 0 <= new_deg < min_deg:
        min_deg = new_deg
        next_row, next_col = nr, nc
    return next_row, next_col

  def get_input(self):
    while True:
      [start_row, start_col] = input('Please input a start postition (splitted by the space):').split()
      [start_row, start_col] = [int(start_row), int(start_col)]
      size = int(input('\nPlease input the chessboard size (an integer):'))
      if 0 <= start_row < size and 0 <= start_col < size:return size, start_row, start_col
    
  def knight_tour(self):
    size, cur_row, cur_col = self.get_input()
    chessboard = np.zeros((size, size))
    degree_map = self.get_degree_map(size)
    for i in range(size * size):
      degree_map[cur_row, cur_col] = 0
      chessboard[cur_row, cur_col] = i + 1
      if chessboard[cur_row, cur_col] == size * size:
        break
      cur_row, cur_col = self.get_next_move_and_degree(cur_row, cur_col, size, degree_map)
    self.print_board(chessboard)

sol = KnightTour()
sol.knight_tour()