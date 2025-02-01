# 7) შექმენით ფუნქცია რომელიც მომხმარებელს შეეკითხება რიცხვს შემდეგ კი დაბეჭდავს ეს რიცხვი ლუწია თუ კენტი


def number():
    num = int(input("enter your number: "))

    if num % 2 == 0:
        print("luwia")
    else:
        print("kentia")

number()