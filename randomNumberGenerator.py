import random
from tkinter import messagebox

lis = [1, 2, 3, 4, 5, 6]
sumR = sumB = 0
for i in range(100):
    x = random.randint(1, 6)
    if i % 2 == 0 and sumR < 100:
        sumR += x
        print("R", x)
        match x:
            case 1:
                messagebox.showinfo("R: ", str(f"Stand, {x}"))
            case 2:
                messagebox.showinfo("R: ", str(f"Lower leg, {x}"))
            case 3:
                messagebox.showinfo("R: ", str(f"Upper leg, {x}"))
            case 4:
                messagebox.showinfo("R: ", str(f"Stomach, {x}"))
            case 5:
                messagebox.showinfo("R: ", str(f"Chest, {x}"))
            case 6:
                messagebox.showinfo("R: ", str(f"Face, {x}"))

    elif i % 2 != 0 and sumB < 100:
        sumB += x
        print("B", x)
        match x:
            case 1:
                messagebox.showinfo("B: ", str(f"Stand, {x}"))
            case 2:
                messagebox.showinfo("B: ", str(f"Lower leg, {x}"))
            case 3:
                messagebox.showinfo("B: ", str(f"Upper leg, {x}"))
            case 4:
                messagebox.showinfo("B: ", str(f"Stomach, {x}"))
            case 5:
                messagebox.showinfo("B: ", str(f"Chest, {x}"))
            case 6:
                messagebox.showinfo("B: ", str(f"Face, {x}"))

    if sumR >= 100 or sumB >= 100:
        break


if sumR > sumB:
    print("R is winner")
else:
    print("B is winner")
