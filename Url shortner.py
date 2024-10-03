import tkinter as tk
from tkinter import messagebox
import pyshorteners

class URLShortenerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("URL Shortener")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f0f0")

        self.create_widgets()

    def create_widgets(self):
        # Header frame
        header_frame = tk.Frame(self.root, bg="#3498db", height=50)
        header_frame.pack(fill="x", padx=10, pady=10)

        tk.Label(header_frame, text="URL Shortener", font=("Arial", 24, "bold"), bg="#3498db", fg="#ffffff").pack(pady=10)

        # URL entry frame
        url_frame = tk.Frame(self.root, bg="#f0f0f0")
        url_frame.pack(fill="x", padx=20, pady=20)

        tk.Label(url_frame, text="Enter URL:", font=("Arial", 14), bg="#f0f0f0").pack(side="left", padx=10)
        self.url_entry = tk.Entry(url_frame, width=40, font=("Arial", 14), relief="flat", borderwidth=1, highlightthickness=1)
        self.url_entry.pack(side="left", fill="x", expand=True, padx=10)

        # Url Shorten button
        shorten_button = tk.Button(url_frame, text="Shorten URL", command=self.shorten_url, font=("Arial", 14), bg="#4CAF50", fg="#ffffff", relief="flat", highlightthickness=0)
        shorten_button.pack(side="left", padx=10)

        # Short URL frame
        short_url_frame = tk.Frame(self.root, bg="#f0f0f0")
        short_url_frame.pack(fill="x", padx=20, pady=20)

        tk.Label(short_url_frame, text="Short URL:", font=("Arial", 14), bg="#f0f0f0").pack(side="left", padx=10)
        self.short_url_entry = tk.Entry(short_url_frame, width=40, font=("Arial", 14), relief="flat", borderwidth=1, highlightthickness=1)
        self.short_url_entry.pack(side="left", fill="x", expand=True, padx=10)

        # Footer frame
        footer_frame = tk.Frame(self.root, bg="#3498db", height=20)
        footer_frame.pack(fill="x", padx=10, pady=10)

    def shorten_url(self):
        url = self.url_entry.get()
        if not url:
            messagebox.showerror("Error", "Please enter a URL")
            return

        try:
            shortener = pyshorteners.Shortener()
            short_url = shortener.tinyurl.short(url)
            self.short_url_entry.delete(0, tk.END)
            self.short_url_entry.insert(0, short_url)
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = URLShortenerApp(root)
    root.mainloop()