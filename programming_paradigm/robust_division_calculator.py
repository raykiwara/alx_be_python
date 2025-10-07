def safe_divide(numerator, denominator):
    try:
        res = float(numerator) / float(denominator)
        return f"The result of thr division is {res}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
