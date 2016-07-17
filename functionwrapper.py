

class FunctionWrapper(object):
    def __init__(self, filename=None, classname=None, funcname=None, instring=None):
        if instring:
            self.fromstring(instring)
        else:
            self.filename, self.classname, self.funcname = filename, classname, funcname

    def __str__(self):
        return "[" + self.filename + "," + ("None" if self.classname == None else self.classname) + "," + self.funcname + "]"

    def fromstring(self, string):
        """String format [a,b,c]"""
        words = string[1:-1].split(",")
        # print words
        self.filename = words[0]
        self.classname = None if words[1] == "None" else words[1]
        self.funcname = words[2]
