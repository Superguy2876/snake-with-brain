import curses
from snake import Snake

def main(stdscr):
    # key mapping allow arrow keys or wasd
    key_map = {curses.KEY_UP: "up", curses.KEY_DOWN: "down", curses.KEY_LEFT: "left", curses.KEY_RIGHT: "right"
               , ord("w"): "up", ord("s"): "down", ord("a"): "left", ord("d"): "right"}

    # initialize snake
    snake = Snake(5, 5, 2, "up", 20)
    # print snake
    stdscr.addstr(str(snake.game_str()))
    # start game loop
    while True:
        # get key input
        key = stdscr.getch()
        # check if key is in key_map
        if key in key_map:
            # change direction
            snake.turn(key_map[key])
        # move snake
        snake.step()
        # print board replacing previous board
        stdscr.addstr(0, 0, str(snake.game_str()))

if __name__ == "__main__":
    curses.wrapper(main)