# 3) მომხმარებელს შემოატანინეთ რიცხვი შემდეგ კი ერთიდან ამ რიცხვამდე დაბეჭდეთ ყველა რიცხვის კვადრატის ჯამი

run = int(input("enter number: "))

sum = 0

for i in range(run):
    sum += (i ** 2)

print(sum)