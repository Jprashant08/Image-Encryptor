from tkinter import *
from tkinter import filedialog
import webbrowser
root = Tk()
root.geometry("600x600")
root.columnconfigure(0, weight=2)  # sets the co-ordinates in center
root.config(bg='#BEBEBE')



def openweb():
    webbrowser.open(url, new=new)


def file_open():
    global file1
    file1 = filedialog.askopenfile(
        mode="r", filetype=[('jpg file', '*.jpg'), ('png file', '*.png'), ('jpeg file', '*.jpeg')])  # gets the file from device
    filename.delete('1.0', 'end')
    filename.insert(END, file1.name)


def click(event):
    entry1.config(state=NORMAL)
    entry1.delete(0, END)


def encrypt_image():
    if file1 is not None:

        file_name = file1.name
        print(file_name)
        # getting the unique key entered by user
        key = entry1.get()
        print(file_name, key)

        file = open(file_name, 'rb')
        image = file.read()
        file.close()

        image = bytearray(image)    # byte of image in array
        for index, values in enumerate(image):
            # interchanging the key with array using XOR operator
            image[index] = values ^ int(key)
        fle = open(file_name, 'wb')
        fle.write(image)
        fle.close()

        successfull.config(text="Image Have SuccessFully Encrypted 👌 ",
                           fg="Red", font=("verdana", 15, "bold"))
        successfull.place(x=90 , y=380)
        remember.config(text=("Remember the key for Decryption Is : "+key))
        remember.place(x=140 , y=450)


def decrypt_image():
    if file1 is not None:

        file_name = file1.name
        print(file_name)
        key = entry1.get()  # getting the unique key entered by user
        print(file_name, key)

        file = open(file_name, 'rb')
        image = file.read()
        file.close()

        image = bytearray(image)    # byte of image in array
        for index, values in enumerate(image):
            # interchanging the key with array using XOR operator
            image[index] = values ^ int(key)
        fle = open(file_name, 'wb')
        fle.write(image)
        fle.close()
        successfull.config(text="Successfully Decrypted the image ",
                           fg="green", font=("Verdana", 15, "bold"))
        successfull.place(x=90 , y=380)


# for encryption process

welcome_label = Label(root, text="🔥Image Encryption & Decryption System 🔥",
                      font=("panton rust", 18, "bold"), fg='#303030' , bg='#BEBEBE')
welcome_label.grid()


Btn1 = Button(root, text="Choose the image 🎞️", command=file_open, font=(
    "Verdana", 15, "bold"), fg="white", bg='#505050', border=8 , activeforeground="Orange",
activebackground="green")

Btn1.grid(pady=10 , padx=100)


support = Label(root, text='🙌'+"Supports only Jpg, jpeg,and png format" + '🙌',
                fg='red',  bg='#BEBEBE' , font=("Verdana", 12 , 'bold'))
support.place(x=100, y=100)

filename = Text(root, height=4, width=45)
filename.insert(END, "File Has Not Choosen!" + '💀💀💀💀💀')

filename.grid(pady=20)


entry1 = Entry(root,width=40)
entry1.insert(0, "Enter an integer key between 0 and 255")  # placeholder
entry1.config(state=NORMAL)
entry1.bind("<Button-1>", click)
entry1.grid(pady=20)
entry1.place(x=160 , y=220)

support1 = Label(root, text="✨Same Key should be used for encryption and decryption✨",
                 fg='red', bg='#BEBEBE' , font=("jost", 12 , 'bold'))
support1.place(x=80, y=240)

encrypt = Button(root, text="Encrypt", command=encrypt_image, font=(
    "jost", 15, "bold"), fg="white", bg='red')
encrypt.place(x=130, y=280)

decrypt = Button(root, text="Decrypt", command=decrypt_image, font=(
    "jost", 15, "bold"), fg="white", bg='#00ffc3')
decrypt.place(x=360, y=280)

successfull = Label(root, text=" " , fg="red",bg='#BEBEBE')
successfull.grid(pady=70)

remember = Label(root, text="", fg="red",bg='#BEBEBE',  font=("jost", 10))
remember.place(x=140, y=320)





root.mainloop()
