#  5) მომხმარებელს შემოატანინეთ რიცხვი შემდეგ კი ერთიდან ამ რიცხვამდე დაბეჭდეთ ყველა რიცხვის ნამრავლი



run = int(input("enter number: "))

sum = 1

for i in range(1, run + 1):
    sum = sum * i

print(sum)