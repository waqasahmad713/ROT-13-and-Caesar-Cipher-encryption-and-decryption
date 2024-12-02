import tkinter as tk
from tkinter import messagebox

# Function to perform ROT-13 encryption/decryption
def rot13(text):
    result = []
    for char in text:
        if 'a' <= char <= 'z':  # Lowercase letters
            result.append(chr((ord(char) - ord('a') + 13) % 26 + ord('a')))
        elif 'A' <= char <= 'Z':  # Uppercase letters
            result.append(chr((ord(char) - ord('A') + 13) % 26 + ord('A')))
        else:
            result.append(char)  # Non-alphabetic characters remain unchanged
    return ''.join(result)

# Function to perform Caesar Cipher encryption/decryption
def caesar_cipher(text, shift, mode):
    result = []
    for char in text:
        if 'a' <= char <= 'z':  # For lowercase letters
            shift_char = chr((ord(char) - ord('a') + (shift if mode == 'encrypt' else -shift)) % 26 + ord('a'))
            result.append(shift_char)
        elif 'A' <= char <= 'Z':  # For uppercase letters
            shift_char = chr((ord(char) - ord('A') + (shift if mode == 'encrypt' else -shift)) % 26 + ord('A'))
            result.append(shift_char)
        else:
            result.append(char)  # Non-alphabetic characters remain unchanged
    return ''.join(result)

# Function to process ROT-13 encryption or decryption
def process_rot13(mode):
    message = input_text.get("1.0", tk.END).strip()  # Get text from the input box
    if not message:
        messagebox.showwarning("Input Error", "Please enter a message!")
        return
    result = rot13(message)  # ROT-13 is the same for both encryption and decryption
    output_text.delete("1.0", tk.END)  # Clear the output box
    output_text.insert(tk.END, result)

# Function to process Caesar Cipher encryption or decryption
def process_caesar(mode):
    message = input_text.get("1.0", tk.END).strip()  # Get text from the input box
    if not message:
        messagebox.showwarning("Input Error", "Please enter a message!")
        return

    shift = shift_value.get()  # Get shift value for Caesar Cipher
    if not shift.isdigit():
        messagebox.showwarning("Input Error", "Please enter a valid number for shift!")
        return
    shift = int(shift)
    result = caesar_cipher(message, shift, mode)
    output_text.delete("1.0", tk.END)  # Clear the output box
    output_text.insert(tk.END, result)

# Create the main application window
root = tk.Tk()
root.title("Colorful Cipher Tool")
root.geometry("500x500")
root.config(bg="#f0f8ff")  # Set a light background color

# Add input label and text box
input_label = tk.Label(root, text="Enter your message:", bg="#f0f8ff", fg="green", font=("Arial", 12, "bold"))
input_label.pack(pady=5)

input_text = tk.Text(root, height=5, width=40, bg="#e0f7fa", fg="black", font=("Arial", 12), bd=3, relief="solid")
input_text.pack(pady=5)

# Add shift value input for Caesar Cipher
shift_label = tk.Label(root, text="Enter shift value (e.g., 3):", bg="#f0f8ff", fg="green", font=("Arial", 12, "bold"))
shift_label.pack(pady=5)

shift_value = tk.Entry(root, width=5, font=("Arial", 12), bg="#ffffff", bd=3, relief="solid")
shift_value.pack(pady=5)

# Add mode selection for Caesar Cipher (Encrypt or Decrypt)
mode_label = tk.Label(root, text="Select mode (Encrypt/Decrypt):", bg="#f0f8ff", fg="green", font=("Arial", 12, "bold"))
mode_label.pack(pady=5)

mode_option = tk.StringVar()
mode_option.set("encrypt")  # Default mode
mode_menu = tk.OptionMenu(root, mode_option, "encrypt", "decrypt")
mode_menu.config(bg="#add8e6", font=("Arial", 12))
mode_menu.pack(pady=5)

# Add buttons for ROT-13 and Caesar Cipher
rot13_button = tk.Button(root, text="Process ROT-13", command=lambda: process_rot13(mode_option.get()), bg="#87cefa", font=("Arial", 12, "bold"))
rot13_button.pack(pady=10)

caesar_button = tk.Button(root, text="Process Caesar Cipher", command=lambda: process_caesar(mode_option.get()), bg="#87cefa", font=("Arial", 12, "bold"))
caesar_button.pack(pady=10)

# Add output label and text box
output_label = tk.Label(root, text="Output:", bg="#f0f8ff", fg="blue", font=("Arial", 12, "bold"))
output_label.pack(pady=5)

output_text = tk.Text(root, height=5, width=40, bg="#fff8dc", fg="black", font=("Arial", 12), bd=3, relief="solid")
output_text.pack(pady=5)

# Run the application
root.mainloop()
