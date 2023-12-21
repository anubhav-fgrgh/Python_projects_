import tkinter as tk
import json

def search():
    # Function to perform search based on input
    user_input_eword = entry.get()

    # You can perform your search logic here
    with open('word_mapping.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    found_hword = None
    for entry_data in data:
        if entry_data.get("eword") == user_input_eword:
            found_hword = entry_data.get("hword")
            break

    # Update the output label with the search result
    if found_hword is not None:
        output_var.set(f"Equivalent Hindi word: {found_hword}")
    else:
        output_var.set("Word not found in the mapping")

# Create the main window
root = tk.Tk()
root.title("Word Search App")

# Create and place widgets
entry_label = tk.Label(root, text="Enter English Word:")
entry_label.pack(pady=10)

entry = tk.Entry(root, width=30)
entry.pack(pady=10)

search_button = tk.Button(root, text="Search", command=search)
search_button.pack(pady=10)

# Use a StringVar to dynamically update the label text
output_var = tk.StringVar()
output_label = tk.Label(root, textvariable=output_var)
output_label.pack(pady=10)

# Run the main loop
root.mainloop()
