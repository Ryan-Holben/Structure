"""
    Loads a log of a program's call stack activity and builds a graph.
"""
import stackgraph

G = stackgraph.StackGraph()
G.load("test.log")
G.display()
