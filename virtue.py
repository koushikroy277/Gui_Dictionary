from tkinter import *
from PIL import Image, ImageTk
import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def search(word):
    if word in data:
        t1.delete(1.0, END)
        t1.config(fg = "#fff")
        t1.insert(END, data[word])

    elif len(get_close_matches(word, data.keys())) > 0:
        t1.config(fg = "red")
        t1.delete(1.0, END)
        t1.insert(END, "Did you mean {} to mean : {}".format(get_close_matches(word, data.keys())[0], data[get_close_matches(word, data.keys())[0]]))
        output = get_close_matches(word, data.keys())

window = Tk()
window.title("Gui Dictionary")
# BACKGROUND
image = Image.open("WebDevelopment.png")
photo_image = ImageTk.PhotoImage(image)
label = Label(window, image = photo_image)
label.pack()

# INPUT
e1_value = StringVar()
e1 = Entry(window, textvariable = e1_value, bg = "#FFFD38", fg = "black", justify = CENTER, font = ("courier", 30, "bold"))
e1.place(relx = .185, rely = 0.70, relwidth = .63, relheight = .082)

# SEARCH BUTTON
b1 = Button(window, text = "SEARCH", command = lambda : search(e1_value.get()), relief = FLAT, bg = "grey", fg = "black", font = ("courier", 50, "bold"))
b1.place(relx = .40, rely = 0.85, relwidth = .2, relheight = .052)

# OUTPUT 
t1 = Text(window, fg = "#fff", relief = FLAT, bg = "#444444", font = ("courier", 30, "bold"))
t1.place(relx = .185, rely = 0.14, relwidth = .63, relheight = .20)


window.mainloop()