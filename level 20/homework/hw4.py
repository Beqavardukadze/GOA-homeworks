# 5) დაწერეთ ციკლი რომელიც ლუწს გამოიტანს " მე მიყვარს გოა" და კენტს " მე მიყვარს პროგრამირება".

a=int(input("num: "))

for i in range(0, a):
    if i %2==0:
        print("me miyvars goa")
    else:
        print("miyvars programireba")