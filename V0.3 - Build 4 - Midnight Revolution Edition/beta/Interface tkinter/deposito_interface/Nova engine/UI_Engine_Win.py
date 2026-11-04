import tkinter as tk


class Window(tk.Tk):
    """Camada simples do Horizon sobre o Tkinter."""

    def __init__(self, title="Sem nome", size="1000x600", bg="#1e1e1e"):
        super().__init__()
        self.title(title)
        self.geometry(size)
        self.configure(bg=bg)

    def frame(self, parent=None, **options):
        return tk.Frame(parent or self, **options)

    def button(self, parent, **options):
        return tk.Button(parent, **options)

    def label(self, parent=None, **options):
        return tk.Label(parent or self, **options)

    def text(self, parent, **options):
        return tk.Text(parent, **options)

    def paned_window(self, parent=None, **options):
        return tk.PanedWindow(parent or self, **options)

    def run(self):
        self.mainloop()
