import tkinter as tk
from start import launch

if __name__ == "__main__":

    root = tk.Tk()
    root.title('GitHub User Information')
    root.geometry('400x200')

    username_label = tk.Label(root, text='GitHub Username:')
    username_label.pack(pady=10)

    username_entry = tk.Entry(root)
    username_entry.pack(pady=5)

    domain_label = tk.Label(root, text='Freshdesk Domain:')
    domain_label.pack(pady=10)

    domain_entry = tk.Entry(root)
    domain_entry.pack(pady=5)

    start_button = tk.Button(root, text='Start', command=lambda: launch(username_entry.get(), domain_entry.get()))
    start_button.pack(pady=10)

    root.mainloop()



