import tkinter as tk
import os
import random

class TipApp:
    def __init__(self):
        self.single_window = None
        self.batch_windows = []
        self.tips = [
            "黛利拉小姐，今夜的夜色很美，能允许我与你跳一支舞吗？",
            "我和小黛是意定之人，你只会拥有更多的爱。",
            "小黛，你怎么看着那么难过呢?重逢的时候，我们都应该是最好的样子。",
            "我可以藏在你的影子里，住在你的眼眸中，你接触世间万物时，我与你如影随形，你的喜怒哀乐，我都会感同身受。",
            "现在，月色有了，我最爱的女孩也在，可是，怎么办，小黛和你在一起的时候，我总是贪得无厌。",
            "传说在布雷诺春信来临之际，看到金色流星雨的人，将得到永不失去的爱情。所以，如果天空不给我们下一场流星雨，我便，自己下一场。。",
            "你若活着，我是你的江声浩荡，若你离去，我是你的死水微澜。"                                                                                                                                                                                                                                                                                                                                          
        ]                                                                                                                                                                                                                                                                                                                                                          ·
        self.bg_colors = [
            'lightpink', 'skyblue', 'lightgreen', 'lavender'
        ]
        self.count = 200

    def show_single_tip(self):
        self.single_window = tk.Tk()
        self.single_window.title("专属提示")
        # 窗口居中
        screen_w = self.single_window.winfo_screenwidth()
        screen_h = self.single_window.winfo_screenheight()
        win_w = 600
        win_h = 180
        pos_x = (screen_w - win_w) // 2
        pos_y = (screen_h - win_h) // 2
        self.single_window.geometry(f"{win_w}x{win_h}+{pos_x}+{pos_y}")
        # 内容填充
        tip = "黛利拉小姐，今夜的夜色很美，能允许我与你跳一支舞吗？"
        bg = random.choice(self.bg_colors)
        # 标签
        tip_label = tk.Label(
            self.single_window,
            text=tip,
            font=("微软雅黑", 14),
            bg=bg,
            width=60,
            height=5,
            wraplength=win_w - 40,
            justify='center'
        )
        tip_label.pack(padx=20, pady=20)
        # 绑定按键（空格，确保绑定到窗口）
        self.single_window.bind("<space>", self.on_space_global)
        self.single_window.attributes('-topmost', True)
        self.single_window.protocol("WM_DELETE_WINDOW", self.start_batch_tips)
        self.single_window.mainloop()

    def start_batch_tips(self):
        if self.single_window:
            self.single_window.destroy()
        self.single_window = None
        self.create_batch_window(self.count)

    def create_batch_window(self, count):
        if count <= 0:
            return
        window = tk.Toplevel()
        self.batch_windows.append(window)
        # 窗口位置
        screen_w = window.winfo_screenwidth()
        screen_h = window.winfo_screenheight()
        pos_x = random.randrange(0, screen_w - 200)
        pos_y = random.randrange(0, screen_h - 100)
        window.geometry(f"250x150+{pos_x}+{pos_y}")
        # 随机内容
        tip = random.choice(self.tips)
        bg = random.choice(self.bg_colors)
        # 标签
        tk.Label(
            window,
            text=tip,
            font=("微软雅黑", 11),
            bg=bg,
            wraplength=180,
            justify='center'
        ).pack(padx=20, pady=20)
        # 窗口绑定按键（空格）
        window.bind("<space>", self.on_space_global)
        window.attributes('-topmost', True)
        window.after(80, self.create_batch_window, count - 1)

    def on_space_global(self, event=None):
        # 按空格将强制关闭所有窗口并退出
        if self.single_window:
            self.single_window.destroy()
        for window in self.batch_windows:
            window.destroy()
        os._exit(0)

if __name__ == "__main__":
    app = TipApp()
    app.show_single_tip()
