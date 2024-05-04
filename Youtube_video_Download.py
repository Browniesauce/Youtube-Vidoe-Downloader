import tkinter
import customtkinter
from pytube import YouTube

#Downloading Video
def StartDownload():
    try:
        YTLink = Link.get()
        YTObject = YouTube(YTLink, on_progress_callback=On_Prog)
        Video = YTObject.streams.get_highest_resolution()
        Video.download()
        FinishLabel.configure(text="Download Completed" , text_color="white")
    except:
        FinishLabel.configure(text="Invalid Youtube URL", text_color="red") 

# Progress Percent Calculation and Updating Progress Bar   
def On_Prog(stream, chunk, bytes_remaining):
    Total_size = stream.filesize
    bytes_downloaded = Total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / Total_size * 100
    per = str(int(percentage_of_completion)) 
    ProgPercent.configure(text= per + "%")
    ProgPercent.update()
    ProgBar.set(float(percentage_of_completion)/100)

#Sys Settings 
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

#App Windows Settings
App = customtkinter.CTk()
App.geometry("800x600")
App.title("Youtube Downloader")

#adding UI Elements
Title = customtkinter.CTkLabel(App , text ="Insert your Youtube Link" )
Title.pack(padx=10 , pady=10)

#Link Input
Url = tkinter.StringVar()
Link = customtkinter.CTkEntry(App , width=400 , height=55,textvariable=Url)
Link.pack()

#Download Finished 
FinishLabel = customtkinter.CTkLabel(App,text="")
FinishLabel.pack(pady=10)

#Progress Percentage
ProgPercent = customtkinter.CTkLabel(App , text="0%")
ProgPercent.pack()

#ProgressBar
ProgBar = customtkinter.CTkProgressBar(App , width=500 , height=25 , corner_radius=8 , progress_color="purple")
ProgBar.set(0)
ProgBar.pack(padx=10 , pady=10)

#Download Button 
Download = customtkinter.CTkButton(App , text="Download" , height=50 , width = 200 , corner_radius=15 , command=StartDownload)
Download.pack(padx=10 , pady=30)

#Running App Conditon
App.mainloop()