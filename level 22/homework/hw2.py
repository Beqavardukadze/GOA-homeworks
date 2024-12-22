# 2) მომხმარებელს შემოატანინეთ რიცხვი შემდეგ კი ერთიდან ამ რიცხვამდე დაბეჭდეთ რიცხვების საშუალო არითმეტიკული


run = int(input("enter your number: "))

sum = 0

for i in range(0, run + 1):
    sum += i
print(sum / run)