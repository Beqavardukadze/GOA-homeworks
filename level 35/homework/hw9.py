# 9) შექმენით ფუნქცია რომელიც მომხმარებელს შეეკითხება ასაკს თუ მისი ასაკი მეტია 18 ზე უთხრას რომ სრულწლოვანია თუარადა არარის


def your_age():
    
    num = float(input("enter your age: "))
    
    
    if num >= 18:
        print(f"{num} srulwlovani.")
    else:
        print(f"{num} arasrulwlovani.")
   
your_age()