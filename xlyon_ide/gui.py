import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox
import os
from .compiler import run_xlyon_code, run_folder

class XlyonIDE(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Xlyon IDE")
        self.geometry("800x600")
        self.filename = None

        # Editor
        self.editor = scrolledtext.ScrolledText(self, wrap=tk.WORD, font=("Consolas", 12))
        self.editor.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Output
        self.output = scrolledtext.ScrolledText(self, wrap=tk.WORD, font=("Consolas", 12), height=10, bg="#f0f0f0")
        self.output.pack(fill=tk.BOTH, expand=False, padx=5, pady=5)
        self.output.config(state=tk.DISABLED)

        # Menu
        menubar = tk.Menu(self)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=self.new_file)
        filemenu.add_command(label="Open...", command=self.open_file)
        filemenu.add_command(label="Save", command=self.save_file)
        filemenu.add_command(label="Save As...", command=self.save_as)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.quit)
        menubar.add_cascade(label="File", menu=filemenu)

        runmenu = tk.Menu(menubar, tearoff=0)
        runmenu.add_command(label="Run Current Code", command=self.run_code)
        runmenu.add_command(label="Run All .xly Files in Folder...", command=self.run_folder)
        menubar.add_cascade(label="Run", menu=runmenu)

        self.config(menu=menubar)
        self.protocol("WM_DELETE_WINDOW", self.quit)

        # Start with Hello World
        self.editor.insert(tk.END, "print('Hello, Xlyon!')")

    def new_file(self):
        self.filename = None
        self.editor.delete(1.0, tk.END)
        self.output_clear()

    def open_file(self):
        fname = filedialog.askopenfilename(defaultextension=".xly", filetypes=[("Xlyon Files", "*.xly"), ("All Files", "*.*")])
        if fname:
            with open(fname, "r") as f:
                self.editor.delete(1.0, tk.END)
                self.editor.insert(tk.END, f.read())
            self.filename = fname
            self.output_clear()

    def save_file(self):
        if self.filename:
            with open(self.filename, "w") as f:
                f.write(self.editor.get(1.0, tk.END))
        else:
            self.save_as()

    def save_as(self):
        fname = filedialog.asksaveasfilename(defaultextension=".xly", filetypes=[("Xlyon Files", "*.xly"), ("All Files", "*.*")])
        if fname:
            with open(fname, "w") as f:
                f.write(self.editor.get(1.0, tk.END))
            self.filename = fname

    def run_code(self):
        code = self.editor.get(1.0, tk.END)
        self.output_clear()
        run_xlyon_code(code, output_callback=self.output_append)

    def run_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.output_clear()
            run_folder(folder, output_callback=self.output_append)

    def output_append(self, text):
        self.output.config(state=tk.NORMAL)
        self.output.insert(tk.END, text + '\n')
        self.output.see(tk.END)
        self.output.config(state=tk.DISABLED)

    def output_clear(self):
        self.output.config(state=tk.NORMAL)
        self.output.delete(1.0, tk.END)
        self.output.config(state=tk.DISABLED)

    def quit(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.destroy()

