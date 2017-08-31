# properties
class PropertyClass(object):
    def __init__(self, name):
        self.name = name

    @property
    def my_name(self):
        return self.name

    @my_name.setter
    def my_name(self, value):
        self.name = value

    @my_name.deleter
    def my_name(self):
        del self.name

# -------------------------------------- #


# __getattribute__ and __getattr__ methods
class GetAttrsMethods(object):
    def __init__(self, name):
        self.name = name

    def __getattribute__(self, item):
        if item == 'alias':
            return self.__class__.__name__.lower()

        else:
            return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        key = value

