import time
from graphics import Window
from maze import Maze


def main():
    win = Window(800, 800)
    maze = Maze(20, 20, 5, 5, 50, 50, win)
    time.sleep(1)
    maze.solve()
    print(maze.path)
    win.wait_for_close()


main()
