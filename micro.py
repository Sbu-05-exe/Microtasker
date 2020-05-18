import tkinter as tk
from tkinter import font, ttk, StringVar

# color_scheme
light_red = '#ff2211'

my_todos = ['Check','me','out'] 

class Task(tk.Frame):
	def __init__(self,parent, task):
		super().__init__(parent)

		lbl_todo = tk.Label(self, text=task)
		lbl_todo.pack(side='left')

		btn_done = ttk.Button(self, command=self.remove_task, text='done')
		btn_done.pack(side='right')

		self.task = task

	def remove_task(self):
		index = my_todos.remove(self.task)
		print(my_todos)
		self.destroy()

class App():
	def __init__(self):
		self.window = tk.Tk()
		self.window.title('MicroTasker')
		self.window.state('zoomed')
		self.h, self.w = self.window.winfo_screenheight(), self.window.winfo_screenwidth()
		self.todo = StringVar()

		self.frm_menu = self.create_menu()
		self.dashboard, self.frm_todos = self.create_dashboard()

		self.frm_menu.place(relx=0, rely=0, relwidth= 0.3, relheight=1)
		self.dashboard.place(relx=0.3, rely=0, relwidth= 0.7, relheight=1)

	def run(self):
		self.window.mainloop()

	def create_menu(self):
		frm_menu = tk.Frame(self.window, bg=light_red)

		style = ttk.Style()
		style.configure('WB.TLabel', foreground='White', background=light_red, font=('Helvitica', 25, 'underline bold'))

		lbl_head = ttk.Label(frm_menu, text='Projects', style='WB.TLabel')
		lbl_head.place(rely=0.1,  relx=0.3)
		
		return frm_menu

	def create_dashboard(self):
		frm_dashboard = tk.Frame(self.window)

		# on the frm_todo

		todo_text_frm = tk.Frame(frm_dashboard,background='#ababab')
		todo_text_frm.place(relwidth=1, relheight=0.3, rely=0)

		frm_todos = tk.Frame(frm_dashboard,background='#bababa')
		frm_todos.place(relwidth=1, relheight=0.7,rely=0.3)

		# Inside the text frame

		lbl_head = ttk.Label(todo_text_frm, text='Projects')
		lbl_head.place(relx=0.5,rely=0.2)

		my_entry = ttk.Entry(todo_text_frm, textvariable=self.todo)
		my_entry.place(relx=0.2, rely=0.5, relwidth=0.4,relheight=0.3)

		btn_add = ttk.Button(todo_text_frm, text ='+', command=self.add_todo)
		btn_add.place(relx=0.7, rely= 0.5, relheigh=0.3)

		self.show_todos(frm_todos)

		return frm_dashboard, frm_todos

	def show_todos(self, frame):

		i = 0

		# clear the contents of the frame
		for child in frame.winfo_children():
			child.destroy()

		# add padding to the todo_frm using ttk
		pad_frm = tk.Frame(frame)
		pad_frm.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

		for todo in my_todos:
			task_frm = Task(pad_frm, todo)
			task_frm.pack(side='top')

	def add_todo(self):
		todo = self.todo.get()
		my_todos.append(todo)

		self.todo.set('')
		self.show_todos(self.frm_todos)

def main():
	app = App()
	app.run()

if __name__ == '__main__':
	main()