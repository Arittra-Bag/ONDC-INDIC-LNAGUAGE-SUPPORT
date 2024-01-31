import tkinter as tk
from googletrans import Translator
from tkinter import simpledialog

def get_hindi_input():
    hindi_text = simpledialog.askstring("Input", "Type in Hindi:")
    if hindi_text:
        entry.delete(0, tk.END)
        entry.insert(0, hindi_text)

def translate_text():
    hindi_text = entry.get()
    english_translation = translator.translate(hindi_text, dest='en').text
    output_label.config(text=f"Translation (to English): {english_translation}")

def insert_hindi_char(char):
    entry.insert(tk.END, char)

# Create the main window
root = tk.Tk()
root.title("Hindi to English Translator")

# Create and pack widgets
label = tk.Label(root, text="Enter Hindi Text:")
label.pack(pady=10)

entry = tk.Entry(root, width=30)
entry.pack(pady=10)

hindi_input_button = tk.Button(root, text="Type in Hindi", command=get_hindi_input)
hindi_input_button.pack(pady=10)

translate_button = tk.Button(root, text="Translate", command=translate_text)
translate_button.pack(pady=10)

output_label = tk.Label(root, text="")
output_label.pack(pady=10)

# Create Translator object
translator = Translator()

# Create Hindi keyboard buttons
def create_hindi_keyboard():
    hindi_keyboard_window = tk.Toplevel(root)
    hindi_keyboard_window.title("Hindi Keyboard")

    hindi_chars = "अआइईउऊऋएऐओऔकखगघङचछजझञटठडढणतथदधनपफबभमयरलवशषसह ा ि ी ु ू ृ ॄ े ै ो ौ"
    for char in hindi_chars:
        hindi_button = tk.Button(hindi_keyboard_window, text=char, command=lambda c=char: insert_hindi_char(c))
        hindi_button.pack(side=tk.LEFT, padx=5)

hindi_keyboard_button = tk.Button(root, text="Show Hindi Keyboard", command=create_hindi_keyboard)
hindi_keyboard_button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
