import tkinter as tk
from tkinter import font
from tkinter import ttk

class App():
	def __init__(self):
		self.window = tk.Tk()
		self.window.title('MicroTasker')
		self.window.state('zoomed')
		self.h, self.w = self.window.winfo_screenheight(), self.window.winfo_screenwidth()

		style = ttk.Style()
		style.configure('Menu.TFrame', background='Blue', width=(self.w*0.3))

		self.frm_menu = self.create_menu()

		style.configure('Todo.TFrame,', background='White', width=(self.w*0.7))
		self.frm_todo = self.create_todo_frame()

		self.frm_menu.pack(side='left', expand=False, fill='both')
		self.frm_todo.pack(side='right', expand=True, fill='both')

	def run(self):
		self.window.mainloop()

	def create_menu(self):
		frm_menu = ttk.Frame(self.window, style='Menu.TFrame', padding=(100,100))

		style = ttk.Style()
		style.configure('WB.TLabel', foreground='White', background='Blue', font=('Helvitica', 25, 'underline bold'))

		lbl_head = ttk.Label(frm_menu, text='Projects', style='WB.TLabel')
		lbl_head.pack()
		
		return frm_menu

	def create_todo_frame(self):
		frm_todo = ttk.Frame(self.window, style='Todo.TFrame', padding=60)

		style = ttk.Style()
		style.configure('H1.TLabel', foreground='Black', font=('Helvitica', 30))

		lbl_Head = ttk.Label(frm_todo, text='Todo List', style='H1.TLabel')
		lbl_Head.pack(side='top')

		style.configure('P.TEntry', font=('Arial', 15), height=20, width = 50)
		entry_todo = ttk.Entry(frm_todo)
		entry_todo.pack(side='top')
		
		return frm_todo


def main():
	app = App()
	app.run()

if __name__ == '__main__':
	main()