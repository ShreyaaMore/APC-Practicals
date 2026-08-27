morning = {"Alice", "Bob", "Charlie", "David"}
afternoon = {"Charlie", "David", "Eve", "Frank"}
both = morning & afternoon
only_morning = morning - afternoon
only_afternoon = afternoon - morning
at_least_one = morning | afternoon
print("Students in morning:", morning)
print("Students in afternoon:", afternoon)
print("Present in both sessions:", both)
print("Present only in morning:", only_morning)
print("Present only in afternoon:", only_afternoon)
print("Present in at least one session:", at_least_one)
