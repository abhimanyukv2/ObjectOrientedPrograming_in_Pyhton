class Foo:
    '''property function itself can be used with decorator syntax
    to turn a get function into a property.'''
    @property   # foo = property(foo)
    def foo(self):
        return 'bar'

    '''we can specify a setter funtion for the new property.'''
    @foo.setter
    def foo(self, value):
        self._foo = value

    '''using the same name for the get and set method is not required,
    but is help group the multiple methods that create one property together.'''