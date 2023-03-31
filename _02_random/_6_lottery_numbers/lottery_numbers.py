import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':

    window = Tk()
    window.withdraw()

    # TODO 1) Get 6 random numbers to put on your lottery ticket
    numbers = random.randint(1, 99)
    Number = random.randint (1, 99)
    Numbers = random.randint (1, 99)
    Number4 = random.randint (1, 99)
    Number5 = random.randint (1, 99)
    Number6 = random.randint (1, 99)
    print(numbers)
    print(Number)
    print(Numbers)
    print(Number4)
    print(Number5)
    print(Number6)
    []
    # TODO 2) Display the selected numbers to the user in a pop-up
    messagebox.showinfo(title=("Lottery Ticket"), message=(numbers,Number,Numbers,Number4,Number5,Number6))

    # TODO 3) BONUS: Set the title of the pop-up to show it is a lottery ticket
