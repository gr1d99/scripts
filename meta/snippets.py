import six


class CarGetter(object):
    def __init__(self, name):
        self._name = name

    def __call__(self, wrappedSelf):
        return getattr(wrappedSelf, self._name)


class CarSetter(object):
    def __init__(self, name):
        self._name = name

    def __call__(self, wrappedSelf, value):
        print "invalidate!"
        return setattr(wrappedSelf, self._name, value)


class CarMeta(type):
    def __new__(mcs, name, bases, attrs):
        super_new = super(CarMeta, mcs).__new__

        # Also ensure initialization is only performed for subclasses of Model
        # (excluding Car class itself).

        parents = [b for b in bases if isinstance(b, CarMeta)]
        if not parents:
            return super_new(mcs, name, bases, attrs)

        # Create the class.
        clsdict = {}
        module = attrs.pop('__module__')
        clsdict.update({'__module__': module})
        for name in attrs['_instanceVars']:
            attrs[name[1:]] = property(CarGetter(name), CarSetter(name))
        new_class = super_new(mcs, name, bases, {'__module__': module})

        return new_class


class Car(six.with_metaclass(CarMeta)):
    _instanceVars = ['_velocity']

    def __init__(self, initialVelocity):
        self._velocity = initialVelocity


class Corolla(Car):
    pass


class Toyota(Car):
    pass

class SpareParts(Corolla):
    pass


c = Corolla(10)
t = Toyota(2)
s = SpareParts(2)
c.velocity = 1
print c.velocity