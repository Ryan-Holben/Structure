

class CallList(object):
    def __init__(self, v1=None, v2=None):
        self.v1, self.v2, self.calls = v1, v2, []

    def attach(self, v1, v2):
        """Inform this CallList which to functions/vertices it is going between."""
        self.v1, self.v2 = v1, v2

    def addCall(self, time, depth):
        self.calls.append( [time, depth] )
