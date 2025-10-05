def safe_divide(numerator, denominator):
    try:
        return (float(numerator) / float(denominator))
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Please enter numeric values only.")
    #inally:
     #  return res

