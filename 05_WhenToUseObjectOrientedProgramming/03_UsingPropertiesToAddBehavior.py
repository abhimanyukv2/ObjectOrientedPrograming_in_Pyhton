class Color:
    '''In Python we can access the attributes directly.'''
    def __init__(self, rgb_value, name):
        self.rgb_value = rgb_value
        self._name = name

    def _set_name(self, name):
        if not name:
            raise Exception("Invalid Name")
        self._name = name

    def _get_name(self):
        return self._name

    '''We use  PROPERTY keybord to make method look like a class attribute.'''
    name = property(_get_name, _set_name)

if __name__ == "__main__":
    c = Color('#0000ff', 'bright red')
    print(c.name)
    c.name = 'red'
    print(c.name)
    c.name = ''