'''Here's our previous silly class rewritten to use property as a decorator.'''
class Silly:
    @property
    def silly(self):
        "This is the silly property"
        print("You are getting silly")
        return self._silly

    @silly.setter
    def silly(self, value):
        print("You are making silly {}".format(value))
        self._silly = value

    @silly.deleter
    def silly(self):
        print("Whoah, yu killed silly!")
        del self._silly