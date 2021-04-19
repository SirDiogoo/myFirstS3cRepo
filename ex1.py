pessoas = int(input("Quantidade de pessoas: "))
if pessoas < 5:
    print("n baixo de pessoas")
elif pessoas >= 5 and pessoas <= 10:
    print("n médio de pessoas")
elif pessoas >= 11 and pessoas <= 15:
    print("n elevado de pessoas")
else:
    print("n extremo de pessoas")