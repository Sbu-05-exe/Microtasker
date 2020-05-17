import tkinter as tk
from tkinter import font, ttk, StringVar

# color_scheme
light_red = '#ff2211'

my_todos = ['Check','me','out'] 


class App():
	def __init__(self):
		self.window = tk.Tk()
		self.window.title('MicroTasker')
		self.window.state('zoomed')
		self.h, self.w = self.window.winfo_screenheight(), self.window.winfo_screenwidth()
		self.todo = StringVar()

		self.frm_menu = self.create_menu()
		self.frm_todo, self.frm_todo_list = self.create_todo_frame()

		self.frm_menu.place(relx=0, rely=0, relwidth= 0.3, relheight=1)
		self.frm_todo.place(relx=0.3, rely=0, relwidth= 0.7, relheight=1)

	def run(self):
		self.window.mainloop()

	def create_menu(self):
		frm_menu = tk.Frame(self.window, bg=light_red)

		style = ttk.Style()
		style.configure('WB.TLabel', foreground='White', background=light_red, font=('Helvitica', 25, 'underline bold'))

		lbl_head = ttk.Label(frm_menu, text='Projects', style='WB.TLabel')
		lbl_head.place(rely=0.1,  relx=0.3)
		
		return frm_menu

	def create_todo_frame(self):
		frm_todo = tk.Frame(self.window)

		# on the frm_todo

		todo_text_frm = tk.Frame(frm_todo,background='#ababab')
		todo_text_frm.place(relwidth=1, relheight=0.3, rely=0)

		frm_todo_list = tk.Frame(frm_todo,background='#bababa')
		frm_todo_list.place(relwidth=1, relheight=0.7,rely=0.3)

		# Inside the text frame

		lbl_head = ttk.Label(todo_text_frm, text='Projects')
		lbl_head.place(relx=0.5,rely=0.2)

		my_entry = ttk.Entry(todo_text_frm, textvariable=self.todo)
		my_entry.place(relx=0.2, rely=0.5, relwidth=0.4,relheight=0.3)

		btn_add = ttk.Button(todo_text_frm, text ='+', command=self.add_todo)
		btn_add.place(relx=0.7, rely= 0.5, relheigh=0.3)

		self.show_todos(frm_todo_list)

		return frm_todo, frm_todo_list

	def show_todos(self, frame):

		i = 0

		for task in my_todos:
			todo_frame = tk.Frame(frame)
			todo_frame.place(relx=0.2,rely = 0.1 + i)

			lbl_task = tk.Label(todo_frame, text=task)
			lbl_task.pack(side='left')

			# border radius
			btn_del = ttk.Button(todo_frame, text='Done', command=self.remove_todo)
			btn_del.pack(side='right')
			btn_del.bind('Button>', self.remove_todo)

			i+= 0.1

	def add_todo(self):
		todo = self.todo.get()
		my_todos.append(todo)

		self.todo.set('')
		self.show_todos(self.frm_todo_list)

		return frm_todo

	def remove_todo(task):
		print(type(task))
		pass

def main():
	app = App()
	app.run()

if __name__ == '__main__':
	main()