from tkinter import *
from datetime import date
from dateutil import relativedelta
from tkcalendar import Calendar
import main_menu as main_menu
from PIL import ImageTk, Image # pillow library
import dbfile as db
from datetime import datetime, timedelta    

class MyCalendar(Calendar):
    def _on_click(self, event):
        print('LABEL:', event.widget)
        print('LABEL text :', event.widget['text'])
        print('LABEL style:', event.widget['style'])
        # var = event.widget['name']
        # print(var)
        
        # run original `_on_click`
        super()._on_click(event)
# TOOLTIPS CAN HELP
class show_calendar(Tk):
    
    def __init__(self, *args, **kwargs):
         super().__init__(*args, **kwargs)
         
         def date_bwn_two_dates(start_date, end_date):
            date_list = [] # The list where we want to store
            for i in range(int((end_date-start_date).days)+1): # Iterate between the range of dates
                year = (start_date+timedelta(i)).strftime("%Y") # Get the Year
                month = (start_date+timedelta(i)).strftime("%m") # Get the month
                date_a = (start_date+timedelta(i)).strftime("%d") # Get the day
                date_list.append(f'{year}-{month}-{date_a}') # Append the Objects accquired
            return date_list # return the list
        
         def headBack():
            self.destroy()
            print("Main-menu")
            
            root = main_menu.main_menu()
            root.state('zoomed')
            root.mainloop()
        
        # General Properties
         self.title('Task Scheduler')
         self.geometry('480x900')
         self.minsize(480,900)
         self.maxsize(480,900)
         self['background'] = 'black'
        
        # Wave
         self.frame_wave = Frame(self, width=200, height=400, bg='#FEF4E8')
         self.frame_wave.place(anchor='center', relx=0.5, rely=0.03)
         self.wave = ImageTk.PhotoImage(Image.open("assets/Header/calendar_header.png"))
         
         self.l1 = Label(self.frame_wave, image = self.wave, bg='black')
         self.l1.grid(row=1,column=1)
         
         # Back
         self.frame_back = Frame(self, width=400, height=400)
         self.frame_back.place(anchor='center', relx=0.07, rely=0.06)
         self.back = ImageTk.PhotoImage(Image.open("assets/Navigation/back_inv.png")) 

         self.head_back = Button(self.frame_back, image = self.back, bg='black', borderwidth=0, command=headBack)
         self.head_back.grid(row=1,column=1)
         
         
        # Calendar
         
         day_type = len(db.show_tasks('DAY')) # better to show a number for daily tasks
         week_type = [[i['title'],i['day']] for i in db.show_tasks('WEEK')]
         month_type = [[i['title'],i['day_range']] for i in db.show_tasks('MONTH')]
         
         self.DAY_COLOR = '#643CFF'
         self.WEEK_COLOR = '#FDB849'
         self.MONTH_COLOR = '#FF4672'
         
         self.cal = MyCalendar(self, background="black", selectmode='day', locale='en_US', cursor="hand1" ,font="Arial 14", mindate = date.today())
         
         # shows number of daily tasks
         self.cal.calevent_create(date.today(), f'{day_type} tasks for today', 'DAY')

         # shows all weekly tasks
         for j in week_type:

            start_date = datetime.strptime(j[1][0], '%Y-%m-%d').date()
            end_date = datetime.strptime(j[1][1], '%Y-%m-%d').date()
             
            for i in date_bwn_two_dates(start_date, end_date):
                date_object = datetime.strptime(i, '%Y-%m-%d').date()
                self.cal.calevent_create(date_object, j[0], 'WEEK')

         # shows all monthly tasks
         for j in month_type:

            start_date = datetime.strptime(j[1][0], '%Y-%m-%d').date()
            end_date = datetime.strptime(j[1][1], '%Y-%m-%d').date()
             
            for i in date_bwn_two_dates(start_date, end_date):
                date_object = datetime.strptime(i, '%Y-%m-%d').date()
                self.cal.calevent_create(date_object, j[0], 'MONTH')
                
         self.cal.tag_config('DAY', background=self.DAY_COLOR, foreground='black')     
         self.cal.tag_config('WEEK', background=self.WEEK_COLOR, foreground='black')
         self.cal.tag_config('MONTH', background=self.MONTH_COLOR, foreground='black')

         self.cal.pack(pady = 200,anchor = 'center',fill="both", expand=True)
  
# if __name__ == "__main__":
#     root = show_calendar()
#     root.state('zoomed')
#     root.mainloop()