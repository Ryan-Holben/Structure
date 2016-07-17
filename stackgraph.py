"""
    Loads a log of a program's call stack activity and builds a graph.
"""
from graph_tool.all import Graph
from functionwrapper import FunctionWrapper

class StackGraph(object):
    def __init__(self):
        self.g = None

    def load(self, filename):
        self.g = Graph()
        f = open(filename, "rb")
        for line in f:
            # Skip any informational lines
            if "*" in line:
                continue
            # Extract a call stack snapshot
            words = line.split()
            time = words[0][2:]
            depth = words[1][2:]
            stack = [FunctionWrapper(instring=item) for item in words[2].split("->")]
            # print words[0][2:], words[1][2:], [str(x) for x in stack]

            # Add the top 2 functions to the graph if necessary

            # Add the edge if necessary, and then add data to it

        f.close()
