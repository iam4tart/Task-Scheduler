from tkinter import *
from PIL import ImageTk, Image

import main_menu as main_menu

class intro_screen(Tk):
    def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      
      def getstarted_callback():
        self.destroy()
        print("Just-Got-Started")
        # if __name__ == "__main__":
        root = main_menu.main_menu()
        root.state('zoomed')
        root.mainloop()
        
      # General Properties
      self.title('Task Scheduler')
      self.geometry('480x900')
      self.minsize(480,900)
      self.maxsize(480,900)
      self['background'] = '#FEF4E8'

      # Title
      self.frame_title = Frame(self, width=200, height=400, bg='#FEF4E8')
      self.frame_title.place(anchor='n', relx=0.5, rely=0.1)
      self.title = ImageTk.PhotoImage(Image.open("assets/Intro/title.png"))

      # Subtitle
      self.frame_sub = Frame(self, width=200, height=400, bg='#FEF4E8')
      self.frame_sub.place(anchor='center', relx=0.5, rely=0.2)
      self.sub = ImageTk.PhotoImage(Image.open("assets\Intro\subtext.png"))
      
      # Avatar
      self.frame_avatar = Frame(self, width=200, height=400, bg='#FEF4E8')
      self.frame_avatar.place(anchor='center', relx=0.5, rely=0.5)
      self.avatar = ImageTk.PhotoImage(Image.open("assets\Intro\success_avatar.png"))

      # Get Started Button
      self.frame_getbutton = Frame(self, bg='#FEF4E8')
      self.frame_getbutton.place(anchor='center', relx=0.5, rely=0.83)
      self.getbutton = ImageTk.PhotoImage(Image.open("assets\Intro\get_started.png").resize((170,45)))

      # Base
      self.frame_base = Frame(self, width=200, height=400, bg='#FEF4E8')
      self.frame_base.place(anchor='center', relx=0.5, rely=0.9)
      self.base = ImageTk.PhotoImage(Image.open("assets\Intro\iphone_base.png"))
         
      # GRID Layout
      self.l1 = Label(self.frame_title, image = self.title, bg='#FEF4E8')
      self.l1.grid(row=1,column=1)

      self.l2 = Label(self.frame_sub, image = self.sub, bg='#FEF4E8')
      self.l2.grid(row=2,column=1) 

      self.l3 = Label(self.frame_avatar, image = self.avatar, bg='#FEF4E8')
      self.l3.grid(row=3,column=1) 

      self.l4 = Button(self.frame_getbutton, image = self.getbutton, bg='#FEF4E8', command = getstarted_callback, borderwidth=0)
      self.l4.grid(row=4,column=1) 

      self.l5 = Label(self.frame_base, image = self.base, bg='#FEF4E8')
      self.l5.grid(row=5,column=1) 

# if __name__ == "__main__":
#     root = intro_screen()
#     root.state('zoomed')
#     root.mainloop()
