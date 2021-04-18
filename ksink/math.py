#Example: minmax(1, 2, 10) == 2
def minmax(value, min_value, max_value):
    return min(max(value, min_value), max_value)
