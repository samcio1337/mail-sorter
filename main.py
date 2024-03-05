import os
import tkinter as tk
from tkinter import filedialog

def sort_emails(emails):
    email_dict = {
        "onet": [],
        "interia": [],
        "wp": [],
        "o2": []
    }

    for line in emails:
        if ":" in line:
            email, password = line.strip().split(':', 1)
            email_lower = email.lower()
            if email_lower.endswith(("@op.pl", "@onet.pl", "@poczta.onet.pl", "@vp.pl", "@onet.eu", "@autograf.pl", "@buziaczek.pl", "@spoko.pl", "@poczta.onet.eu", "@onet.com.pl", "@amorki.pl", "@opoczta.pl")):
                email_dict["onet"].append(line.strip().split(' ', 1)[0])
            elif email_lower.endswith(("@interia.pl", "@poczta.fm", "@interia.eu", "@interia.com", "@intmail.pl", "@adresik.net", "@interiowy.pl", "@pisz.to", "@vip.interia.pl", "@pacz.to", "@ogarnij.se")):
                email_dict["interia"].append(line.strip().split(' ', 1)[0])
            elif email_lower.endswith("@wp.pl"):
                email_dict["wp"].append(line.strip().split(' ', 1)[0])
            elif email_lower.endswith("@o2.pl"):
                email_dict["o2"].append(line.strip().split(' ', 1)[0])

    if not os.path.exists("results"):
        os.makedirs("results")

    for email_type, email_list in email_dict.items():
        if email_list:
            output_filename = f"results/{email_type}_{len(email_list)}.txt"
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
            sort_emails(emails)

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    print("Wciśnij dowolny przycisk aby wybrać comboliste do posortowania...")
    root.bind("<Key>", lambda event: get_file())
    root.mainloop()
