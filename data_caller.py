import dbfile as db

def data_listing(DType):
            data_list = []
            var = db.show_tasks(DType)
            
            for i in range(len(var)):
                  data_list.append([var[i]['title'], var[i]['refID'], var[i]['time'], var[i]['maintype']])
            
            return data_list
                  
def entry_listing(DType):
    var = data_listing(DType)
    entry_list = []
    for i in var:
        entry_list.append([i[0],i[1]])
    return entry_list

def get_name():
   file = open("your_name.txt", 'r')
   text = file.read()
   file.close()
   return text
