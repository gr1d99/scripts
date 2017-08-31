# flatten a list
class Flatten(object):
    """A simple class that flattens a list of any kind and returns all items in one list"""
    def __init__(self, target_list):
        if not isinstance(target_list, list):
            raise TypeError('expected argument of type List')

        self.target_list = target_list
        self.new_list = []

    def start(self):
        for item in self.target_list:
            self.flatten_item(item)

    def flatten_item(self, item):
        if isinstance(item, list):
            for i in item:
                self.flatten_item(i)
        else:
            self.new_list.append(item)


# usage
my_list = [
    [1, 2], 3,
    [4, [5, [[6]]]]
]

obj = Flatten(my_list)
obj.start()
print(obj.new_list)

print globals()
