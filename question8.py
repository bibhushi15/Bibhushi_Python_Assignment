password = input("Enter your password: ")

letter_count = 0
number_count = 0
special_count = 0

special_symbols = "@#$%&"

for ch in password:
    if ch.isalpha():
        letter_count += 1
    elif ch.isdigit():
        number_count += 1
    elif ch in special_symbols:
        special_count += 1

if len(password) >= 8 and letter_count > 0 and number_count > 0 and special_count > 0:
    print("Strong password")
elif len(password) >= 6 and letter_count > 0 and number_count > 0:
    print("Moderate password")
else:
    print("Weak password")