from tkinter import *
from tkinter import ttk
from hashlib import sha256
from time import time

def get_hash():
    global output
    global message_input
    global time_label

    message = message_input.get('1.0', END)
    start = time()
    result = sha256(message.encode('utf-8')).hexdigest()
    time_label.config(text=f'Time: {time() - start}')

    output.delete('1.0', END)
    output.insert(END, result)

# Window
root = Tk()
root.title('SHA')
root.geometry('500x300')
root.resizable(False, False)

label_font = ("Arial", 14)
input_font = ("Arial", 12)

# Styles
st = ttk.Style()
st.configure('TPSE.TButton', font=label_font)

# Message
message_label = ttk.Label(text='Message', font=label_font)
message_label.place(relx=0.43, rely=0.05)
message_input = Text(
    width=50, 
    height=3, 
    wrap='char', 
    font=input_font, 
    borderwidth=1, 
    relief='solid'
)
message_input.place(relx=0.045, rely=0.2)

ttk.Button(
    text='Get hash', 
    command=get_hash,
    style='TPSE.TButton'
).place(relx=0.38, rely=0.47)

# Hash
output = Text(
    width=50, 
    height=2, 
    wrap='char', 
    font=input_font, 
    borderwidth=1, 
    relief='solid'
)
output.place(relx=0.045, rely=0.65)

# Time
time_label = ttk.Label(text='Time: ', font=label_font)
time_label.place(relx=0.045, rely=0.84)

root.mainloop()