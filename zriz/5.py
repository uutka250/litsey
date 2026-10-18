import tkinter as tk

root = tk.Tk()
root.title("Зміна тексту")
root.geometry("300x200")

label = tk.Label(root, text="Привіт, світ!")
label.pack(pady=40)

button = tk.Button(root, text="Змінити!", command=lambda: label.config(text="Текст змінено!"))
button.pack()

root.mainloop()