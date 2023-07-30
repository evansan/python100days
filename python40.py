
name = input("what is your name")
birth = input("what is your date of birth")
phone = input("what is your phone number")
email = input("what is your email")
address = input("what is your address")

user = {"name": name, "birth": birth, "phone": phone, "email": email, "address": address}


print(f"""
Here's your contact card\n
Name: {user['name']}
Date of birth: {user['birth']}
Phone: {user['phone']}
Email: {user['email']}
Address: {user['address']}
""" )