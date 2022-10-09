def no_return():
    print('I am about to raise an exception')
    raise Exception('This is always raised')
    print('This line never be execute')
    return "I won't be returned"

try:
    no_return()
except:
    print('I caught an exception')
print('executed after the exception')