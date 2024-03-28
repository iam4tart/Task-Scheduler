from tkinter import *
from PIL import ImageTk, Image
from tktimepicker import *
import dbfile as db
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import main_menu as main_menu

class progress_report(Tk):
    def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      
      def headBack():
            self.destroy()
            print("New-Plan")
            
            root = main_menu.main_menu()
            root.state('zoomed')
            root.mainloop()
      
      
      stats = db.show_progress()

      #General Properties
      self.title('Task Scheduler')
      size = [480,900]
      self.geometry(f'{size[0]}x{size[1]}')
      self.minsize(size[0],size[1])
      self.maxsize(size[0],size[1])
      self['background'] = '#FEF4E8'

      # Wave
      self.header = Frame(self, width=100, height=400, bg='#FEF4E8')
      self.header.place(anchor='center', relx=0.5, rely=0.07)
      self.wave = ImageTk.PhotoImage(Image.open("assets/Header/progress_header.png"))

      self.l1 = Label(self.header, image = self.wave, bg='#FEF4E8')
      self.l1.grid(row=1,column=1) 
      
      # Back
      self.frame_back = Frame(self, width=400, height=400, bg='#FEF4E8')
      self.frame_back.place(anchor='center', relx=0.08, rely=0.1)
      self.back = ImageTk.PhotoImage(Image.open("assets/Navigation/back.png"))
       
      self.head_back = Button(self.frame_back, image = self.back, bg='#FEF4E8', borderwidth=0, command=headBack)
      self.head_back.grid(row=1,column=1)
      
      
      # DAILY COMPLETION PIE CHART
      self.daily_fig = plt.figure(figsize=(3,3), dpi=100, facecolor='#FEF4E8')
      self.daily_fig.set_size_inches(2.5,2.5)

      self.daily_colors = ["#643CFF", "#E3DDF9"]
      if stats[0][3] == 1:
            plt.pie([1,0], colors = self.daily_colors)
            plt.axis('equal')
      else:
            plt.pie(stats[0][:2], colors = self.daily_colors)
            plt.axis('equal')

      self.daily_canvas = FigureCanvasTkAgg(self.daily_fig, master=self)
      self.daily_canvas.draw()
      self.daily_canvas.get_tk_widget().place(anchor='e', relx=0.5, rely=0.30)
      
      # DAILY LABELS
      self.daily_head = Label(self, text = "Daily", bg='#FEF4E8', font=("Reem Kufi Ink", 24, "bold"))
      self.daily_head.place(anchor='center', relx=0.60, rely=0.25)
      
      try:
            self.daily_rate = Label(self, text = f"{round((stats[0][0]/(stats[0][2]))*100)}% Completion", bg='#FEF4E8', font=("Reem Kufi Ink", 20))
            self.daily_rate.place(anchor='w', relx=0.52, rely=0.30)
      except ZeroDivisionError:
            self.daily_rate = Label(self, text = f"0% Completion", bg='#FEF4E8', font=("Reem Kufi Ink", 20))
            self.daily_rate.place(anchor='w', relx=0.52, rely=0.30)

      # WEEKLY COMPLETION PIE CHART
      self.weekly_fig = plt.figure(figsize=(3,3), dpi=100, facecolor='#FEF4E8')
      self.weekly_fig.set_size_inches(2.5,2.5)

      self.weekly_colors = ["#FDB849", "#FFE8C4"]
      if stats[1][3] == 1:
            plt.pie([1,0], colors = self.weekly_colors)
            plt.axis('equal')
      else:
            plt.pie(stats[1][:2], colors = self.weekly_colors)
            plt.axis('equal')

      self.weekly_canvas = FigureCanvasTkAgg(self.weekly_fig, master=self)
      self.weekly_canvas.draw()
      self.weekly_canvas.get_tk_widget().place(anchor='e', relx=0.5, rely=0.55)
      
      # WEEKLY LABELS
      self.weekly_head = Label(self, text = "Weekly", bg='#FEF4E8', font=("Reem Kufi Ink", 24, "bold"))
      self.weekly_head.place(anchor='center', relx=0.60, rely=0.50)
      
      try:
            self.weekly_rate = Label(self, text = f"{round((stats[1][0]/(stats[1][2]))*100)}% Completion", bg='#FEF4E8', font=("Reem Kufi Ink", 20))
            self.weekly_rate.place(anchor='w', relx=0.52, rely=0.55)
      except ZeroDivisionError:
            self.weekly_rate = Label(self, text = f"0% Completion", bg='#FEF4E8', font=("Reem Kufi Ink", 20))
            self.weekly_rate.place(anchor='w', relx=0.52, rely=0.55)

      # MONTHLY COMPLETION PIE CHART
      self.monthly_fig = plt.figure(figsize=(3,3), dpi=100, facecolor='#FEF4E8')
      self.monthly_fig.set_size_inches(2.5,2.5)

      self.monthly_colors = ["#FF4672", "#FFD9E2"]
      if stats[2][3] == 1:
            plt.pie([1,0], colors = self.monthly_colors)
            plt.axis('equal')
      else:
            plt.pie(stats[2][:2], colors = self.monthly_colors)
            plt.axis('equal')

      self.monthly_canvas = FigureCanvasTkAgg(self.monthly_fig, master=self)
      self.monthly_canvas.draw()
      self.monthly_canvas.get_tk_widget().place(anchor='e', relx=0.5, rely=0.80)
      
      # monthly LABELS
      self.monthly_head = Label(self, text = "Monthly", bg='#FEF4E8', font=("Reem Kufi Ink", 24, "bold"))
      self.monthly_head.place(anchor='center', relx=0.60, rely=0.75)
      
      try:
            self.monthly_rate = Label(self, text = f"{round((stats[2][0]/(stats[2][2]))*100)}% Completion", bg='#FEF4E8', font=("Reem Kufi Ink", 20))
            self.monthly_rate.place(anchor='w', relx=0.52, rely=0.80)
      except ZeroDivisionError:
            self.monthly_rate = Label(self, text = f"0% Completion", bg='#FEF4E8', font=("Reem Kufi Ink", 20))
            self.monthly_rate.place(anchor='w', relx=0.52, rely=0.80)

# if __name__ == "__main__":
#     root = progress_report()
#     root.mainloop()