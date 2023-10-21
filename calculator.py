import tkinter as tk
from tkinter import messagebox

def is_int(val):
    if type(val) == int:
        return True
    else:
        if val.is_integer():
            return True
        else:
            return False

def calculate_stock_options():
    try:
        lot = float(entry_lot.get())
        capital_increase_percentage = float(entry_percentage.get())

        if lot == 0:
            raise ValueError("Number of stocks cannot be zero")
        if capital_increase_percentage == 0:
            raise ValueError("Percentage of capital increase cannot be zero")

        yeni_lot_sayisi = round(int(lot) * (1 + capital_increase_percentage / 100), 6)
        yeni_lot_sayisi_label.config(text=f"Yeni Lot Sayısı: {yeni_lot_sayisi:.6f}")

        options_list = []
        checker = 0

        while len(options_list) < 3:
            if is_int((lot + checker) * (1 + capital_increase_percentage / 100)):
                options_list.append(checker)
            checker += 1

        options_label.config(text=f"Buy: {options_list} stocks to make it int")
        options_label.grid(row=5, column=0, columnspan=2, pady=(10, 0), sticky='w')  # Left align options_label

    except ValueError as e:
        messagebox.showerror("Error", str(e))
    except Exception as e:
        messagebox.showerror("Error", "An error occurred. Please check your inputs")

# Create the main window
root = tk.Tk()
root.title("Stock Calculator")
root.geometry("420x250")  # Set the window size to 600x250
root.resizable(0, 0)  # Make the window non-resizable

# Create and place widgets in the window
label_lot = tk.Label(root, text="Number of Stocks:")
label_lot.grid(row=0, column=0, padx=10, pady=(10, 0), sticky='w')  # Align left

entry_lot = tk.Entry(root)
entry_lot.grid(row=0, column=1, padx=10, pady=(10, 0))

label_percentage = tk.Label(root, text="Percentage of Capital Increase:")
label_percentage.grid(row=1, column=0, padx=10, sticky='w')  # Align left

entry_percentage = tk.Entry(root)
entry_percentage.grid(row=1, column=1, padx=10)

calculate_button = tk.Button(root, text="Calculate", command=calculate_stock_options, bg="dark orange", bd=0)
calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

yeni_lot_sayisi_label = tk.Label(root, text="", fg="blue")
yeni_lot_sayisi_label.grid(row=3, column=0, columnspan=2, pady=(10, 0), sticky='w')  # Left align yeni_lot_sayisi_label

options_label = tk.Label(root, text="Options:")
options_label.grid(row=4, column=0, columnspan=2, pady=10, sticky='w')  # Left align options_label

# Function to properly close the application
def on_closing():
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)  # Call on_closing when closing the window

# Start the GUI event loop
root.mainloop()
