# funqcia
# parametrebi, argumentebi

# def my_func(name):
#     print(name + "hello")

# my_func("beqa")
# my_func("gabriel")


#1) შექმენით ფუნქცია რომელსაც ექნება ორი პარამეტრი ხოლო ამ ფუნქციამ უნდა გადაამრავლოს ეს ორი რიცხვი ერთმანეთზე შემდეგ კი დაიბეჭდოს მიღებული ნარმავლი ლუწია თუ კენტი ნამრავლთან ერთად, გამოიძახეთ ეს ფუნქცია რამდენჯერმე და გადაეცით არგუმენტები(სვადასვა რიცხვები)


def my_func(num1, num2):
    multiple = num1 * num2

    if multiple % 2 == 0:
        print("luwi" + " " + str(multiple))
    else:
        print("kenti"+ " " + str(multiple))

my_func(2, 4)