import tkinter

boards = [
    [
        "--74916-5", 
        "2---6-3-9", 
        "-----7-1-",
        "-586----4", 
        "--3----9-", 
        "--62--187",
        "9-4-7---2", 
        "67-83----", 
        "81--45---"
    ]
]
solutions = [
    [
        "387491625", 
        "241568379", 
        "569327418",
        "758619234", 
        "123784596", 
        "496253187",
        "934176852", 
        "675832941", 
        "812945763"
    ]
]

board = boards[0]
solution = solutions[0]

window = tkinter.Tk()
window.title("Sudoku")


errors = 0
error_label = tkinter.Label(window, text = "Errors your making: 0", fg = "red")
error_label.pack()


numbers = {}
selected = None
digits = tkinter.Frame(window)
digits.pack()

def select_number(num):
    global selected
    selected = num
    for number, button in numbers.items():
        button.config(bg = "lightgray" if number == num else "white")

for i in range(1, 10):
    button = tkinter.Button(digits, text = str(i), width = 5, bg = "white",
                  command = lambda num = i: select_number(num))
    button.grid(row = 0, column = i-1)
    numbers[i] = button

#create the 9x9 sudoku board tiles to select
tiles = {}
grid = tkinter.Frame(window, bg = "black")
grid.pack(padx = 5, pady = 5)

def select_tile(row, col):
    global errors
    tile = tiles[(row, col)]
    if selected is None or tile["text"] != "":
        return
    
    if str(selected) == solution[row][col]:
        tile.config(text = str(selected), fg = "green")
    else:
        errors += 1
        error_label.config(text = "Errors: " + str(errors))

for r in range(9): #board
    for c in range(9):
        value = board[r][c]
        is_default_value = value != "-"

        tile = tkinter.Button(
            grid,
            text = value if is_default_value else "",
            width = 3,
            height = 1,
            font = ("Arial", 16),
            bg = "lightgray" if is_default_value else "white",
            state = "disabled" if is_default_value else "normal",
            command = lambda r = r, c = c: select_tile(r, c)
        )

 

        tile.grid(row = r, column = c,
                  padx = (2 if c % 4 == 0 else 0, 2 if c % 3 == 2 else 0),
                  pady = (2 if r % 3 == 0 else 0, 2 if r % 3 == 2 else 0))
        
        tiles[(r, c)] = tile

#center the window
window.update_idletasks()

width = window.winfo_width()
height = window.winfo_height()

x = (window.winfo_screenwidth() - width) // 2
y = (window.winfo_screenheight() - height) // 2

window.geometry(f"{width}x{height}+{x}+{y}")

window.mainloop()