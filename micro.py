import tkinter as tk
from tkinter import ttk

class App():
	def __init__(self):
		self.window = tk.Tk()
		self.window.title('MicroTasker')
		self.window.state('zoomed')
		self.h, self.w = self.window.winfo_screenheight(), self.window.winfo_screenwidth()

		self.frm_menu = self.create_menu()
		self.frm_todo = self.create_todo_frame()

		self.frm_menu.pack(side='left', expand=True, fill='both')
		self.frm_todo.pack(side='right', expand=True, fill='both')

	def run(self):
		self.window.mainloop()

	def create_menu(self):
		my_frame = tk.Frame(self.window, bg='Red', height=self.h, width = (self.w*0.3))

		
		return my_frame

	def create_todo_frame(self):
		return tk.Frame(self.window, bg='Blue', width=(self.w*0.7))


def main():

	app = App()
	app.run()

if __name__ == '__main__':
	main()