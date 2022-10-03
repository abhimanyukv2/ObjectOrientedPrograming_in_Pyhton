'''Classes can be defined anywhere. They are typically
defined at the module level, but the can also be define
inside a function or method, like so:'''

def formate_string(string, formatter=None):
    '''Format a string using the formatter object, which is
    expected to have a format() method that accepts a string.'''

    class DefaultFormatter:
        '''Format a string in title case.'''
        def format(self,string):
            return str(string).title()
        
    if not formatter:
        formatter = DefaultFormatter()

    return formatter.format(string)

hello_string = "hello world, how are you today?"
print("input: " + hello_string)
print("output: " + formate_string(hello_string))