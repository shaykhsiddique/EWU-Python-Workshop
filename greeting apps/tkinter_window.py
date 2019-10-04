import tkinter
import random


window = tkinter.Tk() 
window.title("App Title")
window.geometry("450x350")
# window.configure(bg="sky blue")


def helloCallBack():
	msg = ["Hello", "Hi", "Nice to meet you, ", "Welcome", "Good morning", "Good evening, ", "It’s a pleasure to meet you, ", "Good day, "]
	output = tkinter.Text(window, width=40, height=5)
	output.grid(columnspan=5, row=6)
	output.insert(tkinter.END, msg[random.randint(0, 7)]+" "+str(E1.get())+".")




LH = tkinter.Label(window, text = "Greeting Apps", font=("Courier", 30, "bold"))
LH.grid(column=1, row=0)

window.grid_rowconfigure(1, minsize=20)

L1 = tkinter.Label(window, text = "Your name: ")
L1.grid(column=0, row=2)

E1 = tkinter.Entry(window, bd = 5, width=50)
E1.grid(column=1, row=2)

window.grid_rowconfigure(3, minsize=20)

B1 = tkinter.Button(window, text = "Click Me", command = helloCallBack)
B1.grid(column=1, row=4)

window.grid_rowconfigure(5, minsize=20)



window.mainloop() 