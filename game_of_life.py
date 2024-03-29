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

render(random_state(5,5))


print(random_state(5,5))