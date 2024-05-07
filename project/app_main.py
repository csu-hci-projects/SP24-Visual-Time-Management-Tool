import tkinter as tk
from tkinter import messagebox
import time

class Task:
    def __init__(self, name, time):
        self.name = name
        self.time = time

tasks = []
current_task = Task("No Task Selected", 0)

def addTask():
    name = add_task_box.get()
    time = add_time.get()
    add_task_box.delete(0, tk.END)
    add_time.delete(0, tk.END)

    if name == "" or time == "":
        messagebox.showinfo("Message", "Please Insert both task and time before adding task")
        return
    if not time.replace(".", "").isnumeric():
        messagebox.showinfo("Message", "Please Enter a Valid Number")
        return
    
    task = Task(name, float(time))
    tasks.append(task)

    group = tk.Frame(master=task_frame, bg="white")
    group.pack(fill=tk.X)
    group.rowconfigure(0, minsize=10)
    group.columnconfigure([0,1,2], minsize=148)

    show_task = tk.Label(master=group, text=name)
    show_task.grid(row=0, column=0, sticky="nw")

    global show_time
    show_time = tk.Label(master=group, text=time + " hours")
    show_time.grid(row=0, column=1, sticky= "nw")

    tasknum = tk.Label(master=group, text="# " + str(len(tasks)))
    tasknum.grid(row=0, column=2)

def selectTask():
    taskIndex = set_task.get()
    set_task.delete(0, tk.END)

    if not taskIndex.isnumeric():
        messagebox.showinfo("Message", "Please Enter a Valid Number")
        return
    
    taskIndex = int(taskIndex)

    if taskIndex > len(tasks):
        messagebox.showinfo("Message", "Please Enter a Valid Number")
        return
    
    global current_task
    current_task = tasks[taskIndex-1] 
    global c_task
    c_task.config(text=current_task.name)
    global c_time
    c_time.config(text=current_task.time)

def decrementTime():
    dtime = log.get()
    log.delete(0, tk.END)
    if not dtime.replace(".", "").isnumeric():
        messagebox.showinfo("Message", "Please Enter a Valid Number")
        return
    dtime = float(dtime)
    if dtime > current_task.time:
        messagebox.showinfo("Message", "Please Enter a Valid Number")
        return

    current_task.time = current_task.time - dtime
    global c_time
    c_time.config(text=current_task.time)
    global show_time
    show_time.config(text=current_task.time)

def startTime():
    if len(tasks) == 0:
        messagebox.showinfo("Message", "Please select a task before clocking in")
        return
    global start_time
    start_time = time.time()

def endTime():
    global end_time
    end_time = time.time()
    t_time = end_time - start_time
    if current_task.time - t_time/60 < 0:
        current_task.time = 0
    else:
        current_task.time = current_task.time - t_time/60
    c_time.config(text=current_task.time)
    show_time.config(text=current_task.time)


window = tk.Tk()
window.title("Deepwork Manager")


#Main task frame
task_frame = tk.Frame(master=window, bg="gray")
task_frame.pack(fill=tk.Y, side=tk.LEFT)

task_instruct = tk.Label(master=task_frame, bg="gray", text="Tasks")
task_instruct.pack(fill=tk.X)


#Add task thing
add_task_frame = tk.Frame(master=task_frame, bg="gray")
add_task_frame.pack(fill=tk.X)
add_task_frame.rowconfigure([0,1], minsize=10)
add_task_frame.columnconfigure([0,1,2],minsize=10)

task_name = tk.Label(master=add_task_frame, text="Task Name")
task_name.grid(row=0, column=0, sticky="ws")
task_time = tk.Label(master=add_task_frame, text="Expected Time (Hours)")
task_time.grid(row=0, column=1, sticky="ws")

add_task_box = tk.Entry(master=add_task_frame)
add_task_box.grid(row=1,column=0, sticky="wn")

add_time = tk.Entry(master=add_task_frame)
add_time.grid(row=1, column=1, sticky="wn")

add_task_button = tk.Button(master=add_task_frame, text="Add", command=addTask)
add_task_button.grid(row=1,column=2, sticky="wn")


#Current Task person is working on
main_frame = tk.Frame(master=window, bg="gray")
main_frame.pack(fill=tk.X, expand=False)
main_frame.rowconfigure([0,1,2], minsize=10)
main_frame.columnconfigure([0,1], minsize=50)

set_taskI = tk.Label(master=main_frame, text="Insert Task # you want to work on")
set_taskI.grid(row=0, column=0)
set_task = tk.Entry(master=main_frame)
set_task.grid(row=1, column=0)
set_taskB = tk.Button(master=main_frame, text="Select", command=selectTask)
set_taskB.grid(row=2, column=0)

global c_task
c_task = tk.Label(master=main_frame, text=current_task.name)
c_task.grid(row=0, column=1, sticky = "e")
global c_time
c_time = tk.Label(master=main_frame, text=current_task.time)
c_time.grid(row=1, column=1, sticky = "e")

#Now for the methods
#1
m1 = tk.Frame(master=window, bg="gray")
m1.pack(fill=tk.BOTH, expand=True)
m1.rowconfigure(0, minsize=10)
m1.columnconfigure([0,1], minsize=10)

global start_time
start_time = time.time()
cin = tk.Button(master=m1, text="Clock In", command = startTime)
cin.grid(row=0,column=0)

global end_time
end_time = time.time()
cout = tk.Button(master=m1, text="Clock Out", command = endTime)
cout.grid(row=0, column=1)



#2
m2 = tk.Frame(master=window, bg="gray")
m2.pack(fill=tk.BOTH, expand=True)
m2.rowconfigure([0,1,2], minsize=10)
m2.columnconfigure(0, minsize=10)

instruct2 = tk.Label(master=m2, text="Please Insert how much time you spent on this task bellow")
instruct2.grid(row=0, column=0)
log = tk.Entry(master=m2)
log.grid(row=1, column=0)
takeoff = tk.Button(master=m2, text="Submit", command=decrementTime)
takeoff.grid(row=2, column=0)




window.mainloop()
