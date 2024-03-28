from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext as st
from PIL import ImageTk, Image
from PIL import ImageDraw
import dbfile as db
import new_plan as new_plan
import update_plan as update_plan
import main_menu as main_menu
import day_menu as day_menu
# other way to make checkbox unpressed is by checking completion status and then updating it

class ScrollableFrame(Frame):
    
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        canvas = Canvas(self, width = 450, height=445, bg='#FEF4E8', highlightbackground='#FEF4E8', relief='ridge')
        
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = Frame(canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )
        
        
        def scroll_vertical(event):
            if scrollbar.get() != (0.0, 1.0):
                canvas.yview_scroll(-1 * int(event.delta / 60), "units")
                
        def bound_to_mousewheel(event):
    

            canvas.bind_all('<MouseWheel>', scroll_vertical)

        def unbound_to_mousewheel(event):
    
            canvas.unbind_all('<MouseWheel>')
            

            canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

            canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        canvas.bind("<Enter>", bound_to_mousewheel)
        canvas.bind("<Leave>", unbound_to_mousewheel)
        

   

   
class month_menu(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        def headBack():
            self.destroy()
            print("New-Plan")
            
            root = main_menu.main_menu()
            root.state('zoomed')
            root.mainloop()
            
        def headForward():
            self.destroy()
            print("New-Plan")
            
            root = day_menu.day_menu()
            root.state('zoomed')
            root.mainloop()
        
        def newPlan():
            self.destroy()
            print("New-Plan")
            
            root = new_plan.new_plan()
            root.state('zoomed')
            root.mainloop()
            
            
        def updatePlan():
            self.destroy()
            print("Update-Plan")
            
            root = update_plan.update_plan()
            root.state('zoomed')
            root.mainloop()
        
        def done(current_over):
            print(current_over)
            # print(self.block_check.instate(['selected']))
            # print(self.block_check.state())
            current_completion = db.get_completion(current_over[1])
            
            if current_completion == False:
                db.set_completed(current_over[1])
            else:
                db.set_incomplete(current_over[1])

        
        # General Properties
        self.title('Task Scheduler')
        self.geometry('480x900')
        self.minsize(480,900)
        self.maxsize(480,900)
        self['background'] = '#FEF4E8'
        
        # Header
        self.frame_wave = Frame(self, width=400, height=400, bg='#FEF4E8')
        self.frame_wave.place(anchor='center', relx=0.5, rely=0.1)
        self.wave = ImageTk.PhotoImage(Image.open("assets/Header/month_header.png")) 
        
        # Back
        self.frame_back = Frame(self, width=400, height=400, bg='#FEF4E8')
        self.frame_back.place(anchor='center', relx=0.08, rely=0.125)
        self.back = ImageTk.PhotoImage(Image.open("assets/Navigation/back.png")) 
        
        # Forward
        self.frame_forward = Frame(self, width=400, height=400, bg='#FEF4E8')
        self.frame_forward.place(anchor='center', relx=0.92, rely=0.125)
        self.forward = ImageTk.PhotoImage(Image.open("assets/Navigation/forward.png")) 
        
        # Add a Note
        self.frame_newplan = Frame(self, width=200, height=400, bg='#FEF4E8')
        self.frame_newplan.place(anchor='center', relx=0.5, rely=0.25)
        self.newplan= ImageTk.PhotoImage(Image.open("assets/new_plan.png")) 
        
        # Update Existing Note
        self.frame_updateplan = Frame(self, width=200, height=400, bg='#FEF4E8')
        self.frame_updateplan.place(anchor='center', relx=0.5, rely=0.33)
        self.updateplan = ImageTk.PhotoImage(Image.open("assets/update_plan.png"))

        # Base
        self.frame_base = Frame(self, width=200, height=400, bg='#FEF4E8')
        self.frame_base.place(anchor='center', relx=0.5, rely=0.40)
        self.base = ImageTk.PhotoImage(Image.open("assets\Intro\iphone_base.png"))
        
        # Show Notes
        self.frame = ScrollableFrame(self)
        self.frame.place(anchor='n', relx=0.5, rely=0.43)
        self.img = ImageTk.PhotoImage(Image.open('assets/plan.png'))
        
        #  All added tasks
        self.data_dir = []
        self.var = (db.show_tasks("MONTH"))
        for i in range(len(self.var)):
            self.data_dir.append([self.var[i]['title'], self.var[i]['day_range'], self.var[i]['refID'], self.var[i]['completion']])
            
        for data in self.data_dir:
            print(data[0])

            self.rise = Canvas(self.frame.scrollable_frame, bg='#FEF4E8', width = 450, height=100, borderwidth=0)
            self.rise.create_image(450,5, anchor=NE, image=self.img)
            self.rise.pack()
   
            self.block_title = Label(self.rise ,bg='#FEF4E8', text = f"{data[0]}",font=("Arial", 15))
            self.rise.create_window(30 , 35, anchor=W, window=self.block_title)
            
            self.block_time = Label(self.rise ,bg='#FEF4E8', text = f"{data[1][0]} - {data[1][1]}",font=("Arial", 12))
            self.rise.create_window(70 , 70, anchor=W, window=self.block_time)
            
            self.bar = IntVar
            s = ttk.Style()
            s.configure('Red.TCheckbutton', foreground='red')
            self.block_check = ttk.Checkbutton(self.rise ,style='Red.TCheckbutton',variable=self.bar, command = lambda p=[data[0], data[2]]: done(p))
            self.rise.create_window(380 , 50, anchor=W, window=self.block_check)
            
            
            if data[3] == False:
                self.block_check.state(['!alternate'])
            elif data[3] == True:
                self.block_check.state(['selected'])
            else:
                pass
            


        
        self.header = Label(self.frame_wave, image = self.wave, bg='#FEF4E8')
        self.header.grid(row=1,column=1)
        
        self.head_back = Button(self.frame_back, image = self.back, bg='#FEF4E8', borderwidth=0, command=headBack)
        self.head_back.grid(row=1,column=1)
        
        self.head_forward = Button(self.frame_forward, image = self.forward, bg='#FEF4E8', borderwidth=0, command=headForward)
        self.head_forward.grid(row=1,column=1)

        self.adder = Button(self.frame_newplan, image = self.newplan, bg='#FEF4E8', borderwidth=0, command=newPlan)
        self.adder.grid(row=2,column=1)
        
        self.editor = Button(self.frame_updateplan, image = self.updateplan, bg='#FEF4E8', borderwidth=0, command=updatePlan)
        self.editor.grid(row=3,column=1)


        self.sep = Label(self.frame_base, image =self.base, bg='#FEF4E8')
        self.sep.grid(row=4,column=1) 
        

# if __name__ == "__main__":
#     root = month_menu()
#     root.state('zoomed')
#     root.mainloop()