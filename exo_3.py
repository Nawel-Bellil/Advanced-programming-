def calculateDiscount():
    total_amount = float(input("Total amount: "))
    num_items = int(input("Number of items: "))
    day_of_week = input("Day of the week: ").strip().lower()

    discount = 0

    if day_of_week in ["monday", "tuesday", "wednesday", "thursday", "friday"]:
        discount += 10
    elif day_of_week in ["saturday", "sunday"]:
        discount += 20

    if num_items > 5:
        discount += 5

    total_price = total_amount * (1 - discount / 100)

    print(f"Total price after discount: {total_price:.2f} dinars")

calculateDiscount()
