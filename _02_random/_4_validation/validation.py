import random
from tkinter import messagebox, Tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    for i in range(10):
        random_ = random.randint(1, 5)

        print(random_)

    # TODO 1) Use each value of random_number to give the user a random compliment
        if random_ == 5:
            messagebox.showinfo(title=("good"), message=("You are looking at a screen"))
    # TODO 2) Repeat all the code above 10 times
        if random_ == 2:
            messagebox.showinfo(title=("bad"), message=("You are still looking at the screen"))
        if random_ == 4:
            messagebox.showinfo(title=("good"), message=("You are still in a building"))
        if random_ == 3:
            messagebox.showinfo(title=("bad"), message=("You are in a room"))
        if random_ == 1:
            messagebox.showinfo(title=("good"), message=("You are in this building to teach or learn code"))
    # TODO 3) Find someone to test out your program. They will like it :)
