minute_price = 0.13 #float(input("Sisesta minuti hind:"))
hourly_price = 4.99 #float(input("Sisesta tunni hind:"))
daily_price = 27.89 #float(input("Sisesta päeva hind:"))
km_price = 0.22 #float(input("Sisesta km hind:"))
rental_duration = "10:30" # input("Sisesta rendi aeg formaadis hh:mm: ")
total_km = 100 #int(input("Enter total distance in km: "))
total_cost = 0

rental_duration_minutes = int(rental_duration[0:2]) * 60 + int(rental_duration[3:5])

days, remaining_minutes = divmod(rental_duration_minutes, 24 * 60)
total_cost += days * daily_price

hours, remaining_minutes = divmod(remaining_minutes, 60)
total_cost += min(hours * hourly_price, daily_price)
total_cost += min(remaining_minutes * minute_price, hourly_price)
total_cost += total_km * km_price

print(f"Rendi kogumaksus on: {total_cost}")