from tkinter import *
from PIL import ImageTk,Image
import random

# main window object
root = Tk()

# Title of GUI window
root.title("Rock Paper Scissors")

# Size of window
root.geometry('1500x1000')
# Creating canvas
canvas = Canvas(root,width=1500,height=1000)
canvas.grid(row=0, column=0)

# Creating labels on GUI window
l1 = Label(root, text='Player', font=('Algerian', 25))
l2 = Label(root, text='Computer', font=('Algerian', 25))
l3 = Label(root, text='Vs', font=('Algerian', 40))

# Placing all the labels on window
l1.place(x=500, y =60)
l2.place(x=930, y=60)
l3.place(x=750,y=260)

# Default image
img_p = Image.open(r"C:\Users\jamad\OneDrive\Pictures\Desktop\login system\default.jpeg.png")
img_p = img_p.resize((300, 300))

# Flipping image from left to right
img_c = img_p.transpose(Image.FLIP_LEFT_RIGHT)

# Loading images to put on canvas
img_p = ImageTk.PhotoImage(img_p)
img_c = ImageTk.PhotoImage(img_c)

# Rock image
rock_p = Image.open(r"C:\Users\jamad\OneDrive\Pictures\Desktop\login system\Rock.png")
rock_p = rock_p.resize((300, 300))

# Flipping image from left to right
rock_c = rock_p.transpose(Image.FLIP_LEFT_RIGHT)

# Loading images to put on canvas
rock_p = ImageTk.PhotoImage(rock_p)
rock_c = ImageTk.PhotoImage(rock_c)

# Paper image
paper_p = Image.open(r"C:\Users\jamad\OneDrive\Pictures\Desktop\login system\paper.jpeg")
paper_p = paper_p.resize((300, 300))

# Flipping image from left to right
paper_c = paper_p.transpose(Image.FLIP_LEFT_RIGHT)

# Loading images to put on canvas
paper_p = ImageTk.PhotoImage(paper_p)
paper_c = ImageTk.PhotoImage(paper_c)

# Scissor image
scissor_p = Image.open(r"C:\Users\jamad\OneDrive\Pictures\Desktop\login system\Scissors.png")
scissor_p = scissor_p.resize((300, 300))

# Flipping image from left to right
scissor_c = scissor_p.transpose(Image.FLIP_LEFT_RIGHT)

# Loading images to put on canvas
scissor_p = ImageTk.PhotoImage(scissor_p)
scissor_c = ImageTk.PhotoImage(scissor_c)

# Selection image
img_s = Image.open(r"C:\Users\jamad\OneDrive\Pictures\Desktop\login system\Selection.jpeg.png")
img_s = img_s.resize((300, 130))
img_s = ImageTk.PhotoImage(img_s)

# Putting image on canvas on specific coordinates
canvas.create_image(410, 150, anchor=NW, image=img_p)
canvas.create_image(870, 150, anchor=NW, image=img_c)



# game function
def game(player):
    select = [1, 2, 3]
    
    # Randomly selects option for computer
    computer = random.choice(select)

    # Setting image for player on canvas
    if player == 1:
        # Puts rock image on canvas
        canvas.create_image(410, 150, anchor=NW, image=rock_p)
    elif player == 2:
        # Puts paper image on canvas
        canvas.create_image(410, 150, anchor=NW, image=paper_p)
    else:
        # Puts scissor image on canvas
        canvas.create_image(410, 150, anchor=NW, image=scissor_p)

    # Setting image for computer on canvas
    if computer == 1:
        # Puts rock image on canvas
        canvas.create_image(870, 150, anchor=NW, image=rock_c)
    elif computer == 2:
        # Puts paper image on canvas
        canvas.create_image(870, 150, anchor=NW, image=paper_c)
    else:
        # Puts scissor image on canvas
        canvas.create_image(870, 150, anchor=NW, image=scissor_c)

    # Obtaining result by comparison
    if player == computer:  # Case of DRAW
        res = 'Draw'
    # Case of player's win
    elif (player == 1 and computer == 3) or (player == 2 and computer == 1) or (player == 3 and computer == 2):
        res = 'You won'
    # Case of computer's win0
    else:
        res = 'Computer won'

    # Putting result on canvas
    canvas.delete('result') #clear previous result
    canvas.create_text(810, 700, text='Result:- ' + res, fill="black", font=('Algerian', 25), tag='result')


# Function for clear button
def clear():
    # Removes result from canvas
    canvas.delete('result')

    # Puts default image on canvas
    canvas.create_image(410, 150, anchor=NW, image=img_p)
    canvas.create_image(870, 150, anchor=NW, image=img_c)


# Button for selecting rock
rock_b = Button(root, text='Rock', font=('Times', 12, 'bold'), command=lambda: game(1),  width=10, height= 3)

rock_b.place(x= 600, y=540)

# Button for select in paper
paper_b = Button(root, text='Paper', font=('Times', 12, 'bold'), command=lambda: game(2) , width=10, height= 3)
paper_b.place(x=750, y=540)

# Button for selecting scissor
scissor_b = Button(root, text='Scissor',  font=('Times', 12, 'bold') ,command=lambda: game(3) ,width=10, height= 3)
scissor_b.place(x=900,y =540)

# Button for clear
clear_b = Button(root, text='CLEAR', font=('Times', 10, 'bold'), width=10, command=clear).place(x=1350, y=40)

root.mainloop()
