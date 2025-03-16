# Banking Application (Python + SQLite)

## 📌 Overview

This is a simple **Banking System** implemented in Python with an **SQLite** database. It allows users to:

- 🥳 **Register** with a unique name and 4-digit PIN.
- 😊 **Login** securely.
- 💰 **Deposit** money into their account.
- 💸 **Withdraw** money (if they have enough balance).
- 🏦 **Check their account balance**.
- ❌ **Logout & Exit** the system.

## 🛠️ Technologies Used

- **Python** (for backend logic)
- **SQLite** (for database storage)

## 📂 Database Structure

The application uses an SQLite database (`bank.db`) with a `users` table:

| Column    | Data Type             | Description                         |
| --------- | --------------------- | ----------------------------------- |
| `id`      | INTEGER (Primary Key) | Auto-incremented user ID            |
| `name`    | TEXT (Unique)         | User's name                         |
| `pin`     | TEXT                  | Hashed 4-digit PIN                  |
| `balance` | REAL                  | User's current balance (default: 0) |

## 🚀 How to Run the Application

### 1️⃣ **Run the Application**

```sh
python bank.py
```

## 🏦 Features

1. **User Registration**
   - Requires a **unique name** and **4-digit PIN**.
   - Stores hashed PINs for security.
2. **User Login**
   - Validates name and PIN.
   - Grants access to banking functions upon successful login.
3. **Deposit Money**
   - Adds money to the user’s account.
4. **Withdraw Money**
   - Deducts money **only if the user has sufficient balance**.
5. **Check Balance**
   - Displays the current balance.
6. **Logout & Exit**
   - Allows the user to securely log out and exit the system.

## 🔒 Security Measures

✅ **PIN Hashing** (SHA-256) – Ensures that the PIN is securely stored. ✅ **Input Validation** – Prevents invalid entries. ✅ **SQLite Transactions** – Ensures data integrity.

## 📸 Sample Output

```
********************************
        WELCOME TO BANK         
********************************
1. 🥳 REGISTER
2. 😊 LOGIN
3. ❌ EXIT
Choose an option: 2
Enter your name: JohnDoe
Enter your PIN: ****
✅ Login successful!

1. 💰 Deposit
2. 💸 Withdraw
3. 🏦 Check Balance
4. 🔒 Logout
Choose an action: 3
💰 Your balance: $500
```

## 📌 Future Improvements

🔹 **Transaction History** – Show past deposits & withdrawals. 🔹 **Interest Calculation** – Implement basic savings account interest. 🔹 **Admin Panel** – Allow an admin to manage users.

## 🎯 Conclusion

This project is a great starting point for learning **Python, SQLite, and basic banking logic**. Feel free to expand and customize it! 🚀

---

✍️ **Created by  GOKULANV7**

