import tkinter as tk
from tkinter import messagebox, Toplevel
import datetime as dt
import uuid
from pymongo import MongoClient

# ---------------- CONFIG ----------------
CURRENCY = "₹"
TAX_RATE = 0.05  # 5% tax

# MongoDB Connection
client = MongoClient("mongodb://localhost:27017/")  # MongoDB server ka URI
db = client["JavaJunctionDB"]
collection = db["bills"]

MENU = {
    "Espresso": 80,
    "Cappuccino": 120,
    "Latte": 150,
    "Mocha": 160,
    "Black Coffee": 70,
    "Tea": 50,
    "Green Tea": 60,
    "Iced Coffee": 130,
    "Brownie": 90,
    "Cheesecake": 140,
    "Sandwich": 110,
    "Muffin": 75
}

# ---------------- FUNCTIONS ----------------
def calculate_total():
    try:
        subtotal = 0
        for item, price in MENU.items():
            qty = int(entries[item].get() or 0)
            subtotal += price * qty

        tax = subtotal * TAX_RATE
        total = subtotal + tax

        lbl_subtotal_val.config(text=f"{CURRENCY}{subtotal:.2f}")
        lbl_tax_val.config(text=f"{CURRENCY}{tax:.2f}")
        lbl_total_val.config(text=f"{CURRENCY}{total:.2f}")

    except ValueError:
        messagebox.showerror("Error", "Invalid quantity entered!")

def generate_bill():
    customer = entry_name.get()
    if not customer:
        messagebox.showerror("Error", "Enter customer name!")
        return

    customer_id = str(uuid.uuid4())[:8]  # Short unique ID
    subtotal = lbl_subtotal_val.cget("text")
    tax = lbl_tax_val.cget("text")
    total = lbl_total_val.cget("text")

    bill_time = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    bill_lines = [
        "      ☕ JAVA JUNCTION BILL ☕",
        "-----------------------------------",
        f"Customer: {customer}",
        f"Customer ID: {customer_id}",
        f"Date: {bill_time}",
        "-----------------------------------"
    ]

    order_items = []
    for item, price in MENU.items():
        qty = int(entries[item].get() or 0)
        if qty > 0:
            bill_lines.append(f"{item:15} x{qty:<2} = {CURRENCY}{price * qty}")
            order_items.append({"item": item, "qty": qty, "price": price, "total": price * qty})

    bill_lines.append("-----------------------------------")
    bill_lines.append(f"Subtotal: {subtotal}")
    bill_lines.append(f"Tax:      {tax}")
    bill_lines.append(f"Total:    {total}")
    bill_lines.append("-----------------------------------")
    bill_lines.append("  Thank you! Visit Again ☺")

    bill_text = "\n".join(bill_lines)

    # Save to file
    with open("coffee_bill.txt", "w", encoding="utf-8") as f:
        f.write(bill_text)

    # Save to MongoDB
    bill_data = {
        "customer_name": customer,
        "customer_id": customer_id,
        "date": bill_time,
        "items": order_items,
        "subtotal": subtotal,
        "tax": tax,
        "total": total
    }
    collection.insert_one(bill_data)

    # Show in new window
    bill_window = Toplevel(root)
    bill_window.title("Bill")
    bill_window.config(bg="#fff3e0")
    tk.Label(bill_window, text="Java Junction - Your Bill", font=("Arial", 14, "bold"), bg="#ffcc80").pack(fill="x")
    tk.Label(bill_window, text=bill_text, font=("Courier", 11), bg="#fff3e0", justify="left").pack(padx=10, pady=10)

def reset():
    entry_name.delete(0, tk.END)
    for e in entries.values():
        e.delete(0, tk.END)
    lbl_subtotal_val.config(text="")
    lbl_tax_val.config(text="")
    lbl_total_val.config(text="")

# ---------------- UI ----------------
root = tk.Tk()
root.title("Java Junction Billing System")
root.geometry("420x620")
root.config(bg="#ffe0b2")

# Cafe Title
tk.Label(root, text="☕ JAVA JUNCTION ☕", font=("Arial", 16, "bold"), bg="#ffe0b2", fg="#4e342e").grid(row=0, column=0, columnspan=2, pady=10)

# Customer Name
tk.Label(root, text="Customer Name:", bg="#ffe0b2", font=("Arial", 12, "bold")).grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_name = tk.Entry(root, font=("Arial", 12))
entry_name.grid(row=1, column=1, pady=5)

# Menu Items
entries = {}
row_num = 2
for item, price in MENU.items():
    tk.Label(root, text=f"{item} ({CURRENCY}{price})", bg="#ffe0b2", font=("Arial", 11)).grid(row=row_num, column=0, padx=10, pady=3, sticky="w")
    e = tk.Entry(root, font=("Arial", 11), width=5)
    e.grid(row=row_num, column=1)
    entries[item] = e
    row_num += 1

# Buttons
tk.Button(root, text="Calculate", command=calculate_total, bg="#81c784", fg="white", font=("Arial", 12, "bold")).grid(row=row_num, column=0, pady=10)
tk.Button(root, text="Generate Bill", command=generate_bill, bg="#64b5f6", fg="white", font=("Arial", 12, "bold")).grid(row=row_num, column=1, pady=10)

# Summary
tk.Label(root, text="Subtotal:", bg="#ffe0b2", font=("Arial", 12, "bold")).grid(row=row_num+1, column=0, sticky="w", padx=10)
lbl_subtotal_val = tk.Label(root, text="", bg="#ffe0b2", font=("Arial", 12))
lbl_subtotal_val.grid(row=row_num+1, column=1, sticky="w")

tk.Label(root, text="Tax (5%):", bg="#ffe0b2", font=("Arial", 12, "bold")).grid(row=row_num+2, column=0, sticky="w", padx=10)
lbl_tax_val = tk.Label(root, text="", bg="#ffe0b2", font=("Arial", 12))
lbl_tax_val.grid(row=row_num+2, column=1, sticky="w")

tk.Label(root, text="Total:", bg="#ffe0b2", font=("Arial", 12, "bold")).grid(row=row_num+3, column=0, sticky="w", padx=10)
lbl_total_val = tk.Label(root, text="", bg="#ffe0b2", font=("Arial", 12))
lbl_total_val.grid(row=row_num+3, column=1, sticky="w")

# Reset Button
tk.Button(root, text="Reset", command=reset, bg="#e57373", fg="white", font=("Arial", 12, "bold")).grid(row=row_num+4, column=0, columnspan=2, pady=10)

root.mainloop()
