from tkinter import *


def download_pdf():
    url_name = url.get()
    Label(master, text=f'Searching {url_name}').pack()


master = Tk()
master.title("Download PDF from URL")
master.geometry('400x300')

Label(master, text='URL')
url = Entry(master)
url.pack(pady=30)

Button(
        master,
        text = "Download PDF",
        padx = 10,
        pady = 5,
        command = download_pdf).pack()


master.mainloop()
