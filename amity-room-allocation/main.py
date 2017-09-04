import argparse
import inspect
import six


class MyArgParseMeta(type):

    def __new__(cls, name, bases, attrs):
        super_new = super(MyArgParseMeta, cls).__new__
        # Also ensure initialization is only performed for subclasses of MyArgParser
        # (excluding MyArgParser class itself).

        parents = [b for b in bases if isinstance(b, MyArgParseMeta)]
        if not parents:
            return super_new(cls, name, bases, attrs)

        # Create the class.
        module = attrs.pop('__module__')
        new_class = super_new(cls, name, bases, {'__module__': module})

        return new_class

    def add_to_class(cls, name, value):
        # We should call the contribute_to_class method only if it's bound
        if not inspect.isclass(value) and hasattr(value, 'contribute_to_class'):
            value.contribute_to_class(cls, name)
        else:
            setattr(cls, name, value)


class MyArgParse(six.with_metaclass(MyArgParseMeta)):
    def __init__(self):
        super(MyArgParse, self).__init__()
        self.parser = argparse.ArgumentParser(description="calculate X to the power of Y")
        self.group = self.parser.add_mutually_exclusive_group()
        self.group.add_argument('-v', '--verbose', action="store_true", help='increase output verbosity')
        self.group.add_argument('-q', '--quite', action="store_true", help='dont display extra ')
        self.parser.add_argument('X', help='the base', type=int)
        self.parser.add_argument('Y', help='the exponential', type=int)

    def excec(self):
        args = self.parser.parse_args()
        answer = args.X ** args.Y

        if args.quite:
            print('{}'.format(answer))

        elif args.verbose:
            print('{} to the power of {} equals {}'.format(args.X, args.Y, answer))

        else:
            print("Running {}^{} == {}".format(args.X, args.Y, answer))



# parser = argparse.ArgumentParser(description="calculate X to the power of Y")
# group = parser.add_mutually_exclusive_group()
# parser.add_argument('X', help='the base', type=int)
# parser.add_argument('Y', help='the exponential', type=int)
# group.add_argument('-v', '--verbose', action="store_true", help='increase output verbosity')
# group.add_argument('-q', '--quite', action="store_true", help='dont display extra ')
#
# args = parser.parse_args()
# answer = args.X ** args.Y
#
# if args.quite:
#     print('{}'.format(answer))
#
# elif args.verbose:
#     print('{} to the power of {} equals {}'.format(args.X, args.Y, answer))
#
# else:
#     print("Running {}^{} == {}".format(args.X, args.Y, answer))

class ArgParseTutorial(MyArgParse):
    pass


obj = ArgParseTutorial()
obj.excec()