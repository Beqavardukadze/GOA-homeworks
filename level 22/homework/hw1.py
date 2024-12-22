# 1) მომხმარებელს შემოატანინეთ რიცხვი შემდეგ კი ერთიდან ამ რიცხვამდე დაბეჭდეთ ყველა რიცხვის ჯამი

run = int(input("enter your number: "))

sum = 0

for i in range(run):
    sum += i
print(sum)