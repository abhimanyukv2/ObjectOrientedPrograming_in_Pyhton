class Inventory:
    def lock(self, item_type):
        '''Select the type of item that is going to be manipulated.
        This method wil lock the item so nobody else can manipulate
        the inventory until it's returned. This prevents selling 
        the same item to two different customers.'''
        pass

    def unlock(self, item_type):
        '''Release the given type so that other customer can access it.'''
        pass

    def purchase(self, item_type):
        '''If the item is not locked, raise an excepton. If the item_type
        does not exist, raise an exception. If the item is currently out of stock,
        raise an exception. if the item is available, subtaract one item and
        return the number of items left.'''
        pass

item_type = 'widget'
inv = Inventory()
inv.lock(item_type)
try:
    num_left(inv.purchase(item_type))
except InvalidItemType:
    print("Sorry we don't sale {}".format(item_type))
except outOfStock:
    print('Sorry, That item is out of stock.')
else:
    print('Purchase complete. There are {} {}s left'.format(num_left,item_type))
finally:
    inv.unlock(item_type)