# snake class

import random as r

class Snake:
    def __init__(self, x: int, y: int, length: int, direction: str, boardsize: int):
        self.x = x
        self.y = y
        self.snake_head = {"x": x, "y": y}
        self.snake_body = []
        self.length = length
        self.direction = direction
        # boardsize length and width is the same
        self.board = [[0 for i in range(boardsize)] for j in range(boardsize)]
        self.game_over = False
        self.ate_food = False

        # initialize snake head = 1 body = 2
        for i in range(length):
            if direction == "up":
                # start from the end of the snake and move up
                self.snake_body.append((y + (length - i), x))
                # self.snake_body.append((y + (length - i) + 1, x))

                
            elif direction == "down":
                self.snake_body.append((y - (length - i) - 1, x))
            elif direction == "left":
                self.snake_body.append((y, x + (length - i) + 1))
            elif direction == "right":
                self.snake_body.append((y, x - (length - i) - 1))
        
        self.board[self.snake_head["y"]][self.snake_head["x"]] = 1

        for i in self.snake_body:
            self.board[i[0]][i[1]] = 2
            

        # place food
        self.place_food()
    
    def place_food(self):
        # place food randomly
        while True:
            x = r.randint(0, len(self.board) - 1)
            y = r.randint(0, len(self.board) - 1)
            if self.board[y][x] == 0:
                self.board[y][x] = 3
                break
        
    def next_position(self):
        # return next position of snake head
        if self.direction == "up":
            return {"x": self.snake_head["x"], "y": self.snake_head["y"] - 1}
        elif self.direction == "down":
            return {"x": self.snake_head["x"], "y": self.snake_head["y"] + 1}
        elif self.direction == "left":
            return {"x": self.snake_head["x"] - 1, "y": self.snake_head["y"]}
        elif self.direction == "right":
            return {"x": self.snake_head["x"] + 1, "y": self.snake_head["y"]}

    def step(self):

        np  = self.next_position()
        
        # if snake hits wall, game over
        if np["x"] < 0 or np["x"] > len(self.board) - 1 or np["y"] < 0 or np["y"] > len(self.board) - 1:
            self.game_over = True
            return

        # if snake hits itself, game over
        if self.board[np["y"]][np["x"]] == 2:
            self.game_over = True
            return
        
        # if snake eats food, increase length
        if self.board[np["y"]][np["x"]] == 3:
            self.length += 1
            self.ate_food = True
            self.place_food()

        # move snake head
        self.board[np["y"]][np["x"]] = 1

        # move snake body
        self.snake_body.append((self.snake_head["y"], self.snake_head["x"]))
        if len(self.snake_body) > self.length:
            self.board[self.snake_body[0][0]][self.snake_body[0][1]] = 0
            self.snake_body.pop(0)
        self.board[self.snake_body[-1][0]][self.snake_body[-1][1]] = 2
        
        # update snake head
        self.snake_head = np

    # def bfs(self):
    #     # return next direction to move towards food
    #     # use bfs to find shortest path to food
    #     # find food then 
    #     queue: list[tuple(int, int, str)] = []
    #     visited: list[tuple(int, int)] = []
    #     queue.append((self.snake_head["x"], self.snake_head["y"], self.direction))
    #     while 
       
        

        
    def game_str(self):
        # return board as string
        # We want to surround the board with a border, horizontal lines on top and bottom, and vertical lines on the sides
        # on the corners we want to put a + sign
        # we want to use the following characters to represent the snake head, snake body, and food
        # snake head: v^<> (down, up, left, right) depending on the direction the snake is facing
        # snake body: -|+ (horizontal, vertical, turn)
        # food: @
        # empty space: space

        # create empty string
        string = ""
        # add horizontal line on top
        string += "+ " + "- " * len(self.board) + "+\n"
        # add vertical lines on sides and snake head/body/food
        for irow, row in enumerate(self.board):
            string += "|"
            for jcol, col in enumerate(row):
                string += " "
                if col == 1:
                    if self.direction == "up":
                        string += "^"
                    elif self.direction == "down":
                        string += "v"
                    elif self.direction == "left":
                        string += "<"
                    elif self.direction == "right":
                        string += ">"
                elif col == 2:
                    # check if snake body is horizontal, vertical, or turn, use snake_body list to check
                    # get index of current snake body part, which will be the location of the current cell in the board
                    index = self.snake_body.index((irow, jcol))
                    # if index is the first index, then the snake body part is the tail, so it can't be a turn
                    # check if the previous snake body part is in the same row or column as the current snake body part
                    # if it is, then the snake body part is horizontal, otherwise it is vertical
                    if index == 0:
                        if self.snake_body[index + 1][0] == self.snake_body[index][0]:
                            string += "-"
                        else:
                            string += "|"
                        continue
                    
                    # if index is the last index, then the snake body part is just after the head, so we need to check the next snake body part and the head
                    # check if the next snake body part is in the same row or column as the next snake body part and the head
                    # if both are same row, then the snake body part is horizontal, if both are same column, then the snake body part is vertical, otherwise it is a turn
                    if index == len(self.snake_body) - 1:
                        if self.snake_body[index - 1][0] == self.snake_body[index][0] and self.snake_body[index][0] == self.snake_head["y"]:
                            string += "-"
                        elif self.snake_body[index - 1][1] == self.snake_body[index][1] and self.snake_body[index][1] == self.snake_head["x"]:
                            string += "|"
                        else:
                            string += "+"
                        continue
                        
                        
                        # if self.snake_body[index + 1][0] == self.snake_body[index][0] and self.snake_body[index + 1][0] == self.snake_head["y"]:
                        #     string += "-"
                        # elif self.snake_body[index + 1][1] == self.snake_body[index][1] and self.snake_body[index + 1][1] == self.snake_head["x"]:
                        #     string += "|"
                        # else:
                        #     string += "+"
                        # continue

                    # if index is neither the first nor the last index, then the snake body part is in the middle of the snake
                    # check if the previous and next snake body parts are in the same row or column as the current snake body part
                    # if both are same row, then the snake body part is horizontal, if both are same column, then the snake body part is vertical, otherwise it is a turn
                    if self.snake_body[index - 1][0] == self.snake_body[index][0] and self.snake_body[index + 1][0] == self.snake_body[index][0]:
                        string += "-"
                    elif self.snake_body[index - 1][1] == self.snake_body[index][1] and self.snake_body[index + 1][1] == self.snake_body[index][1]:
                        string += "|"
                    else:
                        string += "+"

                    

                elif col == 3:
                    string += "@"
                else:
                    string += " "
            string += "|\n"
        # add horizontal line on bottom
        string += "+ " + "- " * len(self.board) + "+\n"
        return string
        
        
        
        # string = ""
        # for row in self.board:
        #     for col in row:
        #         string += str(col)
        #     string += "\n"
        # return string
    
    def turn(self, direction: str):
        # check if direction is valid
        if direction == "up" and self.direction != "down":
            self.direction = direction
        elif direction == "down" and self.direction != "up":
            self.direction = direction
        elif direction == "left" and self.direction != "right":
            self.direction = direction
        elif direction == "right" and self.direction != "left":
            self.direction = direction
        
        # if direction is invalid, do nothing

        
