#  1) შექმენით სია რომელშიც იქნება 10 სხვადასხვა რენდომ რიცხვი, შემდეგ მიწდვით ამ სიის თითოეულ ელემენტს და დაბეჭდეთ თითოეული ელემენტი ოღონდ თუ რიცხვი იქნება ხუთის ჯერადი მიუწერეთ გვერძე რომ ხუთის ჯერადია ხოლო სამის ჯერადებს მიუწერეთ რომ სამის ჯერადია


number = [1,2,3,4,5,6,7,8,9,10]

for i in range(len(number)):
    if number[i] % 5 == 0:
        print(number[i]," 5 is ciladi ")
    if number[i] % 3 == 0: 
        print(number[i]," 3 is ciladi")
    else:
        print(number[i],"ar ak ciladi ")



