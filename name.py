import tkinter as tk
from tkinter import ttk
from webbrowser import open_new

def do_search(site, first_name, last_name):
    if site == 'TruePeople':
        url = f'https://www.truepeoplesearch.com/results?name={first_name}%20{last_name}'
    elif site == 'FastPeople':
        url = f'https://www.fastpeoplesearch.com/name/{first_name}-{last_name}'
    # Add more elif conditions for other sites
    open_new(url)

def main():
    root = tk.Tk()
    root.title("IntelTechniques Name Tool")
    
    # Create the sidebar
    sidebar = tk.Frame(root, width=200, bg='#f1f1f1')
    sidebar.pack(side=tk.LEFT, fill=tk.BOTH)
    
    menu_items = ["Offline Tools", "Online Tools", "Search Engines", "Facebook"] # Add more as needed
    for item in menu_items:
        ttk.Button(sidebar, text=item).pack(fill=tk.X)
    
    # Create the main content area
    content = tk.Frame(root, width=800)
    content.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
    
    tk.Label(content, text="First Name").grid(row=0, column=0)
    tk.Label(content, text="Last Name").grid(row=0, column=1)
    
    first_name_entry = tk.Entry(content)
    last_name_entry = tk.Entry(content)
    
    first_name_entry.grid(row=1, column=0)
    last_name_entry.grid(row=1, column=1)
    
    ttk.Button(content, text="TruePeople", command=lambda: do_search("TruePeople", first_name_entry.get(), last_name_entry.get())).grid(row=1, column=2)
    ttk.Button(content, text="FastPeople", command=lambda: do_search("FastPeople", first_name_entry.get(), last_name_entry.get())).grid(row=2, column=2)
    # Add more buttons as needed
    
    root.mainloop()

if __name__ == "__main__":
    main()

