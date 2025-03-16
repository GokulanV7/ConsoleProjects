# Hotel Booking System

## Overview
This project is a simple hotel booking system written in Python. It allows users to enter their details, select a room category, and choose a food preference to generate a bill. The program also checks age constraints to ensure bookings are only made for users 18 years or older.

## Features
- User input for name and date of birth
- Room category selection (High, Medium, Low)
- Food selection (Veg, Non-Veg)
- Age verification (Only 18+ allowed)
- Automated bill calculation
- Console-based interface with structured output

## Installation & Execution
### Prerequisites
Ensure you have Python installed on your system. This script runs on Python 3.x.

### Steps to Run the Program
1. Clone or download the script.
2. Open a terminal or command prompt in the script's directory.
3. Run the script using:
   ```sh
   python hotel_booking.py
   ```
4. Follow the on-screen prompts to enter user details and select options.

## Code Explanation
### Class: `Hotel`
- **Attributes:**
  - `age`: Minimum age required for booking (18)
  - `veg`, `non_veg`: Prices for food categories
  - `high`, `medium`, `low`: Prices for room categories
  - `bill_amount`: Stores the total bill amount
- **Methods:**
  - `calculate_bill(room_choose, food_choose)`: Calculates and prints the final bill.
  - `calculate_age(date_of_birth)`: Computes the user's age from the entered date of birth.
  - `user_details()`: Takes user input for name, date of birth, room category, and food preference.
  - `constraints(date_of_birth)`: Checks if the user meets the age requirement before proceeding with booking.

## Example Output
```
Enter your name: John Doe
Date of Birth Format(00/00/0000): 15/08/2000
1. High: 1000
2. Medium: 500
3. Low: 250
🥳 per Day
2
1. Veg: 100
2. Non-Veg: 200  
🥳 per Day
1
==================================================
🏩 SIMBO HOTEL 🏩
==================================================
🙏THANK YOU FOR BOOKING ROOM 🙏
                 Name: John Doe                 
                 Age: 24                        
                 Bill: 600                      
==================================================
```

## Possible Enhancements
- Implement a graphical user interface (GUI) using Tkinter or PyQt.
- Add payment processing and booking confirmation.
- Store booking details in a database.

## License
This project is open-source and can be modified as needed. Feel free to contribute!

## Author
Developed by GOKULANV7

