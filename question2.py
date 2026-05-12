name = input ("Enter your Full Name:")

space = name.find(" ")

first_initial = name[0]
last_initial = name[space+1]
print(f"Your initials are: {first_initial.upper()}.{last_initial.upper()}")