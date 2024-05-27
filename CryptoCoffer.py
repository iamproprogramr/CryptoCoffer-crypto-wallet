from tkinter import *
from bitcoin import *
from PIL import Image, ImageTk


screen = Tk()
screen.title("CryptoCoffer by Muhammad Yousaf")
screen.geometry('700x500')
screen.resizable(False, False)


screen.iconbitmap(r'bitcoin.ico')


background_image = Image.open(r'backgournd.png')
background_photo = ImageTk.PhotoImage(background_image)
background_label = Label(screen, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


private_key = random_key()
public_key = privtopub(private_key)
wallet_address = pubtoaddr(public_key)

def generateaddress():
    addressentry.delete(0, END)
    addressentry.insert(END, wallet_address)


Wl = Label(screen, text="Wallet", font=("bold", 24), border=0, bg='white')
Wl.place(x=50, y=50)

Balance = Label(screen, text="Balance:", font=('bold', 14), border=0, bg='white')
Balance.place(x=50, y=100)

Btcbalance = Label(screen, text="0.000000Btc", font=('bold', 12), border=0, bg='white')
Btcbalance.place(x=125, y=103)

recentwithdraw = Label(screen, text="Withdraw:", font=('bold', 14), border=0, bg='white')
recentwithdraw.place(x=50, y=130)

withdrawtext = Label(screen, text="0.00000000Btc", font=('bold', 12), border=0, bg='white')
withdrawtext.place(x=137, y=133)

send = Label(screen, text="Send:", font=("bold", 14), border=0, bg='white')
send.place(x=50, y=160)

sendtext = Label(screen, text="0.00000000Btc", font=('bold', 12), border=0, bg='white')
sendtext.place(x=110, y=163)

revicced = Label(screen, text="Received:", font=('bold', 14), border=0, bg='white')
revicced.place(x=50, y=190)

reviccedtext = Label(screen, text="0.00000000Btc", font=('bold', 12), border=0, bg='white')
reviccedtext.place(x=137, y=193)


recent_Label = Label(screen, text="Recent Transaction", font=("bold", 24), border=0, bg='white')
recent_Label.place(x=400, y=50)

Norevviced = Label(screen, text="No Any Recent\nTransaction", font=('bold', 28), border=0, foreground="#999999", bg='white')
Norevviced.place(x=430, y=130)


Generate = Button(screen, text="Generate Address", width=20, height=1, relief='groove', command=generateaddress)
Generate.place(x=260, y=250)

addressentry = Entry(screen, width=50, border=0, font=('bold', 18))
addressentry.place(x=30, y=280)


SendBitcoin = Button(screen, text="Send Bitcoin", width=20, height=1, relief='groove')
SendBitcoin.place(x=260, y=320)

reviccedsentry = Entry(screen, width=50, border=0, font=('bold', 18))
reviccedsentry.place(x=30, y=360)

screen.mainloop()

