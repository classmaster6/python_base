def divide(a, b):
    try:
        return a / b
    except:  # except ZeroDivisionError:
        return 0.0

print(divide(1, 0))


print(0/0)