import sys, atexit, logging
from time import clock

# See https://pymotw.com/2/sys/tracing.html for info on setting this stuff up!

from pprint import pprint
class Structure(object):
    def __init__(self, logfilename = None):
        self.ignore_functions = set(["write", "print", "_remove", "__exitHook", "_run_exitfuncs", "_exitfunc"])
        self.setLogFile(logfilename)
        self.max_depth = None

    def setMaxDepth(self, depth = None):
        self.max_depth = depth

    def setLogFile(self, logfilename = "structure.log"):
        self.logfilename = logfilename

    def __stackString(self, stack):
        return "->".join([x[0] + "." + x[1] + "()" if x[0] != None else x[1] + "()" for x in stack][::-1])
        # return "->".join([function + "()" for function in stack][::-1])

    def __buildStack(self, frame):
        f = frame
        stack = []
        while f != None:
            if "self" in f.f_locals:
                stack.append([f.f_locals["self"].__class__.__name__, f.f_code.co_name])
            else:
                stack.append([None, f.f_code.co_name])
            f = f.f_back
        return stack

    def __traceHook(self, frame, event, arg):
        # Convenient and fun fact: functions called by __traceHook won't activate another __traceHook!
        try:
            # Only accept function calls
            if event != 'call':
                return
            # Build the call stack, compute the stack depth
            stack = self.__buildStack(frame)
            depth = len(stack)
            # Skip if we are too deep into the call stack
            if self.max_depth and depth > self.max_depth:
                return
            # Skip any forbidden functions show up in the call stack
            if not self.ignore_functions.isdisjoint([x[1] for x in stack]):
                return
            # Display it
            self.log.info("t:" + str(clock()) + "\td:" + str(depth) + "\t" + self.__stackString(stack))

            return
        except Exception as e:
            # Probably should put some actual error handling here...
            print "TRACEHOOK EXCEPTION:", e

    def __exitHook(self):
        sys.settrace(None)

    def beginTrace(self):
        # Register the exit hook function
        atexit.register(self.__exitHook)
        # Activate the logger
        logging.basicConfig(format="%(message)s", filename=self.logfilename, filemode="w", level=logging.INFO)
        self.log = logging.getLogger(self.__class__.__name__ + ".logger")
        self.log.info("t:" + str(clock()) + "\t" + "*"*15 + "Starting Call Stack Logging" + "*"*15)
        # Activate the trace hook
        sys.settrace(self.__traceHook)
