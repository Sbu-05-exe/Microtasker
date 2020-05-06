import tkinter as tk
from tkinter import ttk

class Application(tk.Frame):
	def __init__(self, master = None):
		super().__init__(master)
		self.master = master
		self.pack()
		self.createDashboard()

	def createDashboard(self):
		pass
		# self.menu = createMenu()
		# menu.pack(side='left')

		# self.todoFrame = createTodoFrame()
		# menu.pack(side='right') 
 

def main():
	root = tk.Tk()

	app = Application(master=root)
	app.mainloop()

if __name__ == '__main__':
	main()