import qrcode
import tkinter as tk
from tkinter import filedialog
mn=tk.Tk()
mn.title('QR Code Generator')
mn.geometry('500x300')
hl=tk.Label(mn,text="Data to encode :")
hl.place(x=20,y=20)
h=tk.Entry(mn)
h.place(x=150,y=20)
def generate():
    try:
        data = h.get()
        qr = qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=10,border=4,)
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        key = filedialog.asksaveasfilename(title="Save QR Code image as",defaultextension=".png",filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"),("BMP files", "*.bmp"),("GIF files", "*.gif"),("TIFF files", "*.tiff"), ("All files", "*.*")])
        if key:
            img.save(key)
        else:
            return
    except ValueError:
        return
b=tk.Button(mn,text="Proceed",command=lambda:generate(),cursor="hand2")
b.place(x=400,y=75)
mn.mainloop()
