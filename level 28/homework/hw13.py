odd_numbers = [i for i in range(30, 51) if i % 2 != 0]
smallest_three = sorted(odd_numbers)[:3]
print("Sum of smallest three elements:", sum(smallest_three))