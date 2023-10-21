import tkinter as tk

def is_int(val):
    if type(val) == int:
        return True
    else:
        if val.is_integer():
            return True
        else:
            return False

def calculate_stock_options():
    lot = float(entry_lot.get())
    capital_increase_percentage = float(entry_percentage.get())

    yeni_lot_sayisi = int(lot) * (1 + capital_increase_percentage / 100)
    decimal = yeni_lot_sayisi - int(yeni_lot_sayisi)
    decimal_label.config(text=f"You have 0.{decimal:.6f} as decimal")

    options_list = []
    checker = 0

    while len(options_list) < 5:  # Change the loop to find 5 options
        if is_int((lot + checker) * (1 + capital_increase_percentage / 100)):
            options_list.append(checker)
        checker += 1

    options_label.config(text=f"Options: {options_list}")

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

calculate_button = tk.Button(root, text="Calculate", command=calculate_stock_options)
calculate_button.pack()

decimal_label = tk.Label(root, text="")
decimal_label.pack()

options_label = tk.Label(root, text="")
options_label.pack()

root.mainloop()
