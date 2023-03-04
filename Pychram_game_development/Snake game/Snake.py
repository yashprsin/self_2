
import curses

# Setup Window
curses.initscr()

# y, x
win = curses.newwin(20, 60, 0, 0)
win.keypad(1)
curses.noecho()
curses.curs_set(0)
win.border(0)
# -1
win.nodelay(1)

# Game logic
score = 0
while True:
    event = win.getch()
    #..


curses.endwin()
print(f"Final Score = {score}")

