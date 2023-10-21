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
        desired_stock_count = float(entry_desired_stock_count.get())

        # Check for exceptions
        if lot < 0:
            raise ValueError("Number of stocks you entered cannot be less than 0")
        if capital_increase_percentage == 0:
            raise ValueError("Number of capital increase cannot be zero")
        if len(entry_percentage.get().split(".")[1]) > 8:
            raise ValueError("Limit decimals in number of capital increase to 8 or fewer")
        if desired_stock_count == 0:
            raise ValueError("Desired stock count cannot be 0")

        yeni_lot_sayisi = int(lot) * (1 + capital_increase_percentage / 100)
        decimal = yeni_lot_sayisi - int(yeni_lot_sayisi)
        decimal_label.config(text=f"You have 0.{decimal:.6f} as decimal")

        # Calculate the number of stocks that need to be bought before the capital increase
        stocks_to_buy = max(0, int(desired_stock_count) - int(lot))
        stocks_to_buy_label.config(text=f"Stocks to buy before capital increase: {stocks_to_buy}")

        options_list = []
        checker = 0

        while len(options_list) < 5:
            if is_int((lot + checker) * (1 + capital_increase_percentage / 100)):
                options_list.append(checker)
            checker += 1

        options_label.config(text=f"Options: {options_list}")

        error_label.config(text="")  # Clear any previous error message
    except ValueError as e:
        messagebox.showerror("Error", str(e))
    except Exception as e:
        messagebox.showerror("Error", "An error occurred. Please check your inputs.")

root = tk.Tk()
root.title("Stock Calculator")
root.configure(bg="#30D5C8")

label_lot = tk.Label(root, text="Number of Stocks:")
label_lot.pack()

entry_lot = tk.Entry(root)
entry_lot.pack()

label_percentage = tk.Label(root, text="Percentage of Capital Increase:")
label_percentage.pack()

entry_percentage = tk.Entry(root)
entry_percentage.pack()

label_desired_stock_count = tk.Label(root, text="How many stocks you need to have after the capital increase:")
label_desired_stock_count.pack()

entry_desired_stock_count = tk.Entry(root)
entry_desired_stock_count.pack()

calculate_button = tk.Button(root, text="Calculate", command=calculate_stock_options)
calculate_button.pack()

decimal_label = tk.Label(root, text="")
decimal_label.pack()

stocks_to_buy_label = tk.Label(root, text="")
stocks_to_buy_label.pack()

error_label = tk.Label(root, text="", fg="red")
error_label.pack()

options_label = tk.Label(root, text="")
options_label.pack()

root.mainloop()
