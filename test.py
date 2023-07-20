import math

def calculate_combinations(n):
    total_combinations = 0
    for r in range(2, n + 1):
        combinations = math.comb(n, r)
        total_combinations += combinations
    return total_combinations

# Example usage
total_combinations = calculate_combinations(20)
print("Total combinations:", total_combinations)
