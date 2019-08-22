def divide_numbers(numerator, denominator) -> int:
    """For this exercise you can assume numerator and denominator are of type
       int/str/float.
       Try to convert numerator and denominator to int types, if that raises a
       ValueError reraise it. Following do the division and return the result.
       However if denominator is 0 catch the corresponding exception Python
       throws (cannot divide by 0), and return 0"""
    try:
        numerator = int(numerator)
        denominator = int(denominator)
        try:
            divide = numerator / denominator
            return divide
        except ZeroDivisionError:
            print("cannot divide by 0")
            return 0
    except ValueError:
        raise


print(divide_numbers(1,4))
