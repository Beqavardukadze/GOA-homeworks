# 12) შექმენით ფუნქცია რომელიც მომხმარებელს შეეკითხება რიცხვს შემდეგ კი ერთიდან იმ რიცხვამდე დაბეჭდავს ყველა კენტ რიცხვ

def numbers():
   
    number = int(input("enter your number: "))
    
    
    for i in range(1, number + 1, 2):
        print(i)

numbers()