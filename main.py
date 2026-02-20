import tkinter as tk
from tkinter import filedialog, messagebox

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Pythonic Notes")
        self.root.geometry("800x600")

        self.text_area = tk.Text(self.root, undo=True, font=("Consolas", 12))
        self.text_area.pack(fill=tk.BOTH, expand=True)

        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=self.new_file, accelerator="Ctrl+N")
        file_menu.add_command(label="Open", command=self.open_file, accelerator="Ctrl+O")
        file_menu.add_command(label="Save", command=self.save_file, accelerator="Ctrl+S")
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=root.quit)

        self.root.bind("<Control-n>", lambda e: self.new_file())
        self.root.bind("<Control-o>", lambda e: self.open_file())
        self.root.bind("<Control-s>", lambda e: self.save_file())

        self.current_file = None

    def new_file(self):
        self.text_area.delete(1.0, tk.END)
        self.root.title("New File - Pythonic Notes")
        self.current_file = None

    def open_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt",
                                                filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")])
        if file_path:
            self.text_area.delete(1.0, tk.END)
            with open(file_path, "r") as file:
                self.text_area.insert(1.0, file.read())
            self.root.title(f"{file_path} - Pythonic Notes")
            self.current_file = file_path

    def save_file(self):
        if self.current_file:
            with open(self.current_file, "w") as file:
                file.write(self.text_area.get(1.0, tk.END))
        else:
            file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                      filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")])
            if file_path:
                with open(file_path, "w") as file:
                    file.write(self.text_area.get(1.0, tk.END))
                self.current_file = file_path
                self.root.title(f"{file_path} - Pythonic Notes")

if __name__ == "__main__":
    root = tk.Tk()
    editor = TextEditor(root)
    root.mainloop()
