value = 0

def calc(number1, number2):
    if number2 == 0:
        raise ValueError("Ne nado 0!")


try:
    calc(1, 0)
except ZeroDivisionError as exc:
    print("Dont delete by zero!")
except ValueError as exc:
    print ("User-defined error: {}".format(str(exc)))
except Exception as exc:
    print ("Unknown error: {}".format(str(exc)))
finally:
    print(value)
print ("Thank you!")