'''
    Author: Frankie Barrios
    Date: 10/31/17
    Purpose: This program convers measurements in cups to fluid ounces.
'''

def purpose():
    print("This program converts measurements in cups to fluid ounces.")

def conversion():
    cups = int(input("Enter the number of cups: "))
    ounces = cups * 8
    print("That is equal to", ounces, "fluid ounces.")

def end():
    print("Thanks for using my app!")
    
def main():
    purpose()
    conversion()
    end()
    
main()
