import os
import tkinter as tk
from tkinter import filedialog
import json

def load_config(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def sort_emails(emails, config):
    email_dict = {filename: [] for filename in config}

    for line in emails:
        if ":" in line:
            email, password = line.strip().split(':', 1)
            email_lower = email.lower()
            for filename, domains in config.items():
                if any(email_lower.endswith(domain) for domain in domains):
                    email_dict[filename].append(line.strip().split(' ', 1)[0])

    if not os.path.exists("results"):
        os.makedirs("results")

    for filename, email_list in email_dict.items():
        if email_list:
            output_filename = f"results/{filename}_{len(email_list)}.txt"
            emails_to_write = '\n'.join(email_list)
            with open(output_filename, 'w') as output_file:
                output_file.write(emails_to_write)

    root.destroy()

def get_file():
    root.withdraw()
    top = tk.Toplevel()
    top.withdraw()
    filename = filedialog.askopenfilename(initialdir="/", title="Wybor pliku", filetypes=[("Text files", "*.txt")])
    if filename:
        with open(filename, 'r') as file:
            emails = file.readlines()
            sort_emails(emails, config)

if __name__ == "__main__":
    config = load_config("config.json")

    root = tk.Tk()
    root.withdraw()
    print("Wciśnij dowolny przycisk aby wybrać comboliste do posortowania...")
    root.bind("<Key>", lambda event: get_file())
    root.mainloop()
