def divide_with_excepton(number, divisior):
    try:
        print("{} / {} = {}".format(
            number, divisior, number/divisior * 1.0
        ))
    except ZeroDivisionError:
        print("You can't divide by zero")

def divide_with_if(number, divisor):
    if divisor == 0:
        print("You can't divide by Zero")
    else:
        print("{} / {} = {}".format(
            number, divisor, number/divisor * 1.0
        ))