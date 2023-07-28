
print("STAR WAR NAME GENERATOR\n")

name = input("""Enter your first name, last name,
Mum's maiden name and the
city you were born in:\n""")

split = (name.split())
print("Your Star Wars name is " + f"{(split[0])[0:3] + (split[1])[0:2] + ' ' + (split[2])[0:2] + (split[3])[-2:]}".title())




