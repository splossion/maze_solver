from cell import Cell
import random
import time


class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win = None, seed = None) -> None:
        self.path = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._seed = seed
        if self._seed is not None:
            self._seed = random.seed(seed)
        self._create_cells()
        
        self._break_walls_r(random.randint(0,num_rows-1), random.randint(0, num_cols-1))
        for i in range(self._num_rows):
            for j in range(self._num_cols):
                self._draw_cell(i, j)
        self._reset_cells_visited()
        
        
    def _create_cells(self):
        self._cells = []
        for i in range(self._num_rows):
            row_cells = []
            for j in range(self._num_cols):
                row_cells.append(Cell(self._win))
            self._cells.append(row_cells)
            
        self._break_entrance_and_exit()
    
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._cells[-1][-1].has_bottom_wall = False
                
    def _draw_cell(self, i, j):
        if self._win is None:
            return
        pos_x = self._x1 + j*self._cell_size_x
        pos_y = self._y1 + i*self._cell_size_y
        self._cells[i][j].draw(pos_x, pos_y, pos_x+self._cell_size_x, pos_y+self._cell_size_y)
        self._animate()
    
    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        
    def _break_walls_r(self, i: int, j: int):
        current_cell = self._cells[i][j]
        current_cell._visited = True
        current_cell: Cell
        while 1:
            to_visit = []
            movements = [(0, -1),
                         (-1, 0), (1,0),
                         (0, 1)
                         ]
            for mov in movements:
                ni, nj = i + mov[0], j + mov[1]
                if 0 <= ni < self._num_rows and 0 <= nj < self._num_cols:
                    if not self._cells[ni][nj]._visited:
                        to_visit.append((ni, nj))
        
            
            if len(to_visit) == 0:
                return
            ni, nj = random.choice(to_visit) # contains the tuple (ni, nj)
            
            if ni > i and j == nj:
                current_cell.has_bottom_wall = False
                self._cells[ni][nj].has_top_wall = False
            elif ni < i and j == nj:
                current_cell.has_top_wall = False
                self._cells[ni][nj].has_bottom_wall = False
            elif ni == i and nj < j:
                current_cell.has_left_wall = False
                self._cells[ni][nj].has_right_wall = False
            elif ni == i and nj > j:
                current_cell.has_right_wall = False
                self._cells[ni][nj].has_left_wall = False
            self._break_walls_r(ni, nj)
    
    def _reset_cells_visited(self):
        for i in range(self._num_rows):
            for j in range(self._num_cols):
                self._cells[i][j]._visited = False
    
    def solve(self):
        return self._solve_r(0, 0)
    
    def _solve_r(self, i, j):
        self.path.append((i,j))
        time.sleep(0.05)
        self._animate()
        if i == self._num_rows-1 and j == self._num_cols-1:
            return True
        current_cell = self._cells[i][j]
        current_cell: Cell
        current_cell._visited = True
        
        if self._num_cols-1 > j and not current_cell.has_right_wall:
            to_cell = self._cells[i][j+1]
            if not to_cell._visited:
                current_cell.draw_move(to_cell)
                if self._solve_r(i, j+1):
                   return True
                else:
                    current_cell.draw_move(to_cell, undo = True)
        
        if 0 < j and not current_cell.has_left_wall:
            to_cell = self._cells[i][j-1]
            if not to_cell._visited:
                current_cell.draw_move(to_cell)
                if self._solve_r(i, j-1):
                    return True
                current_cell.draw_move(to_cell, undo = True)
        
        if self._num_rows-1 > i and not current_cell.has_bottom_wall:
            to_cell = self._cells[i+1][j]
            if not to_cell._visited:
                current_cell.draw_move(to_cell)
                if self._solve_r(i+1, j):
                    return True
                current_cell.draw_move(to_cell, True)
        
        if 0 < i and not current_cell.has_top_wall:
            to_cell = self._cells[i-1][j]
            if not to_cell._visited:
                current_cell.draw_move(to_cell)
                if self._solve_r(i-1, j):
                    return True
                current_cell.draw_move(to_cell, undo = True)
                
        self.path.pop()
        return False