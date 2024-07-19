from tkinter import Tk, BOTH, Canvas

class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    
    
class Line:
    def __init__(self, p1: Point, p2: Point) -> None:
        self.p1 = p1
        self.p2 = p2
    
    def draw(self, canvas:Canvas, fill_color):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, width=2, fill=fill_color)

class Window:
    def __init__(self, width, height) -> None:
        self.__root = Tk()
        self.__root.title = "Maze Solver"
        self.__canvas = Canvas(background="white", width=width, height=height)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.__running = True
        while self.__running is True:
            self.redraw()
    
    def close(self):
        self.__running = False
        
    def draw_line(self, line: Line, fill_color="black"):
        line.draw(self.__canvas, fill_color)