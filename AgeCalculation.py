def calculate_age(year, month, date):
    import datetime
    today = datetime.datetime.now().date()
    date_of_birth = datetime.date(year, month, date)
    age = int((today - date_of_birth).days / 365.25)
    print("Age is:", age, "years")


y = int(input("Enter the year: "))
m = int(input("Enter the month: "))
d = int(input("Enter the day: "))
calculate_age(y, m, d)
