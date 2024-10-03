import tkinter as tk
from tkinter import messagebox
import pyshorteners

class URLShortenerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("URL Shortener")
        self.root.resizable(False, False)
        self.root.configure(bg="#2c3e50")

        self.create_widgets()

    def create_widgets(self):
        # Header frame
        header_frame = tk.Frame(self.root, bg="#2ecc71", height=100)
        header_frame.pack(fill="x", padx=10, pady=10)

        tk.Label(header_frame, text="URL Shortener", font=("Arial", 36, "bold"), bg="#2ecc71", fg="#ffffff").pack(pady=20)

        # Main frame
        main_frame = tk.Frame(self.root, bg="#2c3e50")
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # URL entry frame
        url_frame = tk.Frame(main_frame, bg="#2c3e50")
        url_frame.pack(fill="x", padx=10, pady=10)

        tk.Label(url_frame, text="Enter URL:", font=("Arial", 18), bg="#2c3e50", fg="#ffffff").pack(side="left", padx=10)
        self.url_entry = tk.Entry(url_frame, width=40, font=("Arial", 18), relief="flat", borderwidth=1, highlightthickness=1, bg="#ecf0f1")
        self.url_entry.pack(side="left", fill="x", expand=True, padx=10)

        # Shorten button frame
        shorten_button_frame = tk.Frame(main_frame, bg="#2c3e50")
        shorten_button_frame.pack(fill="x", padx=10, pady=10)

        shorten_button = tk.Button(shorten_button_frame, text="Shorten URL", command=self.shorten_url, font=("Arial", 18), bg="#2ecc71", fg="#ffffff", relief="flat", highlightthickness=0)
        shorten_button.pack(fill="x", padx=10, pady=10)

        # Short URL frame
        short_url_frame = tk.Frame(main_frame, bg="#2c3e50")
        short_url_frame.pack(fill="x", padx=10, pady=10)

        tk.Label(short_url_frame, text="Short URL:", font=("Arial", 18), bg="#2c3e50", fg="#ffffff").pack(side="left", padx=10)
        self.short_url_entry = tk.Entry(short_url_frame, width=40, font=("Arial", 18), relief="flat", borderwidth=1, highlightthickness=1, bg="#ecf0f1")
        self.short_url_entry.pack(side="left", fill="x", expand=True, padx=10)

        # Footer frame
        footer_frame = tk.Frame(self.root, bg="#2ecc71", height=20)
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
