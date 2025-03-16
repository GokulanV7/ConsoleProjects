import sqlite3
import hashlib

class Banking:
    def __init__(self):
        self.con=sqlite3.connect('bank.db')
        self.cursor=self.con.cursor()
        self.user_id=None

        self.cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            pin TEXT NOT NULL,
            balance REAL DEFAULT 0
            )
'''
        )
        self.con.commit()
    def hash_pin(self,pin):
        return hashlib.sha256(pin.encode()).hexdigest()
    

    def register(self):
        name=input('😊 Enter your name : ').strip()
        pin=input(" 👮 Enter a Pin : ").strip()

        if len(pin)!=4 or not pin.isdigit():
            print("⚠️ Invalid Pin! Must be 4 digits")
            return
        try:
            self.cursor.execute("INSERT INTO users(name,pin)VALUES(?,?)",(name,self.hash_pin(pin)))
            self.con.commit()
            print("\n".join([
             "="*44,
             "👍 Registration is Completed,Please Login !".center(40),
             "="*44
        ]))
        except sqlite3.IntegrityError:
            print("Username already taken. Try a different one")

    
    def login(self):
        name=input('😊 Enter your name : ').strip()
        pin=input(" 👮 Enter a Pin : ").strip()
        
        self.cursor.execute("SELECT id,pin FROM users WHERE name=?",(name,))
        user=self.cursor.fetchone()

        if user and self.hash_pin(pin)==user[1]:
            self.user_id=user[0]
            print(self.user_id)
            print("\n".join([
             "="*44,
             "👍 Login Success".center(40),
             "="*44
        ]))
            return True
        else:
            print("\n".join([
             "="*44,
             "❌ Invalid Credentials".center(40),
             "="*44
        ]))
            print("❌ Invalid Credentials")
            return False
    

    def deposit(self):
        amount=float(input(" 💵 Enter the Amount : "))
        if amount<=0:
            print("⚠️ Invalid Amount")
            return
        self.cursor.execute("UPDATE users SET balance = balance + ? WHERE id=?",(amount,self.user_id))
        self.con.commit()
        print("\n".join([
             "="*44,
             "👍 Deposit Success".center(40),
             "="*44
        ]))

    
    def withdraw(self):
        amount=float(input(" 💵 Enter the Amount : "))
        self.cursor.execute("SELECT balance FROM users WHERE id = ?",(self.user_id,))
        balance=self.cursor.fetchone()[0]

        if amount<=0:
            print('⚠️ Enter the Valid Amount')
        elif amount>balance:
            print(' 😫 Insufficient balance')
        else:
            print(balance)
            self.cursor.execute("UPDATE users SET balance=balance - ? WHERE id= ? ",(amount,self.user_id,))
            self.con.commit()
            print("\n".join([
             "="*44,
             f' 👍 Withdraw ${amount} successfully!'.center(40),
             "="*44
        ]))
            

    def checkbalance(self):
        self.cursor.execute("SELECT balance FROM users WHERE id = ?",(self.user_id,))
        balance=self.cursor.fetchone()[0]
        print("\n".join([
             "🥳 Available Balannce 🥳".center(40),
             "="*44,
             f'${balance}'.center(40),
             "="*44
        ]))

    
    def close_connection(self):
        self.con.close

bank=Banking()
while True:
    print("\n".join([
         "🌟 WELCOME TO THE SIMBO BANK 🌟".center(40),
        "="*44,
        "1. 🥳 REGISTER".center(40),
        "2. 😊 LOGIN".center(40),
        "3. ❌ EXIT".center(40),
        "="*44,    
    ]))
    choice=input("Choose an option : ")
    if choice=='1':
        bank.register()
    elif choice=='2':
        if bank.login():
            while True:
                print("\n".join([
        "="*44,
         "🌟Enter Your Choice🌟".center(40)     ,       
        "="*44,
        "1. 💰 DEPOSIT".center(40),
        "2. 💵 WITHDRAW".center(40),
        "3. ✅ CHECK BALANCE".center(40),
        "4. ⎆ LOGOUT".center(40),
        "="*44,    
    ])) 
                print("\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. LogOut")
                action=input(" 🪧 Enter your opertion : ")
                if action=='1':
                    bank.deposit()
                elif action=='2':
                    bank.withdraw()
                elif action=='3':
                    bank.checkbalance()
                elif action=='4':
                    bank.close_connection()
                    print("Logging out...")
                    break
                else:
                    print("❌ Invalid Choice")
    elif choice=='3':
        bank.close_connection()
        print("Exiting... Thank you!")
        print("\n".join([
            "="*40,
            "🫡 Exiting... Thank you!",
            "="*40,
        ]))
        break
    else:
        print("❌ Invalid Choice")
