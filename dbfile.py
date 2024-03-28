from pysondb import db

task_cursor = db.getDb("db_task.json")
note_cursor = db.getDb("db_note.json")
em = "NaN" # reusable constant string

# ADD function for last_updated_value

# TASK FUNCTIONS

def add_task(title, maintype, time, day, day_range, refID):
    task_cursor.add({"title": title, "maintype": maintype, "time": time, "day" : day, "day_range" : day_range, "last_updated": "2022-12-20-17-50-20", "completion": False, "refID" : refID}) 

def update_task(title, maintype, time, day, day_range, refID):
    # find using ID (made in task database) and keeping ID same update the task
    task_cursor.updateByQuery({"refID": refID}, {"title": title, "maintype": maintype, "time": time, "day" : day, "day_range" : day_range, "last_updated": "2022-12-20-17-50-20", "completion": False})

def show_tasks(maintype):
    query = task_cursor.getByQuery({"maintype": maintype})
    return query

def get_everything():
    query = task_cursor.getAll()
    return query

def show_all_tasks():
    query = task_cursor.getAll()
    tasklist = []
    for i in query:
        tasklist.append({"title":i["title"], "refID": i["refID"]})
    return tasklist

# NOTE FUNCTIONS

def add_note(title, description, task_id):
    note_cursor.add({"title": title, "description": description, "task_id": task_id})

# def update_note():

def show_notes():
    query = note_cursor.getAll()
    return query
   
 
# PROGRESS REPORT FUNCTIONS 

def show_progress():
    progress = []
    for main in ["DAY", "WEEK", "MONTH"]:
        
        completed = len(task_cursor.getByQuery({"maintype": main, "completion": True}))
        total = len(task_cursor.getByQuery({"maintype": main}))

        to_push = [completed, total-completed, total, 0]
        
        # set default values
        if to_push[1] == 0:
            to_push[1] = 1
        
        if to_push[0] == 0 and to_push[2] == 0 and to_push[0] == to_push[2]:
            to_push[3] = 0
        elif to_push[0] == to_push[2]:
            to_push[3] = 1
        

            
        progress.append(to_push)
    print(progress)
    return progress

def get_completion(refID):
    current_completion = task_cursor.getByQuery(({"refID": refID}))[0]['completion']
    print(current_completion)
    return current_completion

def set_completed(refID):
    task_cursor.updateByQuery({"refID": refID}, {"completion": True})
    print(f"Task with {refID} is set COMPLETED")
    
def set_incomplete(refID):
    task_cursor.updateByQuery({"refID": refID}, {"completion": False})
    print(f"Task with {refID} is set NOT COMPLETED")
