"""
    Loads a log of a program's call stack activity and builds a graph.
"""
from graph_tool.all     import Graph, graph_draw, sfdp_layout
from functionwrapper    import FunctionWrapper
from callswrapper       import CallList

class StackGraph(object):
    def __init__(self):
        self.g = None

    def load(self, filename):
        # Initialize the graph
        self.g = Graph()
        # Each node will store a FunctionWrapper() class instance.
        self.g.vertex_properties["functions"] = self.g.new_vertex_property("object")
        self.g.vertex_properties["display"] = self.g.new_vertex_property("string")
        # Each edge will store a [ ..tbd.. ] .
        self.g.edge_properties["calls"] = self.g.new_edge_property("object")

        # Load the log file and build the graph
        i = 0
        f = open(filename, "rb")
        for line in f:
            i += 1
            try:
                # Skip any informational lines
                if "*" in line:     continue
                # Extract a call stack snapshot
                words = line.split()
                time = words[0][2:]
                depth = words[1][2:]
                stack = [FunctionWrapper(instring=item) for item in words[2].split("->")]

                # Add the top 2 functions to the graph, if necessary.  Format: f1()->f2()
                f1, f2 = stack[-2], stack[-1]
                v1, v2 = None, None
                    # Search for the vertices
                for v in self.g.vertices():
                    if self.g.vp.functions[v] == f1:    v1 = v
                    if self.g.vp.functions[v] == f2:    v2 = v
                    if v1 != None and v2 != None:       break

                    # Add new vertices if needed
                if v1 == None:
                    v1 = self.g.add_vertex()
                    self.g.vp.functions[v1] = f1
                    self.g.vp.display[v1] = f1.graphDisplayString()
                if v2 == None:
                    v2 = self.g.add_vertex()
                    self.g.vp.functions[v2] = f2
                    self.g.vp.display[v2] = f2.graphDisplayString()

                # Add the edge if necessary, and then add data to it
                if not self.g.edge(v1, v2):
                    e = self.g.add_edge(v1, v2)
                    self.g.ep.calls[e] = CallList(v1, v2)

                self.g.ep.calls[e].addCall(time, depth)
            except Exception as e:
                print "Exception on line", i, ":", e
                print [str(x) for x in stack]
                exit()

        f.close()

    def display(self):
        pos = sfdp_layout(self.g)
        graph_draw(self.g, pos=pos, vertex_size = 50, vertex_text=self.g.vp.display, vertex_font_size=12, vertex_text_position=-1, edge_pen_width=3)   #self.g.vertex_index)
