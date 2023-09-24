import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
from event_items import daily_work
from chong_bang import chong_bang

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title('凡人修仙传人界篇')
        self.root.geometry('400x500')  # Set the size of the window

        # Define the font
        font = tkFont.Font(family="Arial")

        # Create a Style object
        style = ttk.Style()

        # Set the font of the 'TNotebook.Tab' style
        style.configure('TNotebook.Tab', font=font)

        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill='both', expand=True)

        self.pages = {}
        page_names = ["日程规划", "灵根获取", "冲榜"]
        
        for page_name in page_names:
            if page_name == "日程规划":
                frame = Calendar(parent=self.notebook, controller=self)
            elif page_name == "冲榜":
                frame = ChongBang(parent=self.notebook, controller=self)
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
            "天雷竹 (默认为0)：", "星海火树 (默认为0)：", "玄玉葫芦 (默认为0)：","堕天松 (默认为0)：", "灵眼神树 (默认为0)：", "神物园加速次数(默认为23)：","分割线",
            "魔道入侵四倍 (默认为0)：", "兽渊探秘探查 (默认为0)：", "云梦试剑四倍 (默认为0)：", "虚天殿四倍 (默认为0)：", "天地弈局四倍 (默认为0)：", "分割线",
            "魔道入侵挑战次数 (默认为0)：", "云梦试剑挑战次数 (默认为0)：", "虚天殿挑战次数 (默认为0)：", "天地弈局挑战次数 (默认为0)：", 
        ]
        self.entries = {}

        for i, label in enumerate(labels):
            if label == "分割线":
                label = tk.Label(self, text="=" * 30, fg="green")
                label.grid(sticky="w")
                continue

            self.label = tk.Label(self, text=label, font=("Arial", 12))
            self.label.grid(row=i, column=0)

            entry = tk.Entry(self)

            if label == "神物园加速次数(默认为23)：":
                entry.insert(0, 23)
            else:
                entry.insert(0, 0)

            entry.grid(row=i, column=1)
            self.entries[label] = entry

        self.button = ttk.Button(self, text="提交", command=self.submit)
        self.button.grid(row=len(labels)+1, column=0, columnspan=2, sticky=tk.E+tk.W, padx=10, pady=10)

    def submit(self):
        values = {label: int(entry.get()) for label, entry in self.entries.items()}

        daily_work_params = [
            {
                "items_num": values["天雷竹 (默认为0)："],
                "core_num": values["魔道入侵四倍 (默认为0)："],
                "tili_num": values["魔道入侵挑战次数 (默认为0)："],
                "event_name": "魔道入侵",
                "jiasu_num": values["神物园加速次数(默认为23)："],
            },
            {
                "items_num": values["星海火树 (默认为0)："],
                "core_num": values["兽渊探秘探查 (默认为0)："],
                "tili_num": 0,
                "event_name": "兽渊探秘",
                "jiasu_num": values["神物园加速次数(默认为23)："],
            },
            {
                "items_num": values["玄玉葫芦 (默认为0)："],
                "core_num": values["云梦试剑四倍 (默认为0)："],
                "tili_num": values["云梦试剑挑战次数 (默认为0)："],
                "event_name": "云梦试剑",
                "jiasu_num": values["神物园加速次数(默认为23)："],
            },
            {
                "items_num": values["堕天松 (默认为0)："],
                "core_num": values["虚天殿四倍 (默认为0)："],
                "tili_num": values["虚天殿挑战次数 (默认为0)："],
                "event_name": "虚天殿",
                "jiasu_num": values["神物园加速次数(默认为23)："],
            },
            {
                "items_num": values["灵眼神树 (默认为0)："],
                "core_num": values["天地弈局四倍 (默认为0)："],
                "tili_num": values["天地弈局挑战次数 (默认为0)："],
                "event_name": "天地弈局",
                "jiasu_num": values["神物园加速次数(默认为23)："],
            }
        ]

        popup = tk.Toplevel()
        popup.title("日程规划")
        popup.geometry("400x500")

        scrollbar = tk.Scrollbar(popup)
        canvas = tk.Canvas(popup, yscrollcommand=scrollbar.set)

        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        frame = tk.Frame(canvas)
        canvas.create_window((0, 0), window=frame, anchor='nw')

        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar.config(command=canvas.yview)

        # Bind the mouse wheel event to the Canvas
        canvas.bind_all('<MouseWheel>', lambda event: canvas.yview_scroll(int(-1*(event.delta/120)), "units"))  # Add this line

        for params in daily_work_params:
            info = daily_work(**params)
            for key, value in info.items():
                if key != "需要的天数" and key != "需要的天数(不考虑体力)" and key != "活动":
                    label = tk.Label(
                        frame, 
                        text=f"{key}: {value}", 
                        font=("Arial", 12), 
                    )
                    label.grid(sticky="w")
                else:
                    label_days_needed = tk.Label(frame, text=f"{key}: {value}", font=("Arial", 12), fg="red")
                    label_days_needed.grid(sticky="w")
            
            label = tk.Label(frame, text="=" * 40, fg="green")
            label.grid(sticky="w")
        
        frame.update()
        # Update the scrollregion after the Canvas contents change
        canvas.config(scrollregion=canvas.bbox('all'))
        
class Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Create combobox for activity selection
        combobox = ttk.Combobox(self, values=["魔道入侵", "兽渊探秘", "天地弈局", "云梦试剑", "虚天殿"], font=("Arial", 12))
        combobox.grid(row=0, column=0, columnspan=2, sticky=tk.W)
        combobox.set("魔道入侵")
        self.activity_combobox = combobox

        # Create input fields for activity details
        labels = ["灵根数量(默认为1)：", "四倍/探查符数量(默认为0)：", "体力次数(默认为0)：", "材料数量(默认为0)：", "神物园加速次数(默认为23)："]
        
        self.entries = {}
        for i, label in enumerate(labels):
            self.label = tk.Label(self, text=label, font=("Arial", 12))
            self.label.grid(row=i+1, column=0)

            entry = tk.Entry(self)
            if label == "神物园加速次数(默认为23)：":
                entry.insert(0, 23)
            elif label == "灵根数量(默认为1)：":
                entry.insert(0, 1)
            else:
                entry.insert(0, 0)

            entry.grid(row=i+1, column=1)
            self.entries[label] = entry
        
        # Create submit button
        self.button = ttk.Button(self, text="提交", command=self.submit)
        self.button.grid(row=len(labels)+1, column=0, columnspan=2, sticky=tk.E+tk.W, padx=10, pady=10)

    def submit(self):
        values = {label: int(entry.get()) for label, entry in self.entries.items()}
        selected_activity = self.activity_combobox.get()

        popup = tk.Toplevel()
        popup.title(f"{selected_activity}")
        popup.geometry("350x200")

        activity_info = daily_work(
            items_num=values["材料数量(默认为0)："],
            core_num=values["四倍/探查符数量(默认为0)："],
            tili_num=values.get("体力次数(默认为0)：", 0),
            event_name=selected_activity,
            jiasu_num=values["神物园加速次数(默认为23)："],
            num_of_linggen=values["灵根数量(默认为1)："]
        )

        for key, value in activity_info.items():
            if key != "需要的天数" and key != "需要的天数(不考虑体力)" and key != "活动":
                label = tk.Label(
                    popup, 
                    text=f"{key}: {value}", 
                    font=("Arial", 12), 
                )
                label.grid(sticky="w")
            else:
                label_days_needed = tk.Label(popup, text=f"{key}: {value}", font=("Arial", 12), fg="red")
                label_days_needed.grid(sticky="w", padx=5)

class ChongBang(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Create combobox for activity selection
        combobox = ttk.Combobox(self, values=["魔道入侵", "兽渊探秘", "天地弈局", "云梦试剑", "虚天殿"], font=("Arial", 12))
        combobox.grid(row=0, column=0, columnspan=2, sticky=tk.W)
        combobox.set("魔道入侵")
        self.activity_combobox = combobox

        labels = ["当前兑换积分：", "目标兑换积分：", "分割线", "当前排名积分：", "目标排名积分：", "分割线", "天地弈局每次获得棋符数量："]
        
        self.entries = {}
        for i, label in enumerate(labels):
            if label == "分割线":
                label = tk.Label(self, text="=" * 30, fg="green")
                label.grid(sticky="w")
                continue

            self.label = tk.Label(self, text=label, font=("Arial", 12))
            self.label.grid(row=i+1, column=0)

            entry = tk.Entry(self)
            entry.insert(0, 0)

            entry.grid(row=i+1, column=1)
            self.entries[label] = entry
        
        # Create submit button
        self.button = ttk.Button(self, text="提交", command=self.submit)
        self.button.grid(row=len(labels)+1, column=0, columnspan=2, sticky=tk.E+tk.W, padx=10, pady=10)

    def submit(self):
        values = {label: int(entry.get()) for label, entry in self.entries.items()}
        selected_activity = self.activity_combobox.get()

        popup = tk.Toplevel()
        popup.title(f"{selected_activity}")
        popup.geometry("400x200")

        if selected_activity == "天地弈局":
            activity_info = chong_bang(
                event=selected_activity,
                current_score=values["当前兑换积分："],
                current_rank_score=values["当前排名积分："],
                target_score=values["目标兑换积分："],
                target_rank_score=values["目标排名积分："],
                qifu_per_time=values["天地弈局每次获得棋符数量："]
            )
        else:
            activity_info = chong_bang(
                event=selected_activity,
                current_score=values["当前兑换积分："],
                current_rank_score=values["当前排名积分："],
                target_score=values["目标兑换积分："],
                target_rank_score=values["目标排名积分："],
            )

        item_type = "探查符" if selected_activity == "兽渊探秘" else "四倍"
        output_info1 = f"达到目标兑换积分需要的{item_type}数量: {activity_info['target_score_need_core_item_num']}"
        output_info2 = f"在达到目标兑换积分后的排名积分: {activity_info['current_rank_score_after_buy_core_item']}"
        output_info3 = f"达到目标排名积分需要的{item_type}数量: {activity_info['target_rank_score_need_core_item_num']}"
        output_info4 = f"在达到目标排名积分后的兑换积分: {activity_info['current_score_after_buy_core_item']}"

        label_1 = tk.Label(popup, text=output_info1, font=("Arial", 12), fg="red")
        label_1.grid(sticky="w", padx=5)

        label_2 = tk.Label(popup, text=output_info2, font=("Arial", 12))
        label_2.grid(sticky="w", padx=5)

        label_3 = tk.Label(popup, text=output_info3, font=("Arial", 12), fg="red")
        label_3.grid(sticky="w", padx=5)

        label_4 = tk.Label(popup, text=output_info4, font=("Arial", 12))
        label_4.grid(sticky="w", padx=5)

if __name__ == "__main__":
    root = tk.Tk()
    root.iconbitmap('icon.ico')
    MainApp(root)
    root.mainloop()
