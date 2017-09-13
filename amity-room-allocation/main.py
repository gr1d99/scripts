import inspect


class MyArgParseMeta(type):

    def __new__(mcs, name, bases, attrs):
        super_new = super(MyArgParseMeta, mcs).__new__
        # Also ensure initialization is only performed for subclasses of MyArgParser
        # (excluding MyArgParser class itself).

        parents = [b for b in bases if isinstance(b, MyArgParseMeta)]
        if not parents:
            return super_new(mcs, name, bases, attrs)

        # Create the class.
        module = attrs.pop('__module__')
        new_class = super_new(mcs, name, bases, {'__module__': module})

        return new_class

    def add_to_class(cls, name, value):
        # We should call the contribute_to_class method only if it's bound
        if not inspect.isclass(value) and hasattr(value, 'contribute_to_class'):
            value.contribute_to_class(cls, name)
        else:
            setattr(cls, name, value)
