Lazy
====

Lazy contains two descriptors; LazyProperty and LazyRef.
These are meant to be used together property attributes that normally take a long time
to calculate.
The idea is that you only wanna calculate this value once, instead of each time
you look it up, so the second time you lookup it up it will return its value
right away.

For more documentation about properties check out `pythons property
documentation 
<https://docs.python.org/2/library/functions.html#property>`_.

LazyProperty
------------

LazyProperty works just like pythons built-in property, except for one thing,
LazyProperty stores its value inside the property after the first lookup. 
Therefore the other lookups will return right away. LazyPropery also supports 
setter and deleter just like the builtin property. When you use a setter to 
reasign a value the property will set its value to None, the same when you use 
a deleter.

LazyRef
-------

LazyRef works almost the same way as LazyProperty, except this is meant to be
a lazy reference to an attribute. This can be used for variables that you don't 
want to hide away. When called the first time, it will calculate its value and 
store it in the instances' dictionary  with the same name so the other lookups 
will find the value in the instances' dictionary instead and return much
faster.

Usage
-----

LazyProperty

.. code:: python
    
    import time
    from lazy import LazyProperty

    class SomeClass(object):
        def __init__(self, n):
            self._n = n

        @LazyProperty
        def x(self):
            """x documentation ..."""
            time.sleep(3)
            return self._n*10

        @x.setter
        def x(self, value):
            self._n = value

        @x.deleter
        def x(self):
            del self.n


    s = SomeClass(3)
    print(s.x) # takes time
    print(s.x) # returns right away

    s.x = 5
    del s.x


Can also be used this way

.. code:: python
    
    
    import time
    from lazy import LazyProperty

    class SomeClass(object)
        def __init__(self, n):
            self._n = n

        def get_x(self):
            time.sleep(3)
            return self._n*10

        def set_x(self, value):
            self._n = value

        def del_x(self):
            del self.n

        x = LazyProperty(fget=get_x, fset=set_x, fdel=del_x, doc='x documentation')


LazyRef

.. code:: python

    import time
    from lazy import LazyRef

    class SomeClass(object):
        def __init__(self, n):
            self.n = n

        @LazyRef
        def x(self):
            time.sleep(3)
            return self.n*10


    s = SomeClass(3)
    print(s.x) # takes time
    # Now x is stored together its value in s' instance dictionary
    print(s.x) # returns right away

