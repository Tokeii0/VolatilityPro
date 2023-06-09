import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from volpro import main
import subprocess

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    from tkinter import ttk

    def create_widgets(self):
        # 输入框，用于输入映像文件路径
        self.image_path_label = tk.Label(self, text="目标目录")
        self.image_path_label.pack(side="left")
        self.image_path_entry = tk.Entry(self)
        self.image_path_entry.pack(side="left")

        # 选择文件按钮
        self.file_browse_button = tk.Button(self)
        self.file_browse_button["text"] = "浏览"
        self.file_browse_button["command"] = self.open_file_dialog
        self.file_browse_button.pack(side="left")

        

        # 下拉选择框，用于选择profile
        self.profile_label = tk.Label(self, text="Profile")
        self.profile_label.pack()
        self.profile_var = tk.StringVar(self)
        #self.profile_var.set("Win7SP1x86")
        #逐行读取profilelist.cfg文件，将profile列表写入profile_choices
        with open("profilelist.cfg", 'r', encoding='utf-8') as f:
            self.profile_choices = [line.strip() for line in f.readlines()]
        #self.profile_choices = ["Win7SP1x64", "Win7SP1x86", "Win10x64", "Win10x86"]
        self.profile_dropdown = ttk.Combobox(self, textvariable=self.profile_var, values=self.profile_choices, state="readonly")
        self.profile_dropdown.pack()

        # 输入框，用于输入dumpfiles 内存地址
        self.profile_label = tk.Label(self, text="dumpfiles")
        self.profile_label.pack()
        self.profile_entry = tk.Entry(self)
        self.profile_entry.pack()
        
        # 确认按钮
        self.confirm_button = tk.Button(self)
        self.confirm_button["text"] = "执行"
        self.confirm_button["command"] = self.confirm
        self.confirm_button.pack(side="bottom", anchor="center")


    def open_file_dialog(self):
        # 打开文件选择对话框
        filepath = filedialog.askopenfilename()
        # 将文件路径写入输入框
        self.image_path_entry.delete(0, tk.END)
        self.image_path_entry.insert(0, filepath)

    def confirm(self):
        # 这里应该是处理输入路径并执行相应功能的地方
        # 你可以在这里调用volpro.py中的函数
        # 例如：
        #执行命令 python volpro.py [imagename] (profile) (dumpfiles)

        command = "python volpro.py " + self.image_path_entry.get() + " " + self.profile_entry.get() + " " + self.profile_var.get()
        # 执行命令,新开cmd窗口
        subprocess.Popen(command, shell=True)





root = tk.Tk()
app = Application(master=root)
app.mainloop()
