import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from googletrans import Translator, LANGUAGES

# Initialize translator
translator = Translator()

# Reverse LANGUAGES dict to get full name to code
LANGUAGE_NAME_TO_CODE = {v.title(): k for k, v in LANGUAGES.items()}
LANGUAGE_LIST = sorted(LANGUAGE_NAME_TO_CODE.keys())

# Common travel phrases
travel_phrases = {
    "Hello": "A friendly greeting",
    "Thank you": "Show gratitude",
    "Where is the bathroom?": "Find facilities",
    "How much does this cost?": "Ask about prices",
    "Can you help me?": "Request assistance",
    "I need a doctor": "Emergency phrase",
    "Good morning": "Morning greeting",
}

# Translate function
def translate_text():
    text = input_text.get()
    lang_name = lang_var.get()

    if not text:
        messagebox.showwarning("Missing Input", "Please enter a phrase or sentence.")
        return

    if lang_name not in LANGUAGE_NAME_TO_CODE:
        messagebox.showerror("Invalid Language", "Please select a valid target language.")
        return

    lang_code = LANGUAGE_NAME_TO_CODE[lang_name]

    try:
        translated = translator.translate(text, dest=lang_code)
        output_box.config(state='normal')
        output_box.delete('1.0', tk.END)
        output_box.insert(tk.END, f"{translated.text}")
        output_box.tag_configure("center", justify='center', foreground="#00FFAB", font=("Helvetica", 13, "bold"))
        output_box.tag_add("center", "1.0", "end")
        output_box.config(state='disabled')
    except Exception as e:
        messagebox.showerror("Translation Error", str(e))

# Load phrase into input box
def load_phrase(event=None):
    selected = phrase_var.get()
    if selected:
        input_text.set(selected)

# Exit the app
def close_app():
    root.destroy()

# --- GUI SETUP ---
root = tk.Tk()
root.title("🌍 AI Travel Translator")
root.geometry("620x520")
root.configure(bg="#0D0D0D")  # Pure dark background

# Styles
style = ttk.Style()
style.theme_use("clam")

# Universal dark theme style settings
style.configure(".", background="#0D0D0D", foreground="#E5E5E5", fieldbackground="#1A1A1A", font=("Helvetica", 11))
style.configure("TButton", background="#111111", foreground="#FFFFFF", font=("Helvetica", 11, "bold"))
style.configure("TLabelFrame", background="#0D0D0D", foreground="#60A5FA")
style.configure("TLabel", background="#0D0D0D", foreground="#E5E5E5")
style.configure("TCombobox", fieldbackground="#1A1A1A", background="#1A1A1A", foreground="#E5E5E5")

# Title
title_label = ttk.Label(root, text="🌍 AI Language Translator for Travelers", font=("Helvetica", 17, "bold"), foreground="#00FFFF", background="#0D0D0D")
title_label.pack(pady=15)

# Phrase dropdown
phrase_frame = ttk.LabelFrame(root, text="Common Travel Phrases", padding=(10, 10))
phrase_frame.pack(padx=20, pady=10, fill="x")
phrase_var = tk.StringVar()
phrase_menu = ttk.Combobox(phrase_frame, textvariable=phrase_var, values=list(travel_phrases.keys()), state="readonly", width=45)
phrase_menu.pack()
phrase_menu.bind("<<ComboboxSelected>>", load_phrase)

# Custom input
input_frame = ttk.LabelFrame(root, text="Enter your sentence", padding=(10, 10))
input_frame.pack(padx=20, pady=10, fill="x")
input_text = tk.StringVar()
input_entry = ttk.Entry(input_frame, textvariable=input_text, font=("Helvetica", 12), width=55)
input_entry.pack()

# Language dropdown
lang_frame = ttk.LabelFrame(root, text="Select Target Language", padding=(10, 10))
lang_frame.pack(padx=20, pady=10, fill="x")
lang_var = tk.StringVar()
lang_menu = ttk.Combobox(lang_frame, textvariable=lang_var, values=LANGUAGE_LIST, state="readonly", width=45)
lang_menu.pack()

# Translate button
translate_btn = ttk.Button(root, text="Translate", command=translate_text)
translate_btn.pack(pady=15)

# Output
output_label = ttk.Label(root, text="Translation:", font=("Helvetica", 12, "bold"), foreground="#00FFAB", background="#0D0D0D")
output_label.pack()

output_box = scrolledtext.ScrolledText(
    root,
    height=6,
    font=("Helvetica", 12),
    wrap=tk.WORD,
    state='disabled',
    bg="#1A1A1A",
    fg="#00FFAB",
    relief="groove",
    borderwidth=3
)
output_box.pack(padx=20, pady=8, fill="both", expand=False)

# Exit button
exit_btn = ttk.Button(root, text="Exit", command=close_app)
exit_btn.pack(pady=10)

# Footer
footer = ttk.Label(root, text="Tip: You can type your own sentence or select a common phrase.", font=("Helvetica", 9), foreground="#888888", background="#0D0D0D")
footer.pack(pady=5)

# Run app
root.mainloop()
