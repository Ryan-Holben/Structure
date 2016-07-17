import structure

def b():
    print 'in b()'

def a():
    print 'in a()'
    b()

def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        if n%2 == 0:
            even()
        else:
            odd()
        return fib(n-1) + fib(n-2)

def even():
    return

def odd():
    return even()

class test():
    def __init__(self):
        pass
    def class_func(self, n):
        return fib(n)


def main():
    s = structure.Structure()
    s.setMaxDepth(None)
    s.setLogFile("test.log")
    s.beginTrace()

    print fib(3)

    testclass_instance = test()
    testclass_instance.class_func(4)

if __name__ == "__main__":
    main()
