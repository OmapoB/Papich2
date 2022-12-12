from tkinter import *



class MainWindow:
    def __init__(self, master):
        self.main_window = master
        self.main_window.title('PapichLoh2.exe')
        self.main_window.geometry(f'{295}x{125}')
        self.main_window.resizable(False, False)
        self.main_window.columnconfigure([0, 1], minsize=100)
        self.main_window.rowconfigure([0, 1, 2], minsize=20)
        self.amount_label = Label(text='Основной склад')
        self.amount_label.grid(row=0, column=0)
        self.amount_input = Entry()
        self.amount_input.grid(row=0, column=1)
        self.article_label = Label(text='Артикулы')
        self.article_label.grid(row=1, column=0)
        self.article_input = Entry()
        self.article_input.grid(row=1, column=1)
        self.save_label = Label(text='Сохранить в')
        self.save_label.grid(row=2, column=0)
        self.save_input = Entry()
        self.save_input.grid(row=2, column=1)
        self.submit = Button(text='не стонкс(', width=10)
        self.submit.grid(row=3, column=1, sticky='e')

    def get_amount_input(self):
        return self.amount_input.get()

    def get_article_input(self):
        return self.article_input.get()

    def get_save_input(self):
        return self.save_input.get()
