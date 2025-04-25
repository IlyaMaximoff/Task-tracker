import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        task_listBox.insert(tk.END,task)
        task_entry.delete(0,tk.END)
def delete_task():
    selected_task = task_listBox.curselection()
    if selected_task:
        task_listBox.delete(selected_task)
def mark_task():
    selected_task = task_listBox.curselection()
    if selected_task:
        task_listBox.itemconfig(selected_task,bg="DarkGreen")
        workers_listBox.itemconfig(selected_task, bg="DarkGreen")
def add_performers():
    performers = task_entry.get()
    if performers:
        performers_listBox.insert(tk.END, performers)
        task_entry.delete(0, tk.END)
def delete_performers():
    selected_performers = performers_listBox.curselection()
    if selected_performers:
        performers_listBox.delete(selected_performers)
def assign_performer():
    selected_task = task_listBox.curselection()
    selected_performer = performers_listBox.curselection()
    if not selected_task or not selected_performer: # Проверка на невыделенный элемент списка
        messagebox.showerror("Ошибка", "Выберите задачу и исполнителя!")
        return
    task = task_listBox.get(selected_task)
    performer = performers_listBox.get(selected_performer)
    if f"{task} → {performer}" in workers_listBox.get(0, tk.END): # Проверка на дубли
        messagebox.showwarning("Предупреждение", "Эта связка уже существует!")
        return
    workers_listBox.insert(tk.END, f"{task} → {performer}")

root = tk.Tk()
root.title("Task list")
root.configure(background="grey33")
text1 = tk.Label(root,text="Введите задачу / Исполнителя",bg="grey33",fg="White")
text1.pack(pady=5)
task_entry = tk.Entry(root,width=50,bg="azure3",fg="black")
task_entry.pack(pady=10)
# Создаем фрейм для кнопок в два столбца
button_frame = tk.Frame(root)
button_frame.pack(pady=10)
# Левый столбец кнопок
left_button_frame = tk.Frame(button_frame)
left_button_frame.grid(row=0, column=0, padx=5)
add_task_button = tk.Button(left_button_frame,text="Добавить задачу",width=25,command=add_task)
add_task_button.pack(pady=5)
delete_button = tk.Button(left_button_frame,text="Удалить задачу",bg="firebrick1",width=25,command=delete_task)
delete_button.pack(pady=5)
mark_button = tk.Button(left_button_frame,text="Отметить выполненную задачу",bg="chartreuse",width=25,command=mark_task)
mark_button.pack(pady=5)
# Правый столбец кнопок
right_button_frame = tk.Frame(button_frame)
right_button_frame.grid(row=0, column=1, padx=5)
add_performer_button = tk.Button(right_button_frame,text="Добавить исполнителя",width=25,command=add_performers)
add_performer_button.pack(pady=5)
delete_performers_button = tk.Button(right_button_frame,text="Удалить исполнителя",bg="firebrick1",width=25,command=delete_performers)
delete_performers_button.pack(pady=5)
assign_performer_button = tk.Button(right_button_frame,text="Назначить исполнителя",bg="DarkGoldenrod1",width=25,command=assign_performer)
assign_performer_button.pack(pady=5)
# Общий контейнер для двух блоков
main_frame = tk.Frame(root)
main_frame.pack(pady=10)
# --- Блок задач (слева) ---
frame_left = tk.Frame(main_frame)
frame_left.pack(side="left", padx=10)
label_tasks = tk.Label(frame_left, text="Список задач", bg="grey33", fg="white")
label_tasks.pack(fill="x")
task_listBox = tk.Listbox(frame_left,exportselection=False, height=5, width=50, bg="grey78")
task_listBox.pack(fill="x")
# --- Блок исполнителей (справа) ---
frame_right = tk.Frame(main_frame)
frame_right.pack(side="left", padx=10)
label_workers = tk.Label(frame_right, text="Список исполнителей", bg="grey33", fg="white")
label_workers.pack(fill="x")
performers_listBox = tk.Listbox(frame_right,exportselection=False, height=5, width=20, bg="grey78")
performers_listBox.pack(fill="x")
# --- Блок "В работе" ---

label_workers = tk.Label(root, text="В работе", bg="grey33", fg="white")
label_workers.pack(fill="x")
workers_listBox = tk.Listbox(root, height=10, width=70, bg="grey78")
workers_listBox.pack(fill="x")

root.mainloop()
