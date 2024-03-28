from tkinter import *
from PIL import ImageTk, Image
import data_caller as dc
import main_menu as main_menu
import show_notes as show_notes
import progress_report as progress_report
import day_menu as day_menu
import week_menu as week_menu
import month_menu as month_menu
import show_calendar as show_calendar

class main_menu(Tk):
    def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      
      def show_daily_menu():
         self.destroy()
         print("Day-Menu")
         
         root = day_menu.day_menu()
         root.state('zoomed')
         root.mainloop()
         
      def show_weekly_menu():
         self.destroy()
         print("Week-Menu")
         
         root = week_menu.week_menu()
         root.state('zoomed')
         root.mainloop()
         
      def show_monthly_menu():
         self.destroy()
         print("Month-Menu")
         
         root = month_menu.month_menu()
         root.state('zoomed')
         root.mainloop()
      
      def showNotes():
         self.destroy()
         print("Show-Notes")
         
         root = show_notes.show_notes()
         root.state('zoomed')
         root.mainloop()
         
      def showCalendar():
         self.destroy()
         print("Show-Calendar")
         
         root = show_calendar.show_calendar()
         root.state('zoomed')
         root.mainloop()
         
      def show_progress():
         self.destroy()
         print("Show-Current-Progress")
         
         root = progress_report.progress_report()
         root.state('zoomed')
         root.mainloop()
         
      # General Properties
      self.title('Task Scheduler')
      self.geometry('480x900')
      self.minsize(480,900)
      self.maxsize(480,900)
      self['background'] = '#FEF4E8'
      
      # Wave
      self.frame_wave = Frame(self, width=400, height=400, bg='#FEF4E8')
      self.frame_wave.place(anchor='center', relx=0.5, rely=0.05)
      self.wave = ImageTk.PhotoImage(Image.open("assets/MainMenu/wave.png"))

      # Text "Schedules for the"
      self.frame_text = Frame(self, width=200, height=400, bg='#FEF4E8')
      self.frame_text.place(anchor='e', relx=0.56, rely=0.24)

      # Schedule Menu
      self.frame_day = Frame(self, width=200, height=400, bg='#FEF4E8')
      self.frame_day.place(anchor='e', relx=0.33, rely=0.4)
      self.day_menu = ImageTk.PhotoImage(Image.open("assets/MainMenu/day_menu.png"))

      self.frame_week = Frame(self, width=200, height=400, bg='#FEF4E8')
      self.frame_week.place(anchor='center', relx=0.5, rely=0.4)
      self.week_menu = ImageTk.PhotoImage(Image.open("assets/MainMenu/week_menu.png"))

      self.frame_month = Frame(self, width=200, height=400, bg='#FEF4E8')
      self.frame_month.place(anchor='w', relx=0.67, rely=0.4)
      self.month_menu = ImageTk.PhotoImage(Image.open("assets/MainMenu/month_menu.png"))
      
      # Subtitle
      self.frame_nametitle = Frame(self, width=200, height=400, bg='#FEF4E8')
      self.frame_nametitle.place(anchor='e', relx=0.97, rely=0.033)


      # Subtitle
      self.frame_sub = Frame(self, width=200, height=400, bg='#FEF4E8')
      self.frame_sub.place(anchor='e', relx=0.97, rely=0.075)
      self.sub = ImageTk.PhotoImage(Image.open("assets/MainMenu/subtitle.png"))

      # Base
      self.frame_base = Frame(self, width=200, height=400, bg='#FEF4E8')
      self.frame_base.place(anchor='center', relx=0.5, rely=0.58)
      self.base = ImageTk.PhotoImage(Image.open("assets\Intro\iphone_base.png"))

      # Add Notes
      self.frame_notes = Frame(self, width=200, height=400, bg='#FEF4E8')
      self.frame_notes.place(anchor='center', relx=0.5, rely=0.65)
      self.notes = ImageTk.PhotoImage(Image.open("assets/MainMenu/add_notes.png"))

      # Show Calendar
      self.frame_calendar = Frame(self, width=200, height=400, bg='#FEF4E8')
      self.frame_calendar.place(anchor='center', relx=0.5, rely=0.75)
      self.calendar = ImageTk.PhotoImage(Image.open("assets/MainMenu/show_calendar.png"))

      # Show Current Progress Report
      self.frame_progress = Frame(self, width=200, height=400, bg='#FEF4E8')
      self.frame_progress.place(anchor='center', relx=0.5, rely=0.85)
      self.progress = ImageTk.PhotoImage(Image.open("assets/MainMenu/progress_report.png"))
         
      # GRID Layout

      self.l1 = Label(self.frame_wave, image = self.wave, bg='#FEF4E8')
      self.l1.grid(row=1,column=1)
      
      self.l2 = Label(self.frame_nametitle, text=f"Hello, {dc.get_name()}",fg="#815FFB", bg='#FEF4E8', font=("Reem Kufi Ink", 22, "bold"))
      self.l2.grid(row=2,column=1) 

      self.l2 = Label(self.frame_sub, image = self.sub, bg='#FEF4E8')
      self.l2.grid(row=2,column=1) 

      self.l3 = Label(self.frame_text, text = "Schedules for the", fg="gray20", bg='#FEF4E8', font=("Reem Kufi Ink", 22, "bold"))
      self.l3.grid(row=3,column=1) 

      self.l6_1 = Button(self.frame_day, image = self.day_menu, bg='#FEF4E8', command = show_daily_menu, borderwidth=0)
      self.l6_1.grid(row=4,column=1) 

      self.l6_2 = Button(self.frame_week, image = self.week_menu, bg='#FEF4E8', command = show_weekly_menu, borderwidth=0)
      self.l6_2.grid(row=4,column=1)

      self.l6_3 = Button(self.frame_month, image = self.month_menu, bg='#FEF4E8', command = show_monthly_menu, borderwidth=0)
      self.l6_3.grid(row=4,column=1) 

      self.l5 = Label(self.frame_base, image = self.base, bg='#FEF4E8')
      self.l5.grid(row=5,column=1) 

      self.l6 = Button(self.frame_notes, image =self. notes, bg='#FEF4E8', command = showNotes, borderwidth=0)
      self.l6.grid(row=6,column=1) 

      self.l7 = Button(self.frame_calendar, image = self.calendar, bg='#FEF4E8', command = showCalendar, borderwidth=0)
      self.l7.grid(row=7,column=1) 

      self.l8 = Button(self.frame_progress, image = self.progress, bg='#FEF4E8', command = show_progress, borderwidth=0)
      self.l8.grid(row=8,column=1) 