email = input("Enter your email address: ")

at = email.find("@")
domain = email[at + 1:len(email)]

print("Domain:", domain)