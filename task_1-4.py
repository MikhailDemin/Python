num = int(input('enter any number'))
max_digit = 0
while num > 0:
    digit = num % 10
    if digit > max_digit:
        max_digit = digit
    num //= 10
print(max_digit)