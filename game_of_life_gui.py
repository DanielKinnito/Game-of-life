import time
import tkinter as tk
from tkinter import filedialog
from game_of_life import load_board_state, random_state, next_board_state

CELL_SIZE = 20  # Size of each cell in pixels

def load_file():
    filename = filedialog.askopenfilename()
    if filename:
        return load_board_state(filename)

def generate_random(width, height):
    return random_state(width, height)

def render(board_state):
    canvas.delete("all")  # Clear canvas before rendering

    for i in range(len(board_state)):
        for j in range(len(board_state[0])):
            x0 = j * CELL_SIZE
            y0 = i * CELL_SIZE
            x1 = x0 + CELL_SIZE
            y1 = y0 + CELL_SIZE

            if board_state[i][j] == 1:
                canvas.create_rectangle(x0, y0, x1, y1, fill="black")
            else:
                canvas.create_rectangle(x0, y0, x1, y1, fill="white")

def start_game():
    if selected_option.get() == "Load from File":
        init_state = load_file()
    elif selected_option.get() == "Generate Random":
        width = int(width_entry.get())
        height = int(height_entry.get())
        init_state = generate_random(width, height)
    else:
        return

    run_game(init_state)

def run_game(init_state):
    while True:
        render(init_state)
        init_state = next_board_state(init_state)
        root.update()
        time.sleep(0.4)

root = tk.Tk()
root.title("Game of Life")

selected_option = tk.StringVar()
selected_option.set("Load from File")

file_button = tk.Radiobutton(root, text="Load from File", variable=selected_option, value="Load from File")
file_button.pack()

random_button = tk.Radiobutton(root, text="Generate Random", variable=selected_option, value="Generate Random")
random_button.pack()

width_label = tk.Label(root, text="Width:")
width_label.pack()
width_entry = tk.Entry(root)
width_entry.pack()

height_label = tk.Label(root, text="Height:")
height_label.pack()
height_entry = tk.Entry(root)
height_entry.pack()

start_button = tk.Button(root, text="Start Game", command=start_game)
start_button.pack()

canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

root.mainloop()