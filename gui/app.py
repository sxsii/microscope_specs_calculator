import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog

from core.calculator import calculate_real_size
from core.microscope_data import MICROSCOPES
from core.database import create_table
from core.database import save_record
from core.database import get_records


create_table()


class MicroscopeApp:

    def __init__(self, root):

        self.root = root

        self.root.title("Microscope Calculator")

        self.root.geometry("600x500")

        self.image_path = None

        self.build_ui()

    def build_ui(self):

        tk.Label(self.root, text="Username").pack()

        self.username_entry = tk.Entry(self.root, width=40)
        self.username_entry.pack()

        tk.Label(self.root, text="Measured Size (mm)").pack()

        self.size_entry = tk.Entry(self.root, width=40)
        self.size_entry.pack()

        tk.Label(self.root, text="Microscope").pack()

        self.microscope_var = tk.StringVar()

        self.microscope_dropdown = ttk.Combobox(
            self.root,
            textvariable=self.microscope_var,
            values=list(MICROSCOPES.keys()),
            state="readonly"
        )

        self.microscope_dropdown.pack()

        tk.Label(self.root, text="Output Unit").pack()

        self.unit_var = tk.StringVar()

        self.unit_dropdown = ttk.Combobox(
            self.root,
            textvariable=self.unit_var,
            values=["nm", "um", "mm", "cm", "m"],
            state="readonly"
        )

        self.unit_dropdown.pack()

        tk.Button(
            self.root,
            text="Upload Image",
            command=self.upload_image
        ).pack(pady=10)

        tk.Button(
            self.root,
            text="Calculate",
            command=self.calculate
        ).pack(pady=10)

        self.result_label = tk.Label(
            self.root,
            text="Result appears here"
        )

        self.result_label.pack(pady=20)

    def upload_image(self):

        self.image_path = filedialog.askopenfilename(
            filetypes=[("Image Files", "*.png *.jpg *.jpeg")]
        )

        if self.image_path:
            messagebox.showinfo(
                "Success",
                "Image uploaded successfully"
            )

    def calculate(self):

        try:

            username = self.username_entry.get()

            measured_size = float(
                self.size_entry.get()
            )

            microscope_type = self.microscope_var.get()

            output_unit = self.unit_var.get()

            magnification = MICROSCOPES[microscope_type]

            real_size_mm, converted = calculate_real_size(
                measured_size,
                magnification,
                output_unit
            )

            self.result_label.config(
                text=f"Real Size: {converted:.6f} {output_unit}"
            )

            save_record(
                username,
                measured_size,
                microscope_type,
                magnification,
                converted,
                output_unit
            )

        except Exception as e:

            messagebox.showerror("Error", str(e))


root = tk.Tk()

app = MicroscopeApp(root)

root.mainloop()