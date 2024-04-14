import qrcode
from tkinter import *
from PIL import Image


def generate():
    qr = qrcode.make(url.get())
    qr.save("qrcode.png", "PNG")

    img = Image.open("qrcode.png")
    img.show()

    url.delete(0, END)


window = Tk()
window.title("QR Code Generator")
window.config(padx=20, pady=20)
window.resizable(width=FALSE, height=FALSE)

text = Label(window, text="Enter a URL:", font=('Arial', 12))
text.grid(column=0, row=0, pady=10)

url = Entry(window, width=35, font=('Arial', 10))
url.grid(column=1, row=0, columnspan=2, pady=10)

button = Button(window, text="Generate", font=('Arial', 12), width=26, command=generate)
button.grid(column=1, row=1, columnspan=2, pady=10)

window.mainloop()