import tkinter as tk
from tkinter import font
from tkinter import ttk

# color_scheme
light_red = '#ff2211'

my_todos = ['Check','me','out'] 

class App():
	def __init__(self):
		self.window = tk.Tk()
		self.window.title('MicroTasker')
		self.window.state('zoomed')
		self.h, self.w = self.window.winfo_screenheight(), self.window.winfo_screenwidth()

		self.frm_menu = self.create_menu()

		self.frm_todo = self.create_todo_frame()

		self.frm_menu.place(relx=0, rely=0, relwidth= 0.3, relheight=1)
		self.frm_todo.place(relx=0.3, rely=0, relwidth= 0.7, relheight=1)

	def run(self):
		self.window.mainloop()

	def create_menu(self):
		frm_menu = tk.Frame(self.window, bg=light_red)

		style = ttk.Style()
		style.configure('WB.TLabel', foreground='White', background=light_red, font=('Helvitica', 25, 'underline bold'))

		lbl_head = ttk.Label(frm_menu, text='Projects', style='WB.TLabel')
		lbl_head.place(rely=0.1, anchor='w')
		
		return frm_menu

	def create_todo_frame(self):
		frm_todo = tk.Frame(self.window)

		lbl_head = ttk.Label(frm_todo, text='Project')
		lbl_head.pack()

		my_entry = ttk.Entry(frm_todo)
		my_entry.pack()

		# border radius
		btn_add = ttk.Button(frm_todo, text ='+')
		btn_add.pack()

		self.show_todos(frm_todo)

		return frm_todo

	def show_todos(self, frame):
		for task in my_todos:
			lbl_task = tk.Label(frame, text=task)
			lbl_task.pack()

			# border radius
			btn_del = ttk.Button(frame, text='Remove')
			btn_del.pack()

def main():
	app = App()
	app.run()

if __name__ == '__main__':
	main()