total = 0
count = 0


while True:
    try:
        price = float(input("price (0 to stop):"))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue


    if price == 0:
        break


        total += price
        count += 1
        

    if count > 0:
        average = total / count
        print(f"Items: (count)")
        print(f)






