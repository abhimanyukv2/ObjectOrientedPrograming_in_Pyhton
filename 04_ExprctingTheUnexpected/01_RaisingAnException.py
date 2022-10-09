class EvenOnly(list):
    def append(self, integer):
        if not isinstance(integer, int):
            raise TypeError('Only Integer can be added')
        if integer%2:
            raise ValueError('Only even number can be added')
        super().append(integer)


if __name__ == "__main__":
    e = EvenOnly()
    e.append('a String')
    f = EvenOnly()
    f.append(3)
    g = EvenOnly()
    g.append(2)