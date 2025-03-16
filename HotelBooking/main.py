import datetime
import re
from random import choice


class Hotel:
    def __init__(self):
        self.age=18
        self.veg=100
        self.non_veg=200
        self.high=1000
        self.medium=500
        self.low=250
        self.bill_amount=0


    def calculate_bill(self,room_choose,food_choose):
        if room_choose=='high':
            self.bill_amount+=self.high
        elif room_choose=='medium':
            self.bill_amount+=self.medium
        elif room_choose=='low':
            self.bill_amount=self.low

        if food_choose=='veg':
            self.bill_amount+=self.veg
        else:
            self.bill_amount+=self.non_veg

        print("\n".join([
            '=' * 50,
            '🏩 SIMBO HOTEL 🏩'.center(50),
            '='*50,
            '🙏THANK YOU FOR BOOKING ROOM 🙏'.center(50),
            f'Name: {self.name}'.center(50),
            f'Age: {self.age}'.center(50),
            f'Bill: {self.bill_amount}'.center(50),
            '=' * 50
        ]))

        return


    def calculate_age(self,date_of_birth):
        find_year=date_of_birth.split('/')
        find_year=int(find_year[2])
        current_year= datetime.date.today().year
        user_age=current_year-find_year
        return user_age

    def user_details(self):
        self.name=input("Enter your name : ")
        while True:
            self.date_of_birth = input("Date of Birth Format(00/00/0000): ")
            try:
                date_obj=datetime.datetime.strptime(self.date_of_birth,'%d/%m/%Y')
                break
            except ValueError:
                print('Invalid Date format')
        print(f'1.High:{self.high} \n2.Medium:{self.medium} \n3.Low{self.low} \n🥳perDay')
        self.room_choice=input()
        while True:
            if self.room_choice=='1':
                self.room_catagories='high'
                break
            elif self.room_choice=='2':
                self.room_catagories='medium'
                break
            elif self.room_choice=='3':
                self.room_catagories='low'
                break
            else:
                print('Enter the valid choice')

        print(f'1.Veg:{self.veg}\n2.NonVeg:{self.non_veg}  \n🥳perDay')
        self.food_choice = input("Enter your choice")
        while True:
            if self.food_choice=='1':
                self.food_catgories='veg'
                break
            elif self.food_choice=='2':
                self.food_catgories='non_veg'
                break
            else:
                print('Enter the valid choice')
        self.constraints(self.date_of_birth)

    def constraints(self,date_of_birth):
        user_age=self.calculate_age(date_of_birth)
        if user_age>=self.age:
            self.calculate_bill(self.room_catagories,self.food_catgories)
        else:
            print('After 18+ visit our hotel')
            return




v=Hotel()
v.user_details()

