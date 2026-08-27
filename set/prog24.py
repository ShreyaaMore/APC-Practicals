day1_visitors = {101, 102, 103, 104, 105}
day2_visitors = {104, 105, 106, 107, 108}
unique_all = day1_visitors | day2_visitors
returning = day1_visitors & day2_visitors
only_day1 = day1_visitors - day2_visitors
only_day2 = day2_visitors - day1_visitors

print("Day 1 Visitors:", day1_visitors)
print("Day 2 Visitors:", day2_visitors)
print("Unique visitors across both days:", unique_all)
print("Returning visitors:", returning)
print("Visitors only on first day:", only_day1)
print("Visitors only on second day:", only_day2)

electronics = {"Smartwatch", "Laptop", "Fitness Band", "Headphones"}
fitness_items = {"Fitness Band", "Yoga Mat", "Dumbbells", "Smartwatch"}
both_categories = electronics.intersection(fitness_items)
print("Products in both categories:", both_categories)
