#  11) შექმენით ფუნქცია რომელიც მომხმარებელს შეეკითხება რიცხვს შემდეგ კი ერთიდან იმ რიცხვამდე დაბეჭდავს ყველა ლუწ რიცხვს

def numbers():
   
    number = int(input("enter your number: "))
    
    
    for i in range(2, number + 1, 2):
        print(i)

numbers()