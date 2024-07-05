import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from datetime import datetime
import os
import glob
import shutil
import zipfile

class LogCaptureApp:
    def __init__(self, master):
        self.master = master
        master.title("Log File Capture Application")
        master.geometry("600x400")

        # Variables
        self.start_time = tk.StringVar()
        self.end_time = tk.StringVar()
        self.software_name = tk.StringVar()
        self.config_path = tk.StringVar()
        self.log_path = tk.StringVar()

        # Create and place widgets
        self.create_widgets()

    def create_widgets(self):
        # Start time
        ttk.Label(self.master, text="Start Time:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        ttk.Entry(self.master, textvariable=self.start_time).grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(self.master, text="Capture Start", command=self.capture_start).grid(row=0, column=2, padx=5, pady=5)

        # End time
        ttk.Label(self.master, text="End Time:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        ttk.Entry(self.master, textvariable=self.end_time).grid(row=1, column=1, padx=5, pady=5)
        ttk.Button(self.master, text="Capture End", command=self.capture_end).grid(row=1, column=2, padx=5, pady=5)

        # Software name
        ttk.Label(self.master, text="Software Name:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        ttk.Entry(self.master, textvariable=self.software_name).grid(row=2, column=1, padx=5, pady=5)

        # Config path
        ttk.Label(self.master, text="Config Path:").grid(row=3, column=0, padx=5, pady=5, sticky="w")
        ttk.Entry(self.master, textvariable=self.config_path).grid(row=3, column=1, padx=5, pady=5)
        ttk.Button(self.master, text="Browse", command=lambda: self.browse_directory(self.config_path)).grid(row=3, column=2, padx=5, pady=5)

        # Log path
        ttk.Label(self.master, text="Log Path:").grid(row=4, column=0, padx=5, pady=5, sticky="w")
        ttk.Entry(self.master, textvariable=self.log_path).grid(row=4, column=1, padx=5, pady=5)
        ttk.Button(self.master, text="Browse", command=lambda: self.browse_directory(self.log_path)).grid(row=4, column=2, padx=5, pady=5)

        # Store button
        ttk.Button(self.master, text="Store", command=self.store_files).grid(row=5, column=1, padx=5, pady=20)

    def capture_start(self):
        self.start_time.set(datetime.now().strftime("%y%m%d_%H%M%S"))

    def capture_end(self):
        self.end_time.set(datetime.now().strftime("%y%m%d_%H%M%S"))

    def browse_directory(self, path_var):
        directory = filedialog.askdirectory()
        if directory:
            path_var.set(directory)

    def store_files(self):
        # Validate inputs
        if not all([self.start_time.get(), self.end_time.get(), self.software_name.get(), self.config_path.get(), self.log_path.get()]):
            messagebox.showerror("Error", "All fields must be filled")
            return

        # Get user description
        description = self.get_description()
        if not description:
            return  # User cancelled

        # Create temporary directories
        temp_dir = "temp_storage"
        logs_dir = os.path.join(temp_dir, "Logs")
        ini_dir = os.path.join(temp_dir, "Ini")
        os.makedirs(logs_dir, exist_ok=True)
        os.makedirs(ini_dir, exist_ok=True)

        # Copy log files
        self.copy_log_files(logs_dir)

        # Copy ini files
        self.copy_ini_files(ini_dir)

        # Create description file
        with open(os.path.join(temp_dir, "description.txt"), "w") as f:
            f.write(description)

        # Create zip file
        zip_filename = f"{self.start_time.get()}_{self.software_name.get()}.zip"
        with zipfile.ZipFile(zip_filename, 'w') as zipf:
            for root, dirs, files in os.walk(temp_dir):
                for file in files:
                    zipf.write(os.path.join(root, file), 
                               os.path.relpath(os.path.join(root, file), temp_dir))

        # Clean up
        shutil.rmtree(temp_dir)

        messagebox.showinfo("Success", f"Files stored in {zip_filename}")

    def get_description(self):
        description_window = tk.Toplevel(self.master)
        description_window.title("Enter Description")
        description = tk.StringVar()
        ttk.Entry(description_window, textvariable=description, width=50).pack(padx=10, pady=10)
        ttk.Button(description_window, text="OK", command=description_window.quit).pack(pady=10)
        description_window.mainloop()
        description_window.destroy()
        return description.get()

    def copy_log_files(self, logs_dir):
        start_time = datetime.strptime(self.start_time.get(), "%y%m%d_%H%M%S")
        end_time = datetime.strptime(self.end_time.get(), "%y%m%d_%H%M%S")
        for file in glob.glob(os.path.join(self.log_path.get(), "Data_*.CSV")):
            file_time = datetime.strptime(os.path.basename(file)[5:18], "%y%m%d_%H%M%S")
            if start_time <= file_time <= end_time:
                shutil.copy(file, logs_dir)

    def copy_ini_files(self, ini_dir):
        for file in glob.glob(os.path.join(self.config_path.get(), "*.ini")):
            shutil.copy(file, ini_dir)

if __name__ == "__main__":
    root = tk.Tk()
    app = LogCaptureApp(root)
    root.mainloop()