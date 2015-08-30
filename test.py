import time
from lazy import LazyProperty, LazyRef


class SomeClass(object):
    def __init__(self, x):
        self._x = x

    @LazyProperty
    def x(self):
        time.sleep(3) # Simulates a time consuming calculation
        return self._x*10

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x


class SomeOtherClass(object):
    def __init__(self, n):
        self.n = n

    @LazyRef
    def x(self):
        time.sleep(3) # Simulates a time consuming calculation
        return self.n + 1

def print_results(var_name, value, time1, time2):
    unit1 = 'seconds' if time1 > 1 else 'milliseconds'
    unit2 = 'seconds' if time2 > 1 else 'milliseconds'

    time1 = time1 if time1 > 1 else time1*1000
    time2 = time2 if time2 > 1 else time2*1000
    
    time1 = '%.4f' % (time1)
    time2 = '%.4f' % (time2)

    print('{} returned {}'.format(var_name, value))
    print('first lookup took {} {}'.format(time1, unit1))
    print('second lookup took {} {}'.format(time2, unit2))


def run_lazy_property_test(s, var_name, return_val, new_val=None, delete=False):
    if delete:
        print('\ndeleting {}\n'.format(var_name))
        del s.x
        return
    if new_val:
        s.x = new_val
        print('\nassigned {} to {}\n'.format(var_name, new_val))
    
    start = time.time()
    x = s.x
    stop = time.time()
    time1 = stop-start
    
    start = time.time()    
    y = s.x
    stop = time.time()
    time2 = stop-start
    
    assert x == y
    assert s.x == return_val
    print_results(var_name, x, time1, time2)


def run_lazy_ref_test(s, var_name):
    
    print('instance dict contains {} before first lookup'.format(s.__dict__))
    start = time.time() 
    x = s.x
    stop = time.time()
    time1 = stop-start

    print('instance dict contains {} after lookup'.format(s.__dict__))
    start = time.time() 
    y = s.x
    stop = time.time()
    time2 = stop-start

    assert x == y

    print_results(var_name, x, time1, time2)


if __name__ == '__main__':
    s = SomeClass(3)
    print('Running lazy property tests\n')
    run_lazy_property_test(s, 's.x', 30)
    run_lazy_property_test(s, 's.x', 50,  new_val=5)
    run_lazy_property_test(s, 's.x', None, delete=True)

    s = SomeOtherClass(3)
    print('-----------\n\nRunning lazy ref test\n')
    run_lazy_ref_test(s, 's.x')







