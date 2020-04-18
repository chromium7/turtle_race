from tkinter import *
import random
import turtle
import time

root = Tk()
root.title("Race")
root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")

class character(turtle.RawTurtle):
    def __init__(self, shape, xcor, ycor, color):
        super().__init__(turtle_screen, visible=False)
        self.shape(shape)
        self.color(color)
        self.pensize(1)
        self.speed(0)
        self.penup()
        self.setx(xcor)
        self.sety(ycor)
        self.showturtle()
        self.pendown()

    def move(self):
        self.forward(random.randint(5,18))

def generate_turtle():
    global players
    global scoreboard
    turtle_number = number_selection.get()
    counter=0
    players = []
    for x in range(turtle_number):
        x_shape = shape_list[counter]
        x_color = color_list[counter]
        x_xcor = -450
        x_ycor = (50*turtle_number/3) - counter*(300/turtle_number)
        x = character(x_shape,x_xcor,x_ycor,x_color)
        players.append(x)
        counter +=1


def create_score():
    global scoreboard
    scoreboard = [0] * number_selection.get()
    counter = 0
    for i in range(number_selection.get()):
        char_lbl = Label(score_lbl_frame, text=name_list[i], bg="#9fcff4")
        char_lbl.grid(row=counter, column=0, padx=40, pady=1, sticky=W)
        counter += 1

def race():
    x = 0
    while x <= 400:
        for player in players:
            player.move()
            if player.xcor() >= x:
                x = player.xcor()
    res = [player.xcor() for player in players]
    winner = res.index(max(res))
    scoreboard[winner] += 1
    counter = 0
    print(scoreboard)
    for _ in players:
        score_lbl = Label(score_lbl_frame, text=scoreboard[counter], fg="red", bg="#9fcff4")
        score_lbl.grid(row=counter, column=1)
        counter += 1
    time.sleep(2)
    turtle_screen.clear()
    setup()
    generate_turtle()

def clear():
    turtle_screen.clear()
    setup()
    for widget in score_lbl_frame.winfo_children():
        widget.destroy()

def setup():
    turtle_screen.bgcolor("#49d444")
    t = turtle.RawTurtle(turtle_screen, visible=False)
    t.penup()
    t.speed(0)
    t.goto(-390, 230)
    t.pendown()
    t.color("navy")
    t.write("LETS GOOOOOOOOO pEpEG", font=("Helvetica", 38, "bold italic"))
    tt = turtle.RawTurtle(turtle_screen, visible=False)
    tt.penup()
    tt.speed(0)
    tt.goto(-500, -257)
    tt.fillcolor("brown")
    tt.begin_fill()
    tt.forward(1000)
    tt.right(90)
    tt.forward(100)
    tt.right(90)
    tt.forward(1000)
    tt.right(90)
    tt.forward(100)
    tt.end_fill()
    ttt = turtle.RawTurtle(turtle_screen, visible=False)
    ttt.penup()
    ttt.speed(0)
    ttt.goto(400, 180)
    ttt.pensize(5)
    ttt.color("brown")
    ttt.pendown()
    ttt.right(90)
    ttt.forward(400)

title_frame = Frame(root, bg="#222f94", borderwidth=0, highlightthickness=0)
title_frame.grid(row=0, column=0, columnspan=2, sticky=EW, ipady=10)
title_lbl = Label(title_frame, text="OMEGA Pepeg Race", font= "Helvetica 34 bold", bg="#222f94", fg="white")
title_lbl.pack(anchor=W)

text_frame = Frame(root, borderwidth=3, bg= "#2B97EB", relief=SUNKEN,highlightbackground="black")
text_frame.grid(row=1, column=1, sticky=NS)

select_text = Label(text_frame, text="Select player number:", font="Helvetica 18", fg="black",bg= "#2B97EB", width=25)
select_text.grid(row=0, column=0, pady= 10)

number_selection = Scale(text_frame, from_= 2, to=7, bg= "#2B97EB", orient=HORIZONTAL, borderwidth=0, highlightthickness=0)
number_selection.grid(row=1, column=0, pady=10)

generate_char = Button(text_frame, text="Generate Players", command=generate_turtle)
generate_char.grid(row=2, column =0, pady=5)

show_score = Button(text_frame, text="Set up scoreboard", command=create_score)
show_score.grid(row=3,column=0,pady=5)

start_btn = Button(text_frame, text="Start Race", command=race)
start_btn.grid(row=4, column=0, pady=5)

score_lbl_frame = LabelFrame(text_frame, text="Scoreboard", font="Helvetica 12 italic", bg= "#9fcff4", width= 250, height= 350, borderwidth= 8)
score_lbl_frame.grid_propagate(0)
score_lbl_frame.grid(row=5,column=0, pady=5)

clear_btn = Button(text_frame, text="Clear Board", command= clear)
clear_btn.grid(row=6,column=0)

turtle_canvas = Canvas(root, width= 1000, height=655, highlightbackground="black", relief=SUNKEN)
turtle_canvas.grid(row=1, column=0)

turtle_screen = turtle.TurtleScreen(turtle_canvas)
setup()
turtle_screen.register_shape("trihardrun.gif")
turtle_screen.register_shape("schubertrun.gif")
turtle_screen.register_shape("peperun.gif")
turtle_screen.register_shape("peperun2.gif")
turtle_screen.register_shape("jogchamp.gif")
turtle_screen.register_shape("fatrun.gif")
turtle_screen.register_shape("fatcycle.gif")

shape_list = ["trihardrun.gif","jogchamp.gif","peperun.gif","fatrun.gif","schubertrun.gif","peperun2.gif","fatcycle.gif"]
name_list = ["TriHard", "JogChamp", "Peepo", "FatHead", "Clown", "Weird Pepe", "FatHead on Bicycle"]
color_list = ["brown", "yellow", "green", "white", "pink", "blue", "black"]

root.mainloop()
