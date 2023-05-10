import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    number = random.randint(0, 3)
    # TODO Get the user to enter a question for the 8 ball to answer
    messagebox_ = simpledialog.askstring(title=(number), prompt=("type in a yes or no question"))
    # Make a variable and initialize it to a random number between 0 and 3


    if number == 0:
        messagebox.showinfo(title=("yes"), message=("yes"))
    elif number == 1:
        messagebox.showinfo(title=("no"), message=("no"))
    elif number == 2:
        messagebox.showinfo(title=("Google"), message=("Maybe you should ask google"))
    elif number == 3:
        messagebox.showinfo(title=("something"), message=("You choose yes or no"))
    # If the random number is 0

        # tell the user "Yes"

    # If the random number is 1

        # tell the user "No"

    # If the random number is 2

        # tell the user "Maybe you should ask Google?"

    # If the random number is 3

        # write your own answer
