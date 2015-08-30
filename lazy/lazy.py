class LazyRef(object):
    def __init__(self, fget):
        self.fget = fget
        self.name = fget.__name__

    def __get__(self, instance, cls):
        val = self.fget(instance)
        instance.__dict__[self.name] = val
        return val


class LazyProperty(object):
    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        if doc is None and fget is not None and hasattr(fget, '__doc__'):
            doc = fget.__doc__
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        self.__doc__ = doc
        self.value = None 

    def __get__(self, instance, cls):
        if self.fget is None:
            raise AttributeError('unreadable attribute')
        if not self.value:
            self.value = self.fget(instance)
        return self.value

    def __set__(self, instance, value):
        if self.fset is None:
            raise AttributeError('can\'t set attribute')
        self.value = None
        return self.fset(instance, value)

    def __delete__(self, instance):
        if self.fdel is None:
            raise AttributeError('can\'t delete attribute')
        self.value = None
        return self.fdel(instance)

    def getter(self, func):
        self.fget = func
        return self

    def setter(self, func):
        self.fset = func
        return self

    def deleter(self, func):
        self.fdel = func
        return self

