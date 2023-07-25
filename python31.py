def yellow(text):
        return "\033[33m" + text + "\033[0m"
def purple(text):
        return "\033[35m" + text + "\033[0m"
def green(text):
        return "\033[32m" + text + "\033[0m"
def default(text):
         return "\033[0m" + text + "\033[0m"

title = purple("=") + default("=") + green("=") + " Music App " + green("=") + default("=") + purple("=")
print (f"{title:^100}\n")
print("💿  Radio Gaga")
print(yellow(f"{'Queen':>9}\n\n"))
print(default("PREV"))
print(green(f"{'NEXT':>9}"))
print(purple(f"{'PAUSE':>15}\n\n\n\n"))

print(f"{'WELCOME TO':^100}")
print(green(f"{'--   ARMBOOK --':^100}\n"))
print(f"""
{'Definitely not a rip':>50}

{'off of a certain other':>50}

{'social networking site.':>50}
\n""")


print(purple(f"{'Honest':^100}\n"))
print(default(f"{'Username:':^100}"))
print(default(f"{'Password:':^100}"))