<img width="535" height="820" alt="Screenshot 2025-08-15 233314" src="https://github.com/user-attachments/assets/21b09ac8-321d-4618-9fc3-06b00a63ba8b" /># ☕ Java Junction – Café Billing System with MongoDB Integration

**Java Junction** is a Python-based café billing application built using **Tkinter** for GUI and **MongoDB** for backend storage.  
It automates the order-taking and billing process for cafés or restaurants, while keeping a detailed sales record in the database.

---

# 🚀 Features

- **Interactive GUI** – Simple Tkinter-based interface for quick order input.
- **Dynamic Menu** – Predefined coffee, snacks, and dessert menu with prices.
- **Automatic Bill Calculation**  
  - Subtotal based on selected items & quantities  
  - 5% tax calculation  
  - Grand total display
- **Bill Generation** – Printable receipt with:
  - Customer Name
  - Unique Bill ID
  - Ordered Items & Quantity
  - Subtotal, Tax, and Total
- **MongoDB Storage** – Every bill is saved in the database with full details.
- **Reset Option** – Clears all fields for a new order.

---

# 🛠️ Tech Stack

- **Frontend (GUI):** Python Tkinter  
- **Backend Logic:** Python  
- **Database:** MongoDB (via `pymongo`)  
- **Libraries Used:**  
  - `tkinter` – GUI  
  - `datetime` – Timestamps  
  - `uuid` – Unique Bill IDs  
  - `pymongo` – Database connection

---

# 📂 Project Flow

1. **Order Entry** – User selects items and enters quantity.
2. **Bill Calculation** – Subtotal, tax, and total computed automatically.
3. **Bill Generation** – Printable bill with all order details.
4. **Data Storage** – Bill stored in MongoDB for future reference.

---

# 📸 Screenshots

## 1️⃣ Order Entry Window
<img width="535" height="820" alt="Screenshot 2025-08-15 233314" src="https://github.com/user-attachments/assets/40ddda66-974f-4a52-bd45-b6617ed24566" />

## 2️⃣ Bill Window
<img width="435" height="452" alt="Screenshot 2025-08-15 233332" src="https://github.com/user-attachments/assets/f09b3b11-2a20-497f-bf9e-b266b7591a5a" />

## 3️⃣ MongoDB Records
<img width="1766" height="990" alt="Screenshot 2025-08-15 233530" src="https://github.com/user-attachments/assets/5cc02036-3264-4231-87d5-d9777b92f386" />

---
