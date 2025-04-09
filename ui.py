import tkinter as tk
from tkinter import ttk, messagebox

class MapApp:
    def __init__(self, master, graph, labels, path_callback):
        self.graph = graph
        self.labels = labels
        self.path_callback = path_callback

        self.start_var = tk.StringVar()
        self.end_var = tk.StringVar()

        tk.Label(master, text="Chọn điểm đầu:").pack()
        self.start_menu = ttk.Combobox(master, textvariable=self.start_var, values=list(labels.values()))
        self.start_menu.pack()

        tk.Label(master, text="Chọn điểm cuối:").pack()
        self.end_menu = ttk.Combobox(master, textvariable=self.end_var, values=list(labels.values()))
        self.end_menu.pack()

        tk.Button(master, text="Tìm đường", command=self.find_path).pack()

    def find_path(self):
        start_label = self.start_var.get()
        end_label = self.end_var.get()

        label_to_id = {label: node for node, label in self.labels.items()}
        if start_label in label_to_id and end_label in label_to_id:
            path = self.path_callback(label_to_id[start_label], label_to_id[end_label])
            if path:
                messagebox.showinfo("Kết quả", f"Đường đi: {' -> '.join(path)}")
            else:
                messagebox.showwarning("Lỗi", "Không tìm được đường đi.")
        else:
            messagebox.showerror("Lỗi", "Điểm không hợp lệ.")