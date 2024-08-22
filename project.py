import tkinter as tk
import random
import string
def generate_password():
    length = int(lenght_entry.get())
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''
    for i in range(length):
        password += random.choice(characters)
    password_label.config(text=password)
window = tk.Tk()
window.title('Password Generator')
length_label = tk.Label(window, text='Password length:')
length_label.pack()
lenght_entry = tk.Entry(window)
lenght_entry.pack()
generate_button = tk.Button(window, text='Generate', command=generate_password)
generate_button.pack()
password_label = tk.Label(window, text='')
password_label.pack()
window.mainloop()

