def print_tree(height):
    for i in range(1, height + 1):
        spaces = " " * (height - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars)

# Adjust the height based on your preference
tree_height = 5
print_tree(tree_height)
