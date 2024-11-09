#  Berilgan raqamlarni teskarichasiga yozib ekranga chiqarish
#  Misol uchun 154, 2024  sonini

def print_digits(num: int) -> None:
    if num == 0:
        print("0")
        return

    while num != 0:
        digit = num % 10
        print(digit, end=" ")
        num //= 10
		# 154 % 10 = 4;
		# 154 / 10 = 15;
		# 15 % 10 = 5;

		# 15 / 10 = 1;
		# 1 % 10 = 1;
		# 1 / 10 = 1; 
