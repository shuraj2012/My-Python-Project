def print_pyramid(rows):
    for i in range(rows):
        print(" " * (rows - i - 1) + "*" * (2 * i + 1))

# Example usage
rows = 5
print_pyramid(rows = 20)
