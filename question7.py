numbers = []

count = int(input("How many numbers do you want to enter?"))

for i in range(count):
    num = int(input("Enter a number: "))
    numbers.append(num)

for num in numbers:
    if num > 50:
        break

    if num % 5 == 0:
        continue

    print(num)