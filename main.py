from tkinter import *
from pytube import YouTube

# creating the display window or the tkinter grid
# Tk() used to initialize tkinter to create display window
window = Tk()
# used to set the window’s width and height
window.geometry('500x500')
# set the fix size of window
window.resizable(0,0)
# used to give the title of window
window.title('Video Downloader App')

# Label() widget used to display text that users can’t able to modify.
Label(window,text = 'Youtube Video Downloader', font ='arial 20 bold').pack()

# Create field to enter link:
# declaring a variable called link and set it to stringvar which is a string type variable and we r gonna use that to store the youtube video link that the user enters.
link = StringVar()  

Label(window, text = 'Paste Link Here:', font = 'arial 15 bold').place(x= 160 , y = 60)

# Create an input field to enter the youtube link that you want to download
link_enter = Entry(window, width = 70,textvariable = link).place(x = 32, y = 90)

# Let's create a function to start the downloading process
def downloader():
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(window, text = "Video is downloaded and saved in project's folder !", font = 'arial 15').place(x= 20 , y = 210)

# Create a button widget to download and assign the download function to one of the attributes of the Button class which is called command, which simply means by clicking on that button I am giving it a command to trigger the downloader function
Button(window, text="Download", font='arial 15 bold', bg='yellow', padx=2, command=downloader).place(x=180, y=150)

window.mainloop()