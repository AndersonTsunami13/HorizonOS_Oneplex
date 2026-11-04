import ast
import tkinter as tk
from tkinter import filedialog

from UI_Engine_Win import Window

class Toolbar:
    def __init__(self, window, on_new, on_open, on_save, on_check):
        self.frame = window.frame(bg="#111111", height=40)
        self.frame.pack(fill="x")

        self._add_button(window, "Novo", on_new)
        self._add_button(window, "Abrir", on_open)
        self._add_button(window, "Salvar", on_save)
        self._add_button(window, "Verificar", on_check)

    def _add_button(self, window, text, command):
        button = window.button(
            self.frame,
            text=text,
            command=command,
            bg="#222222",
            fg="white",
            relief="flat"
        )
        button.pack(side="left", padx=5, pady=5)


class CodeEditor:
    def __init__(self, window, parent):
        self.frame = window.frame(parent)
        self.text = window.text(
            self.frame,
            bg="#1e1e1e",
            fg="#00ff88",
            insertbackground="white",
            font=("Consolas", 11),
            undo=True
        )
        self.text.pack(fill="both", expand=True)

    def clear(self):
        self.text.delete("1.0", tk.END)

    def get_content(self):
        return self.text.get("1.0", tk.END)

    def set_content(self, content):
        self.clear()
        self.text.insert(tk.END, content)


class LogPanel:
    def __init__(self, window, parent):
        self.frame = window.frame(parent, bg="#111111", width=250)
        self.frame.pack_propagate(False)

        self.title = window.label(
            self.frame,
            text="Horizon AI",
            bg="#111111",
            fg="#00ff88",
            font=("Arial", 10, "bold")
        )
        self.title.pack(fill="x", pady=5)

        self.text = window.text(
            self.frame,
            bg="#111111",
            fg="white",
            font=("Consolas", 10)
        )
        self.text.pack(fill="both", expand=True)

        self.write("=== Horizon AI ===")
        self.write("Editor iniciado.")

    def write(self, message):
        self.text.config(state="normal")
        self.text.insert(tk.END, message + "\n")
        self.text.see(tk.END)
        self.text.config(state="disabled")


class StatusBar:
    def __init__(self, window):
        self.label = window.label(
            text="Horizon Editor iniciado",
            anchor="w",
            bg="#111111",
            fg="white"
        )
        self.label.pack(fill="x")

    def set(self, message):
        self.label.config(text=message)


class EditorApp:
    def __init__(self):
        self.window = Window(
            title="Horizon Editor",
            size="1000x600",
            bg="#1e1e1e"
        )

        self.current_file = None

        self.toolbar = Toolbar(
            self.window,
            self.new_file,
            self.open_file,
            self.save_file,
            self.check_code
        )

        self.content = self.window.paned_window(
            bg="#1e1e1e",
            orient=tk.HORIZONTAL,
            sashwidth=5
        )
        self.content.pack(fill="both", expand=True)

        self.editor = CodeEditor(self.window, self.content)
        self.log_panel = LogPanel(self.window, self.content)

        self.content.add(self.editor.frame, stretch="always")
        self.content.add(self.log_panel.frame)

        self.status = StatusBar(self.window)

    def new_file(self):
        self.current_file = None
        self.editor.clear()
        self.status.set("Novo arquivo")
        self.log_panel.write("Novo arquivo criado")

    def open_file(self):
        path = filedialog.askopenfilename(
            filetypes=[
                ("Python", "*.py"),
                ("Texto", "*.txt"),
                ("Todos os arquivos", "*.*")
            ]
        )

        if not path:
            return

        try:
            with open(path, "r", encoding="utf-8") as file:
                content = file.read()

            self.editor.set_content(content)
            self.current_file = path
            self.status.set(f"Aberto: {path}")
            self.log_panel.write("Arquivo aberto")

        except OSError as error:
            self.log_panel.write(f"Erro ao abrir arquivo: {error}")

    def save_file(self):
        if not self.current_file:
            self.current_file = filedialog.asksaveasfilename(
                defaultextension=".py",
                filetypes=[
                    ("Python", "*.py"),
                    ("Texto", "*.txt"),
                    ("Todos os arquivos", "*.*")
                ]
            )

            if not self.current_file:
                return

        try:
            with open(self.current_file, "w", encoding="utf-8") as file:
                file.write(self.editor.get_content())

            self.status.set(f"Salvo: {self.current_file}")
            self.log_panel.write("Arquivo salvo")

        except OSError as error:
            self.log_panel.write(f"Erro ao salvar arquivo: {error}")

    def check_code(self):
        self.log_panel.write("Verificando código...")

        try:
            ast.parse(self.editor.get_content())
            self.log_panel.write("Nenhum erro de sintaxe encontrado")
            self.status.set("Código válido")

        except SyntaxError as error:
            self.log_panel.write(
                f"Linha {error.lineno}: {error.msg}"
            )
            self.status.set("Erro de sintaxe")

        except Exception as error:
            self.log_panel.write(f"Erro: {error}")
            self.status.set("Erro ao verificar")

    def run(self):
        self.window.run()


if __name__ == "__main__":
    EditorApp().run()
