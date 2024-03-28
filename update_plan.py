from tkinter import *
from PIL import ImageTk, Image
from tktimepicker import *
import dbfile as db
import data_caller as dc
import main_menu as main_menu
from datetime import date
from dateutil import relativedelta
from tkcalendar import Calendar
import day_menu as day_menu
import week_menu as week_menu
import month_menu as month_menu
#----------
# select the task to update using dropdown - get its title and id
# fetch whats already the task
# display it
# use the new_plan functions to edit from the orignal state to new state
# update the record with the new state
#----------

class update_plan(Tk):
      def __init__(self, *args, **kwargs):
         super().__init__(*args, **kwargs)
         
         self.current_id = {}
         
         def headBack():
            self.destroy()
            print("Main-menu")
            
            root = main_menu.main_menu()
            root.state('zoomed')
            root.mainloop()
         
         def combo_defocus(event):
             event.widget.master.focus_set()
         
         def getter(*arg):
            current_index = self.name_entry.current()
            #self.current_data = dc.data_listing('WEEK')[current_index]
            self.current_data = db.get_everything()[current_index]
            self.current_id = self.current_data
            
            print(self.current_data['maintype'])
            if self.current_data['maintype'] == "DAY":
               self.menu.set(self.options[0])
               type_getter()
            elif self.current_data['maintype'] == "WEEK":
               self.menu.set(self.options[1])
               type_getter()
            elif self.current_data['maintype'] == "MONTH":
               self.menu.set(self.options[2])
               type_getter()
            else:
               pass
            
            # self.from_time.configure(text=self.current_data[2][0])
            # self.to_time.configure(text=self.current_data[2][1])
            
         def type_getter(*arg):
            current_type = self.type_entry.current()
            #print(current_type)
            if current_type == 0:
               self.task_time = ImageTk.PhotoImage(Image.open("assets/NewPlan/time_duration.png"))
               self.l4 = Label(self.frame_time, image = self.task_time, bg='#FEF4E8')
               self.l4.grid(row=4,column=1) 
               
               self.from_time = Button(self.frame_time, text="Pick a time of the day!", command= lambda t= "from": updateTime(t), font=("Times New Roman", 18), borderwidth=0, bg='white')
               self.from_time.place(anchor='center', relx=0.5, rely=0.49)

               self.to_time = Button(self.frame_time, text="Pick a time of the day!", command= lambda t= "to": updateTime(t), font=("Times New Roman", 18), borderwidth=0, bg='white')
               self.to_time.place(anchor='center', relx=0.5, rely=0.85)

            elif current_type == 1:
               self.task_time = ImageTk.PhotoImage(Image.open("assets/NewPlan/day_duration.png"))
               self.l4 = Label(self.frame_time, image = self.task_time, bg='#FEF4E8')
               self.l4.grid(row=4,column=1)
               
               self.from_day = Button(self.frame_time, text="Pick a day of the week!", command= lambda t= "from": updateDayWeek(t), font=("Times New Roman", 18), borderwidth=0, bg='white')
               self.from_day.place(anchor='center', relx=0.5, rely=0.49)

               self.to_day = Button(self.frame_time, text="Pick a day of the week!", command= lambda t= "to": updateDayWeek(t), font=("Times New Roman", 18), borderwidth=0, bg='white')
               self.to_day.place(anchor='center', relx=0.5, rely=0.85)

               
               
            elif current_type == 2:
               self.task_time = ImageTk.PhotoImage(Image.open("assets/NewPlan/week_duration.png"))
               self.l4 = Label(self.frame_time, image = self.task_time, bg='#FEF4E8')
               self.l4.grid(row=4,column=1)
               
               self.from_date = Button(self.frame_time, text="Pick a date of the month!", command= lambda t= "from": updateDateMonth(t), font=("Times New Roman", 18), borderwidth=0, bg='white')
               self.from_date.place(anchor='center', relx=0.5, rely=0.49)

               self.to_date = Button(self.frame_time, text="Pick a date of the month!", command= lambda t= "to": updateDateMonth(t), font=("Times New Roman", 18), borderwidth=0, bg='white')
               self.to_date.place(anchor='center', relx=0.5, rely=0.85)
            else:
               pass
         
         def submit_data():
            
            task_type = self.menu.get()
            
            if task_type == "Daily":
               task_type = "DAY"
               time_from = self.from_time.cget('text')
               time_to = self.to_time.cget('text')
               
               print(f"{task_type} TYPE TASK -- FROM {time_from} TO {time_to}")
               db.update_task(self.current_id['title'], task_type, [time_from, time_to], ["NaN", "NaN"], ["NaN", "NaN"], self.current_id['refID'])

               self.destroy()
               print("Back to Day Menu")
                  
               root = day_menu.day_menu()
               root.state('zoomed')
               root.mainloop()
               
            elif task_type == "Weekly":
               task_type = "WEEK"
               day_from = self.from_day.cget('text')
               day_to = self.to_day.cget('text')
               
               print(f"{task_type} TYPE TASK -- FROM {day_from} TO {day_to}")
               db.update_task(self.current_id['title'], task_type, ["NaN", "NaN"], [day_from, day_to], ["NaN", "NaN"], self.current_id['refID'])

               self.destroy()
               print("Back to Day Menu")
                  
               root = week_menu.week_menu()
               root.state('zoomed')
               root.mainloop()
               
            elif task_type == "Monthly":
               task_type = "MONTH"
               date_from = self.from_date.cget('text')
               date_to = self.to_date.cget('text')
               
               print(f"{task_type} TYPE TASK -- FROM {date_from} TO {date_to}")
               db.update_task(self.current_id['title'], task_type, ["NaN", "NaN"], ["NaN", "NaN"], [date_from, date_to], self.current_id['refID'])

               self.destroy()
               print("Back to Day Menu")
                  
               root = month_menu.month_menu()
               root.state('zoomed')
               root.mainloop()
            else:
               pass
            
            

         def updateDayWeek(fname):
            
               def print_sel():
                  day_fetch=cal.selection_get()
                  
                  if fname == "from":
                     self.from_day.configure(text=day_fetch)
                  elif fname == "to":
                     self.to_day.configure(text=day_fetch)
                  else:
                     pass
                  
                  print(day_fetch)
                  top.destroy()

               top = Toplevel(self)
               top.resizable(False,False)
               nextweek = date.today() + relativedelta.relativedelta(weeks=1)
               cal = Calendar(top, background="#815FFB", selectmode='day', locale='en_US', cursor="hand1" ,font="Arial 14", mindate=date.today(), maxdate=nextweek)
               cal.pack(fill="both", expand=True)
               ttk.Button(top, text="ok", command=print_sel).pack()
            
         def updateDateMonth(fname):
            
               def print_sel():
                  day_fetch=cal.selection_get()
                  
                  if fname == "from":
                     self.from_date.configure(text=day_fetch)
                  elif fname == "to":
                     self.to_date.configure(text=day_fetch)
                  else:
                     pass
                  
                  print(day_fetch)
                  top.destroy()

               top = Toplevel(self)
               top.resizable(False,False)
               nextmonth = date.today() + relativedelta.relativedelta(months=1)
               cal = Calendar(top, background="#14D29B",selectmode='day', locale='en_US', cursor="hand1" ,font="Arial 14", mindate=date.today(), maxdate=nextmonth)
               cal.pack(fill="both", expand=True)
               ttk.Button(top, text="ok", command=print_sel).pack()
            
         def updateTime(fname):
            
               # time_fetch = ""
               
               def time_data(time):
                  time_fetch="{}:{} {}".format(*time)
                  
                  if fname == "from":
                     self.from_time.configure(text=time_fetch)
                  elif fname == "to":
                     self.to_time.configure(text=time_fetch)
                  else:
                     pass
                  
                  print(time_fetch)
                  newWindow.destroy()
                  
               newWindow = Toplevel(self)
         
               newWindow.title("Time Picker")
               newWindow.resizable(False,False)
               newWindow.geometry("360x400")
               newWindow["bg"] ="white"
               ptime_picker = AnalogPicker(newWindow)
               ptime_picker.grid(row=1, column=1)
               theme = AnalogThemes(ptime_picker)
               theme.setDracula()
               
               setter = Button(newWindow, text="Pick", width=23, height=2, font=("Times New Roman", 18), borderwidth=0, bg='white', command = lambda: time_data(ptime_picker.time()))
               setter.grid(row=2, column=1)
         
         # General Properties
         self.title('Task Scheduler')
         self.geometry('480x900')
         self.minsize(480,900)
         self.maxsize(480,900)
         self['background'] = '#FEF4E8'
 
         # Wave
         self.frame_wave = Frame(self, width=200, height=400, bg='#FEF4E8')
         self.frame_wave.place(anchor='center', relx=0.52, rely=0.03)
         self.wave = ImageTk.PhotoImage(Image.open("assets/NewPlan/update_plan_header.png"))
         
         # Back
         self.frame_back = Frame(self, width=400, height=400, bg='#FEF4E8')
         self.frame_back.place(anchor='center', relx=0.07, rely=0.06)
         self.back = ImageTk.PhotoImage(Image.open("assets/Navigation/back.png")) 

         # task name
         self.frame_sub = Frame(self, width=200, height=400, bg='#FEF4E8')
         self.frame_sub.place(anchor='center', relx=0.5, rely=0.20)
         self.sub = ImageTk.PhotoImage(Image.open("assets/NewPlan/task_name.png"))

         self.frame_type = Frame(self, width=200, height=400, bg='#FEF4E8')
         self.frame_type.place(anchor='center', relx=0.5, rely=0.38)
         self.task_type = ImageTk.PhotoImage(Image.open("assets/NewPlan/task_type.png"))

         self.frame_time = Frame(self, width=200, height=400, bg='#FEF4E8')
         self.frame_time.place(anchor='center', relx=0.5, rely=0.65)
         self.task_time = ImageTk.PhotoImage(Image.open("assets/NewPlan/time_duration.png"))

         self.frame_done = Frame(self, width=200, height=400, bg='#FEF4E8')
         self.frame_done.place(anchor='center', relx=0.5, rely=0.88)
         self.task_done = ImageTk.PhotoImage(Image.open("assets/NewPlan/done.png"))

         self.l1 = Label(self.frame_wave, image = self.wave, bg='#FEF4E8')
         self.l1.grid(row=1,column=1)

         self.l2 = Label(self.frame_sub, image = self.sub, bg='#FEF4E8')
         self.l2.grid(row=2,column=1) 

         self.namemenu = StringVar()
         self.namemenu.set('Select a Task')
         self.nameoptions = [ i['title'] for i in db.get_everything() ]
         
         style= ttk.Style()
         style.configure("TCombobox", fieldbackground= "white", background= "white")
         
         self.name_entry = ttk.Combobox(self.frame_sub, textvariable=self.namemenu, width=29, font=("Times New Roman", 18)) #self.namemenu, *self.nameoptions, command= lambda t=self.namemenu : getter(t))
         self.name_entry.place(anchor='center', relx=0.475, rely=0.68)
         self.name_entry.bind("<FocusIn>", combo_defocus)
         self.name_entry['values'] = self.nameoptions
         self.name_entry['state'] = 'readonly'
         self.namemenu.trace('w', getter)

         self.l3 = Label(self.frame_type, image = self.task_type, bg='#FEF4E8')
         self.l3.grid(row=3,column=1) 

         self.menu = StringVar()
         self.options = ("Daily", "Weekly", "Monthly")
         self.menu.set("Select Task Type")
         
         self.type_entry = ttk.Combobox(self.frame_type, textvariable=self.menu, width=29, font=("Times New Roman", 18))
         self.type_entry.place(anchor='center', relx=0.475, rely=0.68)
         self.type_entry.bind("<FocusIn>", combo_defocus)
         self.type_entry['values'] = self.options
         self.type_entry['state'] = 'readonly'
         self.menu.trace('w', type_getter)


         self.l4 = Label(self.frame_time, image = self.task_time, bg='#FEF4E8')
         self.l4.grid(row=4,column=1) 
         
         self.head_back = Button(self.frame_back, image = self.back, bg='#FEF4E8', borderwidth=0, command=headBack)
         self.head_back.grid(row=1,column=1)
         
         self.from_time = Button(self.frame_time, text="Pick a time of the day!", command= lambda t= "from": updateTime(t), font=("Times New Roman", 18), borderwidth=0, bg='white')
         self.from_time.place(anchor='center', relx=0.5, rely=0.49)

         self.to_time = Button(self.frame_time, text="Pick a time of the day!", command= lambda t= "to": updateTime(t), font=("Times New Roman", 18), borderwidth=0, bg='white')
         self.to_time.place(anchor='center', relx=0.5, rely=0.85)

         self.l5 = Button(self.frame_done, image = self.task_done, bg='#FEF4E8', borderwidth=0, command = submit_data)
         self.l5.grid(row=5,column=1) 

# if __name__ == "__main__":
#           root = update_plan()
#           root.state('zoomed')
#           root.mainloop()