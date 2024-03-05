import tkinter as tk
from tkinter import filedialog

def sort_emails(emails):
    onet_emails = []
    interia_emails = []
    wp_emails = []
    o2_emails = []

    for line in emails:
        if ":" in line:
            email, password = line.strip().split(':', 1)
            email_lower = email.lower()
            if email_lower.endswith(("@op.pl", "@onet.pl", "@poczta.onet.pl", "@vp.pl", "@onet.eu", "@autograf.pl", "@buziaczek.pl", "@spoko.pl", "@poczta.onet.eu", "@onet.com.pl", "@amorki.pl", "@opoczta.pl")):
                onet_emails.append(line.strip())
            elif email_lower.endswith(("@interia.pl", "@poczta.fm", "@interia.eu", "@interia.com", "@intmail.pl", "@adresik.net", "@interiowy.pl", "@pisz.to", "@vip.interia.pl", "@pacz.to", "@ogarnij.se")):
                interia_emails.append(line.strip())
            elif email_lower.endswith("@wp.pl"):
                wp_emails.append(line.strip())
            elif email_lower.endswith("@o2.pl"):
                o2_emails.append(line.strip())

    if onet_emails:
        output_filename = f"onet_{len(onet_emails)}.txt"
        with open(output_filename, 'w') as output_file:
            output_file.write('\n'.join(onet_emails))

    if interia_emails:
        output_filename = f"interia_{len(interia_emails)}.txt"
        with open(output_filename, 'w') as output_file:
            output_file.write('\n'.join(interia_emails))

    if wp_emails:
        output_filename = f"wp_{len(wp_emails)}.txt"
        with open(output_filename, 'w') as output_file:
            output_file.write('\n'.join(wp_emails))
    
    if o2_emails:
        output_filename = f"o2_{len(o2_emails)}.txt"
        with open(output_filename, 'w') as output_file:
            output_file.write('\n'.join(o2_emails))

    root.destroy() 

def get_file():
    root.withdraw()
    top = tk.Toplevel() 
    top.withdraw()
    filename = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=[("Text files", "*.txt")])
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
