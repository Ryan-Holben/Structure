"""
    Loads a log of a program's call stack activity and builds a graph.
"""
from graph_tool.all import Graph

class StackGraph(object):
    def __init__(self):
        self.g = None

    def load(self, filename):
        self.g = Graph()
        f = open(filename, "rb")
        for line in f:
            words = line.split()
            if words[0][0] == "*":
                continue
            time = words[0][2:]
            depth = words[1][2:]
            rawstack = words[2].split("->")
            # stack = 
            print words[0][2:], words[1][2:], words[2].split("->")
        f.close()
