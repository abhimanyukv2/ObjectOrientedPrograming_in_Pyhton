import random
some_exceptions = [ValueError, TypeError, IndexError, None]

try:
    choice = random.choice(some_exceptions)
    print('raising {}'.format(choice))
    if choice:
        raise choice('An Error')
except ValueError:
    print('Caught a ValueError')
except TypeError:
    print('Caught a TypeError')
except Exception as e:
    print('Caught some other error: %s'%(e.__class__.__name__))

else:
    print('This code called if there is no exception')
finally:
    print('THis cleanup code is allways called')