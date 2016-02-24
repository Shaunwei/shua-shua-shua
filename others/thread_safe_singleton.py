import threading


class Singleton:
    __singleton_instance = None
    __singleton_lock = threading.Lock()

    @classmethod
    def instance(cls):
        if not cls.__singleton_instance:
            with cls.__singleton_lock:
                if not cls.__singleton_instance:
                    cls.__singleton_instance = cls()
        return cls.__singleton_instance


class A(Singleton):
    pass

class B(Singleton):
    pass

if __name__ == '__main__':
    a0, a1 = A.instance(), A.instance()
    b0, b1 = B.instance(), B.instance()

    assert a0 is a1
    assert b0 is b1
    assert a0 is not b0

    print('a:  %s\na2: %s' % (a0, a1))
    print('b:  %s\nb2: %s' % (b0, b1))
