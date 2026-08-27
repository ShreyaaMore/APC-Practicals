def analyze_list(l):
    min_val = min(l)
    max_val = max(l)
    total_sum = sum(l)
    avg_val = total_sum / len(l)
    return min_val, max_val, total_sum, avg_val

l = [15, 25, 3, 48, 92, 11]
minimum, maximum, total, avg = analyze_list(l)
print("Minimum:", minimum)
print("Maximum:", maximum)
print("Sum:", total)
print("Average:", avg)
