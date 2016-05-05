#!/usr/bin/python

import tkinter as tk
from hegelizer.model.notion import Notion


class MainWindow(tk.Frame):
    counter = 0

    def __init__(self, *args, **kwargs):
        self.notions = []
        tk.Frame.__init__(self, *args, **kwargs)
        self.button = tk.Button(self, text="Create new notion",
                                command=self.create_notion)
        self.button.pack(side="top")

    def create_notion(self):
        self.counter += 1
        t = tk.Toplevel(self)
        t.wm_title("New Notion")

        lbl_name = tk.Label(t, text="Name:").grid(row=0, column=0)
        self.tb_name = tk.Entry(t).grid(row=0, column=1)
        lbl_type = tk.Label(t, text="Hegelian Type:").grid(row=1, column=0)
        self.tb_type = tk.Entry(t).grid(row=1, column=1)
        lbl_other = tk.Label(t, text="Other names:").grid(row=2, column=0)
        self.tb_other = tk.Entry(t).grid(row=2, column=1)
        lbl_notes = tk.Label(t, text="Notes:").grid(row=3, column=0)
        self.txt_notes = tk.Text(t).grid(row=3, column=1)

        btn_save = tk.Button(t, text="Save",
                             command=lambda: self.save_notion(t)
                             ).grid(row=4, column=1)


    def save_notion(self, t):
        self.notions.append(
            Notion(
                self.tb_name.get(),
                self.tb_type.get(),
                [self.tb_other.get()],
                self.txt_notes.get()
            )
        )

if __name__ == "__main__":
    root = tk.Tk()
    main = MainWindow(root)
    main.pack(side="top", fill="both", expand=True)
    root.mainloop()
