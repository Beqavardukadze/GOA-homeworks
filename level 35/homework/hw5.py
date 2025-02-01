# 5) შექმენით ფუნქცია რომელიც მომხმარებელს შეეკითხება ორ რიცხვს შემდეგ კი მათ გაამრავლებს ერთმანეთზე



def number():
    num = float(input("enter number: "))
    num1 = float(input("enter number: "))
    result = num * num1
    print(f" {num} * {num1} = {result}")

number()