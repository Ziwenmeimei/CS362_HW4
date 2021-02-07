def calculate_cube(side):
    try:
        return side*side*side
    except TypeError:
        return "Type Error"