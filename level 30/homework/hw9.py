# 9) გამოიყენეთ append და pop რომ დაატრიალოთ ლისტი და დაპრინტეთ შემდეგ




list = []

print(list)

i = 0

while i <5:
    num = int(input("enter your number: "))
    list.append(num)
    i += 1

list.reverse()

print(list)