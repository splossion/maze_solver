from graphics import Line, Point, Window


class Cell:
    def __init__(self, win: Window) -> None:
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._center = None
        self._win = win
        self._visited = False
    
    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        l = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
        if self.has_left_wall:
            self._win.draw_line(l)
        else:
            self._win.draw_line(l, "white")
        
        l = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
        if self.has_right_wall:
            self._win.draw_line(l,)
        else:
            self._win.draw_line(l, "white")
        
        l = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))    
        if self.has_top_wall:
            self._win.draw_line(l)
        else:
            self._win.draw_line(l, "white")
        
        l = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
        if self.has_bottom_wall:
            self._win.draw_line(l)
        else:
            self._win.draw_line(l, "white")
    
    def draw_move(self, to_cell, undo=False):
        center_1 = Point((self._x1+self._x2)//2, (self._y1+self._y2)//2)
        center_2 = Point((to_cell._x1+to_cell._x2)//2, (to_cell._y1+to_cell._y2)//2)
        fill_color = "red"
        if undo:
            fill_color = "gray"
        self._win.draw_line(Line(center_1, center_2), fill_color=fill_color)
        
    def __repr__(self) -> str:
        return "+++"