# testing snake class
import sys

import pprint
import tensorflow as tf
from snake import Snake



def snake_test():
    # initialize snake
    snake = Snake(5, 5, 3, "up", 10)
    # print snake
    pprint.pprint(snake.board)
    # print next position
    print(snake.next_position())
    # move snake
    snake.step()
    # print snake
    pprint.pprint(snake.board)

def gpu_test():
    gpus = tf.config.list_physical_devices('GPU')
    if gpus:
        for i, gpu in enumerate(gpus):
            print("GPU", i+1, ":", gpu)
    else:
        print("No GPUs found")

if __name__ == "__main__":
    # get args and run specific test
    if len(sys.argv) > 1:
        if sys.argv[1] == "snake":
            snake_test()
        elif sys.argv[1] == "gpu":
            gpu_test()