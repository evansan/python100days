money = 1000

for year in range(10):
    money = money * 1.05
    print("year", year + 1, "is", round(money,2))