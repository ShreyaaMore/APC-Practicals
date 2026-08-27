set1 = {1, 2, 3}
set2 = {4, 5, 6}
print("Set 1:", set1)
print("Set 2:", set2)
if set1.isdisjoint(set2):
    print("The sets have no elements in common.")
else:
    print("The sets have common elements.")
