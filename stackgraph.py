"""
    Loads a log of a program's call stack activity and builds a graph.
"""
from graph_tool.all import Graph
from functionwrapper import FunctionWrapper

class StackGraph(object):
    def __init__(self):
        self.g = None

    def load(self, filename):
        # Initialize the graph
        self.g = Graph()
        # Each node will store a FunctionWrapper() class instance.
        self.g.vertex_properties["functions"] = self.g.new_vertex_property("object")
        # Each edge will store a [ ..tbd.. ] .
        self.g.edge_properties["calls"] = self.g.new_edge_property("object")

        # Load the log file and build the graph
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

            # Add the top 2 functions to the graph, if necessary.  Format: f1()->f2()
            f1, f2 = stack[-2], stack[-1]
            v1, v2 = None, None
                # Search for the vertices
            for v in self.g.vertices():
                if self.g.vp.functions[v] == f1:
                    v1 = v
                    # print "Found", f1.funcname,
                if self.g.vp.functions[v] == f2:
                    v2 = v
                    # print "Found", f2.funcname,
                if v1 != None and v2 != None:
                    break

                # Add new vertices if needed
            if v1 == None:
                v1 = self.g.add_vertex()
                self.g.vp.functions[v1] = f1
                # print "Add", f1.funcname,
            if v2 == None:
                v2 = self.g.add_vertex()
                self.g.vp.functions[v2] = f2
                # print "Add", f2.funcname,
            # print ""

            # Add the edge if necessary, and then add data to it

        f.close()
        print len(list(self.g.vertices()))
        for v in self.g.vertices():
            print self.g.vp.functions[v]
