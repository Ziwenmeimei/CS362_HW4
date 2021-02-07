def calculate_list(x):
    try:
        return sum(x) / len(x)
    except TypeError:
        return "Type Error"
    except ZeroDivisionError:
        return "Empty List"