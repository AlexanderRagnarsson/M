def is_float(str):
    try:
        float(str)
        return True
    except ValueError:
        return False


print(is_float('3.45'))
print(is_float('3e4'))
print(is_float('abc'))
print(is_float('4'))
print(is_float('.5'))