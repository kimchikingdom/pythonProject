print("숫자게임 시작합니다.")
number = 62

exact_num=input("Guess number 1 to 100")
print(exact_num)

guess = int(exact_num)

if guess== number:
    print("True")
else :
    print("False")