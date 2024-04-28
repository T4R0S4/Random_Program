import tkinter as tk
from tkinter import messagebox
from autocorrect import Speller
import re

spell = Speller()

def correct_format():
    text = text_entry.get("1.0", "end-1c")
    corrected_text = re.sub(r'\b(?!(?:I|IS|IN)\b)[A-Z]\w*', lambda x: x.group().lower(), text)
    output_entry.delete("1.0", "end")
    output_entry.insert("1.0", corrected_text)

# Create the main window
root = tk.Tk()
root.title("Text Format Corrector")

# Create input label and text box
input_label = tk.Label(root, text="Enter text to correct format and typos:")
input_label.pack()
text_entry = tk.Text(root, height=5, width=50)
text_entry.pack()

# Create output label and text box
output_label = tk.Label(root, text="Corrected text:")
output_label.pack()
output_entry = tk.Text(root, height=5, width=50)
output_entry.pack()

# Create button to correct format
correct_button = tk.Button(root, text="Correct Format", command=correct_format)
correct_button.pack()

# Start the GUI event loop
root.mainloop()
