print("30 Days down, what do you think?")
for i in range (1,11):
    answer = input(f"Day {i}\n")
    formatted = f"You think day {i} was"
    print(f"{formatted:^35}")
    print(f"{answer:^35}")
