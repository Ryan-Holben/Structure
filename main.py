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
        return fib(n-1) + fib(n-2)

class test():
    def __init__(self):
        pass
    def class_func(self, arg):
        return arg


def main():
    s = structure.Structure()
    s.setMaxDepth(None)
    s.setLogFile("test.log")
    s.beginTrace()

    print fib(5)

    testclass_instance = test()
    testclass_instance.class_func(4)

if __name__ == "__main__":
    main()
