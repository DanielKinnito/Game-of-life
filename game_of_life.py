import time
import random

def dead_state(width: int, height: int):
    dead_board = [[0] * width for _ in range(height)]
    return dead_board

def random_state(width: int, height: int):
    board_state = dead_state(width, height)
    
    for i in range(height):
        for j in range(width):
            random_number = random.choice([0,1])

            board_state[i][j] = random_number
    
    return board_state
def render(board_state):
    printed = []
    for row in board_state:
        temp = []
        for i in range(len(row)):
            
            if row[i] == 1:
                temp.append('#')
            else:
                temp.append('_')
        printed.append(temp)
    
    for row in printed:
        print(row)         
    
    return 

def next_board_state(initial_board_state):
    width = len(initial_board_state[0])
    height = len(initial_board_state)
    
    return_board = dead_state(width, height)
    
    for i in range(len(initial_board_state)):
        for j in range(len(initial_board_state[0])):
            count = 0
            
            for x in range(max(0, i - 1), min(height, i + 2)):
                for y in range(max(0, j - 1), min(width, j + 2)):
                    count += initial_board_state[x][y]
            
            count -= initial_board_state[i][j]  # Subtract the current cell itself
            
            if initial_board_state[i][j] == 1:
                if count <= 1 or count >= 4:
                    return_board[i][j] = 0
                else:
                    return_board[i][j] = 1
            else:
                if count == 3:
                    return_board[i][j] = 1
    
    return return_board

def load_board_state(filename):
    board_state = []
    
    with open(filename, 'r') as file:
        
        for line in file:
            row = line.strip()
            row = [int(char) for char in row]
            
            board_state.append(row)
    
    return board_state

def run_forever(init_state):
    next_state = init_state
    while True:
        render(next_state)
        next_state = next_board_state(next_state)
        time.sleep(0.6)

if __name__ == "__main__":
    init_state = load_board_state('./load-files/toad.txt')

    run_forever(init_state)