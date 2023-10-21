import tkinter as tk
from tkinter import messagebox

def calculate_stock_options():
    try:
        lot = float(entry_lot.get())
        capital_increase_percentage = float(entry_percentage.get())
        desired_stock_count = float(entry_desired_stock_count.get())

        if lot < 0:
            raise ValueError("Number of stocks cannot be less than 0")
        if capital_increase_percentage == 0:
            raise ValueError("Percentage of capital increase cannot be zero")
        if desired_stock_count == 0:
            raise ValueError("Desired stock count cannot be 0")

        yeni_lot_sayisi = lot * (1 + capital_increase_percentage / 100)
        decimal = yeni_lot_sayisi - int(yeni_lot_sayisi)
        decimal_label.config(text=f"You have 0.{decimal:.6f} as decimal")

        stocks_to_buy = max(0, desired_stock_count - lot)
        stocks_to_buy_label.config(text=f"Stocks to buy before capital increase: {stocks_to_buy}")

        options_list = [int(lot + i) for i in range(5)]
        options_label.config(text=f"Options: {options_list}")

        error_label.config(text="")  # Clear any previous error message
    except ValueError as e:
        messagebox.showerror("Error", str(e))
    except Exception as e:
        messagebox.showerror("Error", "An error occurred. Please check your inputs.")

root = tk.Tk()
root.title("Bedelsiz Hesaplayıcı - Capital Increase Calculator")
root.geometry("320x400")
root.attributes("-alpha", 0.5)  # 50% transparent background

# Set a uniform color for labels
label_bg_color = "#C0C0C0"

label_lot = tk.Label(root, text="Number of Stocks:", bg=label_bg_color)
label_lot.grid(row=0, column=0, sticky="w")

entry_lot = tk.Entry(root)
entry_lot.grid(row=0, column=1)

label_percentage = tk.Label(root, text="Percentage of Capital Increase:", bg=label_bg_color)
label_percentage.grid(row=1, column=0, sticky="w")

entry_percentage = tk.Entry(root)
entry_percentage.grid(row=1, column=1)

label_desired_stock_count = tk.Label(root, text="How many stocks you need to have after the capital increase:", bg=label_bg_color)
label_desired_stock_count.grid(row=2, column=0, sticky="w")

entry_desired_stock_count = tk.Entry(root)
entry_desired_stock_count.grid(row=2, column=1)

calculate_button = tk.Button(root, text="Calculate", command=calculate_stock_options, bg="dark orange")
calculate_button.grid(row=3, column=1, sticky="se")

decimal_label = tk.Label(root, text="", bg=label_bg_color)
decimal_label.grid(row=4, columnspan=2)

stocks_to_buy_label = tk.Label(root, text="", bg=label_bg_color)
stocks_to_buy_label.grid(row=5, columnspan=2)

error_label = tk.Label(root, text="", fg="red", bg=label_bg_color)
error_label.grid(row=6, columnspan=2)

options_label = tk.Label(root, text="", bg=label_bg_color)
options_label.grid(row=7, columnspan=2)

root.mainloop()
