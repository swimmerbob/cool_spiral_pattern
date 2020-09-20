import tkinter
import random
from math import sqrt
#####
# Create root window
####

root = tkinter.Tk()
canvas = tkinter.Canvas(root, width=700, height=700, background='#FFFFFF')
canvas.grid(row=0, rowspan=2, column=1)
    #lines 12-24 adapted from https://stackoverflow.com/questions/4781184/tkinter-displaying-a-square-grid

rows = 300
columns = 300
cellwidth = 10
cellheight = 10
rect = {}
dot = {}
for column in range(70):
    for row in range(70):
        x1 = column*cellwidth
        y1 = row * cellheight
        x2 = x1 + cellwidth
        y2 = y1 + cellheight
        rect[row,column] = canvas.create_rectangle(x1,y1,x2,y2, fill="white")

base_square_row = []
base_square_col = []

        
for i in range(90):
    row = random.randint(1,68)
    col = random.randint(1,68)
    base_square_col.append(col)
    base_square_row.append(row)
    item_id = rect[row,col]
    canvas.itemconfig(item_id, fill="black")
# rgb to hex because tkinter shapes dont accept rgb 
# taken from https://www.codespeedy.com/convert-rgb-to-hex-color-code-in-python/ 
def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb



#make loop goes trough the lists of bsr and brc by one changing rgb values
p = 0
row = base_square_row[0]
col = base_square_col[0]
stepper = 1
def shader(row,col):
    r = 50
    g = 226
    b = 100
    stepper = 0
    for i in range(4):
        while stepper < 16:
            if stepper % 2 == 0:
                for i in range(stepper):
                    if row > 0 and row < 71: 
                        row = row -1
                        item_id = rect[row,col]
                        canvas.itemconfig(item_id, fill="#"+new_color)
                for i in range(stepper):
                    if col > 0 and col < 71:
                        col = col -1
                        item_id = rect[row,col]
                        canvas.itemconfig(item_id, fill="#"+new_color)
            else:
                for i in range(stepper):
                    if row > -1 and row < 69: 
                        row = row +1
                        item_id = rect[row,col]
                        canvas.itemconfig(item_id, fill="#"+new_color)
                for i in range(stepper):
                    if col > -1 and col < 69:
                        col = col +1
                        item_id = rect[row,col]
                        canvas.itemconfig(item_id, fill="#" + new_color)
            
            stepper = stepper + 1
            r = r + 6
            g = g - 7
            if b%2 == 0:
                b = b + 51
            else:
                b = b - 51
            
            color_fill = (r,g,b)
            new_color = rgb_to_hex(color_fill)

    
def main():
    
    i = 0                
    while i < 90:
        row = base_square_row[i]
        col = base_square_col[i]
        shader(row, col)
        i = i + 1
    root.mainloop()
    
main()
print(base_square_row)
print(base_square_col)

