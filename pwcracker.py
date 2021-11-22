import tkinter as tk
#from tkinter import *
#root=tk.Tk()
#root.mainloop()
from views import NavBar, DisclaimerPage, HelpPage,MainPage
APP_HEIGHT=600
APP_WIDTH=1024
class Application(tk.Tk):
    def __init__(self):#constructor-instance of class
        super().__init__() #to inherit from multiple classes
        self.title("Password Cracker")
        main_frame=tk.Frame(self,height=APP_HEIGHT,width=APP_WIDTH)
        main_frame.pack_propagate(0)
        main_frame.pack(fill="both",expand=True) #expand frame to fit size
        self.resizable(0,0) #fix size to maximize and minimize GUI
        self.geometry(f"{APP_WIDTH}x{APP_HEIGHT}")

        #menu of the application
        menubar=NavBar(parent=self)
        self.config(menu=menubar)

        #frame for our application
        self.frames={}
        pages=(MainPage,)

        for page in pages:
            frame=page(parent=main_frame)
            self.frames[page]=frame
            frame.place(rely=0,relx=0)

        self.show_frame(MainPage)

    def show_frame(self,frame_name):
        frame=self.frames[frame_name]
        frame.tkraise()


    def OpenHelpPage(self):
        HelpPage()

    def OpenDisclaimerPage(self):
        DisclaimerPage()




if __name__ == '__main__':
    root=Application()
    root.mainloop()





