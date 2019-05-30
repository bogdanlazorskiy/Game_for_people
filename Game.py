import tkinter as tk


class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()

    def init_main(self):
        fone_btn = tk.Frame(bg='#d7d8e0', bd=2)
        fone_btn.pack(side=tk.TOP, fill=tk.X)
        text = tk.Text(width=200, height=25, bd=2)
        text.pack()
        btn_add = tk.Button(fone_btn, text="Add window", command=self.open_dialog, bd=0, compound=tk.TOP)
        btn_add.pack(side=tk.LEFT)

    def open_dialog(self):
        Child()




class Child(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child()

    def init_child(self):
        self.title("Add new window")
        self.geometry("400x320")
        self.resizable(False, False)
        self.grab_set()
        self.focus_set()


if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    app.pack()
    root.title("New game")
    root.geometry("900x600")
    root.resizable(False, False)
    root.mainloop()