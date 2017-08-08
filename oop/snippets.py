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



