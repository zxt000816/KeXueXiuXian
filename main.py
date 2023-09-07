import tkinter as tk
from tkinter import ttk

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title('凡人修仙传人界篇')
        self.root.geometry('380x420')  # Set the size of the window

        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill='both', expand=True)

        self.pages = {}
        page_names = ["日程规划", "兽渊探秘", "魔道入侵 | 天地弈局 | 云梦试剑 | 虚天殿"]
        
        for page_name in page_names:
            if page_name == "日程规划":
                frame = Calendar(parent=self.notebook, controller=self)
            elif page_name == "兽渊探秘":
                frame = ShouYuan(parent=self.notebook, controller=self)
            else:
                frame = Page(parent=self.notebook, controller=self)

            self.pages[page_name] = frame
            self.notebook.add(frame, text=page_name)

    def show_frame(self, page_name):
        frame = self.pages[page_name]
        self.notebook.select(frame)

class Calendar(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        labels = [
            "天雷竹 (默认为0)：", "魔道入侵四倍 (默认为0)：", "魔道入侵挑战次数 (默认为0)：", 
            "星海火树 (默认为0)：", "兽渊探秘探查 (默认为0)：", 
            "玄玉葫芦 (默认为0)：","云梦试剑四倍 (默认为0)：", "云梦试剑挑战次数 (默认为0)：", 
            "堕天松 (默认为0)：", "虚天殿四倍 (默认为0)：", "虚天殿挑战次数 (默认为0)：",
            "灵眼神树 (默认为0)：", "天地弈局四倍 (默认为0)：", "天地弈局挑战次数 (默认为0)：",
         ]

        self.entries = []

        for i, label in enumerate(labels):
            self.label = tk.Label(self, text=label)
            self.label.grid(row=i, column=0)

            entry = tk.Entry(self)
            entry.grid(row=i, column=1)
            self.entries.append(entry)

        self.button = ttk.Button(self, text="提交", command=self.submit)
        self.button.grid(row=len(labels)+1, column=0, columnspan=2, sticky=tk.E+tk.W, padx=10, pady=10)

    def submit(self):
        values = [entry.get() for entry in self.entries]
        # Do something with values

class Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Create combobox for activity selection
        self.activity_combobox = self.create_combobox(["魔道入侵", "天地弈局", "云梦试剑", "虚天殿"], "魔道入侵", 0, tk.W)

        # Create input fields for activity details
        labels = ["四倍数量 (默认为0)：", "体力次数 (默认为0)：", "材料数量 (默认为0)："]
        self.input_fields = [self.create_input_field(label, i+1) for i, label in enumerate(labels)]

        # Create submit button
        self.submit_button = self.create_button("提交", self.submit, len(labels)+1)

    def create_combobox(self, values, default, row=0, sticky=None):
        combobox = ttk.Combobox(self, values=values)
        combobox.grid(row=row, column=0, columnspan=2, sticky=sticky)
        combobox.set(default)
        return combobox

    def create_input_field(self, label, row):
        input_label = tk.Label(self, text=label)
        input_label.grid(row=row, column=0)

        input_field = tk.Entry(self)
        input_field.grid(row=row, column=1)

        return input_field

    def create_button(self, text, command, row):
        button = ttk.Button(self, text=text, command=command)
        button.grid(row=row, column=0, columnspan=2, sticky=tk.E+tk.W, padx=10, pady=10)
        return button

    def submit(self):
        values = [field.get() for field in self.input_fields]
        selected_activity = self.activity_combobox.get()
        # Do something with values and selected_activity


class ShouYuan(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        labels = ["探查符数量 (默认为0)：", "材料数量 (默认为0)："]
        self.entries = []

        for i, label in enumerate(labels):
            self.label = tk.Label(self, text=label)
            self.label.grid(row=i, column=0)

            entry = tk.Entry(self)
            entry.grid(row=i, column=1)
            self.entries.append(entry)

        self.button = ttk.Button(self, text="提交", command=self.submit)
        self.button.grid(row=len(labels)+1, column=0, columnspan=2, sticky=tk.E+tk.W, padx=10, pady=10)

    def submit(self):
        values = [entry.get() for entry in self.entries]
        # Do something with values

if __name__ == "__main__":
    root = tk.Tk()
    root.iconbitmap('icon.ico')
    MainApp(root)
    root.mainloop()
