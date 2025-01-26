import tkinter as tk
from tkinter import messagebox


def add_task():
    task = entry.get()
    if task:
        task_lst.insert(tk.END,task)
        entry.delete(0,tk.END)

    else:
        messagebox.showwarning("Warning", "Task can't be empty!")


def delete_task():
    try:
        task_index = task_lst.curselection()[0]
        task_lst.delete(task_index)

    except IndexError:
        messagebox.showwarning("Warning","Please select a task to delete!")


def view_task():

    done_count = 0
    total_count = task_lst.size()
    for i in range(total_count):
        if task_lst.itemcget(i,"fg") == "green":
            dont_count += 1

    messagebox.showinfo("Task Statistics", f"Total tasks: {total_count}\nCompleted tasks: {done_count}")

def mark_task():
    task_index = task_lst.curselection()
    if task_index:
        task_lst.itemconfig(task_index, fg="green")
        task_lst.selection_clear(task_index)  # Deselect the task if needed
        task_lst.selection_set(task_index)  


def exit_task():
    root.destroy()
    


# Initialize the Tkinter window
root = tk.Tk()
root.title("To-Do List")
root.geometry("500x500")
root.resizable(False,False)
root.config(bg="orange")


# Title Label
label = tk.Label(root, text = "TODO-LIST", font=("Helvetica", 16))
label.pack(padx=5,pady=5)

#input from user
user_input = tk.Frame(root)
user_input.pack(pady=10)

#task_entry field
entry = tk.Entry(user_input,width=45 )
entry.grid(row=1,column=0,padx=7,ipady=4)

#add task button
add_button = tk.Button(user_input, width = 10, text="Add Task", bd=2, relief="solid",bg= "#1068b5", fg="white", font=("Helvetica", 10), command=add_task)
add_button.grid(row=1,column=1,padx=3)

#listbox to display tasks
task_lst = tk.Listbox(root, width=54, height=18,  font=("Helvetica", 10),selectmode=tk.SINGLE)
task_lst.pack(padx=0,pady=0)

#button frame for action buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

#mark task button
mark_button = tk.Button(btn_frame, width = 13, bd=2, relief="solid", bg="#1eb510", fg="white" , text="Mark",font=("Helvetica", 10),command=view_task)
mark_button.grid(row=1,column=0,padx=7,pady=7)

#delete task button
dlt_button_button = tk.Button(btn_frame, width = 13, bd=2, relief="solid" ,bg="red", fg="white" ,  text="Delete",font=("Helvetica", 10), command=delete_task)
dlt_button_button.grid(row=1,column=3,padx=7,pady=7)

#exit task button
exit_button = tk.Button(btn_frame, width = 13, bd=2, relief="solid" , text="Exit",font=("Helvetica", 10), command=exit_task)
exit_button.grid(row=1,column=5,padx=7,pady=7)

#run the main loop
root.mainloop()