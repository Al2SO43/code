# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import os
import platform

class HostsEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Hosts文件编辑器---version=0.12---Powered by Al2(SO4)3")

        self.system = platform.system()
        self.hosts_path = self.get_hosts_path()
        self.hosts_content = self.read_hosts_file()

        self.create_ui()

    def get_hosts_path(self):
        if self.system == 'Windows':
            return r"C:\Windows\System32\drivers\etc\hosts"
        elif self.system == 'Linux' or self.system == 'Darwin':  # Darwin = macOS
            return "/etc/hosts"
        else:
            raise OSError("Unsupported operating system:不受支持的操作系统")

    def read_hosts_file(self):
        with open(self.hosts_path, 'r') as file:
            return file.read()

    def write_hosts_file(self, content):
        with open(self.hosts_path, 'w') as file:
            file.write(content)

    def create_ui(self):
        # 左右布局
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # 左边编辑
        self.edit_frame = tk.Frame(self.main_frame)
        self.edit_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.edit_text = tk.Text(self.edit_frame, wrap=tk.NONE)
        self.edit_text.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.edit_text.insert(tk.END, self.hosts_content)

        self.scrollbar_y = tk.Scrollbar(self.edit_frame, command=self.edit_text.yview)
        self.scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
        self.edit_text.config(yscrollcommand=self.scrollbar_y.set)

        self.scrollbar_x = tk.Scrollbar(self.edit_frame, orient=tk.HORIZONTAL, command=self.edit_text.xview)
        self.scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)
        self.edit_text.config(xscrollcommand=self.scrollbar_x.set)

        # 右边显示
        self.display_frame = tk.Frame(self.main_frame)
        self.display_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.tree = ttk.Treeview(self.display_frame, columns=("IP", "域名"), show="headings")
        self.tree.heading("IP", text="IP地址")
        self.tree.heading("域名", text="对应域名")
        self.tree.column("IP", anchor=tk.CENTER)
        self.tree.column("域名", anchor=tk.CENTER)
        self.tree.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.populate_display_tree()

        self.scrollbar_y_display = tk.Scrollbar(self.display_frame, command=self.tree.yview)
        self.scrollbar_y_display.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree.config(yscrollcommand=self.scrollbar_y_display.set)

        self.scrollbar_x_display = tk.Scrollbar(self.display_frame, orient=tk.HORIZONTAL, command=self.tree.xview)
        self.scrollbar_x_display.pack(side=tk.BOTTOM, fill=tk.X)
        self.tree.config(xscrollcommand=self.scrollbar_x_display.set)

        # 新建 刷新 删除
        self.button_frame = tk.Frame(self.display_frame)
        self.button_frame.pack(side=tk.BOTTOM)

        self.add_button = tk.Button(self.button_frame, text="新建条目", command=self.add_entry)
        self.add_button.pack(side=tk.LEFT)

        self.refresh_button = tk.Button(self.button_frame, text="刷新显示栏", command=self.refresh_display_tree)
        self.refresh_button.pack(side=tk.LEFT)

        self.delete_button = tk.Button(self.button_frame, text="删除选中条目", command=self.delete_entry)
        self.delete_button.pack(side=tk.LEFT)

        # 保存
        self.save_button = tk.Button(self.root, text="保存此次更改(这会将当前的所有内容写入Hosts文件!)", command=self.save_changes)
        self.save_button.pack(side=tk.BOTTOM)

    def populate_display_tree(self):
        for line in self.hosts_content.splitlines():
            if line.strip() and not line.startswith('#'):
                parts = line.split()
                if len(parts) >= 2:
                    ip = parts[0]
                    domain = parts[1]
                    self.tree.insert("", tk.END, values=(ip, domain))

    def refresh_display_tree(self):
        self.tree.delete(*self.tree.get_children())
        self.populate_display_tree()

    def add_entry(self):
        add_window = tk.Toplevel(self.root)
        add_window.title("新建条目")

        tk.Label(add_window, text="IP地址:").grid(row=0, column=0)
        ip_entry = tk.Entry(add_window)
        ip_entry.grid(row=0, column=1)

        tk.Label(add_window, text="对应域名:").grid(row=1, column=0)
        domain_entry = tk.Entry(add_window)
        domain_entry.grid(row=1, column=1)

        def add():
            ip = ip_entry.get()
            domain = domain_entry.get()
            if ip and domain:
                self.edit_text.insert(tk.END, f"\n{ip} {domain}")
                self.hosts_content += f"\n{ip} {domain}"
                self.tree.insert("", tk.END, values=(ip, domain))
                add_window.destroy()
            else:
                messagebox.showwarning("错误", "IP地址和对应域名不能为空")

        tk.Button(add_window, text="添加条目", command=add).grid(row=2, column=0, columnspan=2)

    def delete_entry(self):
        selected_item = self.tree.selection()
        if selected_item:
            item = self.tree.item(selected_item)
            ip = item['values'][0]
            confirm = messagebox.askyesno("删除选中条目", f"确定要删除条目: IP {item['values'][0]} 域名 {item['values'][1]} 吗？")
            if confirm:
                self.hosts_content = "\n".join([line for line in self.hosts_content.splitlines() if ip not in line])
                self.edit_text.delete(1.0, tk.END)
                self.edit_text.insert(tk.END, self.hosts_content)
                self.tree.delete(selected_item)

    def save_changes(self):
        self.hosts_content = self.edit_text.get(1.0, tk.END)
        self.write_hosts_file(self.hosts_content)
        messagebox.showinfo("保存此次更改", "保存成功,已经将当前的所有内容写入到Hosts文件!")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1000x600") 
    app = HostsEditor(root)
    root.mainloop()
