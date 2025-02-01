# 8) შექმენით ფუნქცია რომელიც მომხმარებელს შეეკითხება რიღხვს შემდეგ კი დაბეჭდავს დადებითია თუ უარყოფითი


def number():
    
    num = float(input("enter your number: "))
    
    
    if num > 0:
        print(f"{num} dadebiti.")
    elif number < 0:
        print(f"{num} uaryofiti.")
    else:
        print(f"{num} nuli.")

number()