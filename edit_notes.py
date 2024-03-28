from tkinter import *
from tkinter import scrolledtext
from PIL import ImageTk, Image
from tktimepicker import *
import dbfile as db
import show_notes as show_notes
import main_menu as main_menu

class edit_notes(Tk):
   def __init__(self, *args, **kwargs):
       super().__init__(*args, **kwargs)
       
       def headBack():
            self.destroy()
            print("New-Plan")
            
            root = main_menu.main_menu()
            root.state('zoomed')
            root.mainloop()
        
       # General Properties
       self.title('Task Scheduler')
       self.geometry('480x900')
       self.minsize(480,900)
       self.maxsize(480,900)
       self['background'] = '#FEF4E8'
       self.state('zoomed')

       # Wave
       self.header = Frame(self, width=200, height=400, bg='#FEF4E8')
       self.header.place(anchor='center', relx=0.52, rely=0.03)
       self.wave = ImageTk.PhotoImage(Image.open("assets/AddNotes/editing_note.png"))
       
       # Back
       self.frame_back = Frame(self, width=400, height=400, bg='#FEF4E8')
       self.frame_back.place(anchor='center', relx=0.07, rely=0.06)
       self.back = ImageTk.PhotoImage(Image.open("assets/Navigation/back.png"))
         
       self.head_back = Button(self.frame_back, image = self.back, bg='#FEF4E8', borderwidth=0, command=headBack)
       self.head_back.grid(row=1,column=1)
       
       # task name
       self.frame_sub = Frame(self, width=200, height=400, bg='#FEF4E8')
       self.frame_sub.place(anchor='center', relx=0.5, rely=0.20)
       self.sub = ImageTk.PhotoImage(Image.open("assets/AddNotes/note_name.png"))

       self.frame_type = Frame(self, width=200, height=400, bg='#FEF4E8')
       self.frame_type.place(anchor='center', relx=0.5, rely=0.38)
       self.task_type = ImageTk.PhotoImage(Image.open("assets/AddNotes/corresponding_task.png"))

       self.frame_time = Frame(self, width=200, height=400, bg='#FEF4E8')
       self.frame_time.place(anchor='center', relx=0.5, rely=0.65)
       self.task_time = ImageTk.PhotoImage(Image.open("assets/AddNotes/describe_color.png"))

       self.frame_done = Frame(self, width=200, height=400, bg='#FEF4E8')
       self.frame_done.place(anchor='center', relx=0.5, rely=0.88)
       self.task_done = ImageTk.PhotoImage(Image.open("assets/NewPlan/done.png"))

       self.l1 = Label(self.header, image = self.wave, bg='#FEF4E8')
       self.l1.grid(row=1,column=1)

       self.l2 = Label(self.frame_sub, image = self.sub, bg='#FEF4E8')
       self.l2.grid(row=2,column=1) 

       self.notename = ""
       self.notename_entry = Entry(self.frame_sub, textvariable = self.notename, font=("Times New Roman", 18), width=30)
       self.notename_entry.place(anchor='center', relx=0.47, rely=0.7)
       self.notename_entry["borderwidth"]=0

       self.l3 = Label(self.frame_type, image = self.task_type, bg='#FEF4E8')
       self.l3.grid(row=3,column=1) 

       self.all_tasks = db.show_all_tasks()
       print(self.all_tasks)

       self.selected_task = []

       def setter(current_list):
         print("Current selected option -->", current_list)
         self.but.configure(text=current_list[0])
         
         # global selected_task
         self.selected_task = current_list

       def create_menu():
         self.notetype_entry.delete(0, tkinter.END)
         for textvar in self.all_tasks:
            
            self.notetype_entry.add_command(label=f"{textvar['title']}", command = lambda t=[f"{textvar['title']}",textvar['refID']]: setter(t))
            
       def submit_data():
         note_name = self.notename_entry.get()
         note_desc = self.multi.get("1.0",'end-1c')
         print(note_name, self.selected_task[1], note_desc)
   
         if note_name=="" and note_desc=="":
            print("Please complete the note")
         else:
            db.add_note(note_name, note_desc, self.selected_task[1])
            self.destroy()
            root = show_notes.show_notes()
            root.state('zoomed')
            root.mainloop()
            

       self.but = Menubutton(text="NaN", bg="white", font=("Times New Roman", 20))
       self.notetype_entry = Menu(self.but, postcommand=create_menu, tearoff=0)
       self.but.configure(menu=self.notetype_entry)
       self.but.place(anchor='center', relx=0.5, rely=0.41)


       self.l4 = Label(self.frame_time, image = self.task_time, bg='#FEF4E8')
       self.l4.grid(row=4,column=1) 


       self.multi = scrolledtext.ScrolledText(self, wrap=WORD,width=35, height=9,font=("Times New Roman", 15))
       self.multi['borderwidth']=0
       self.multi.place(anchor='center', relx=0.498, rely=0.685)


       self.l5 = Button(self.frame_done, image = self.task_done, bg='#FEF4E8', borderwidth=0, command = submit_data)
       self.l5.grid(row=5,column=1)


# if __name__ == "__main__":
#     root = edit_notes()
#     root.mainloop()