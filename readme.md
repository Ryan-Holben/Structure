# Structure

An experiment in graphing the control flow of a Python program.  Currently does not support multithreaded applications.

### Challenges
* Identifying class methods' class names

### Usage

    import structure
    s = structure.Structure()
    s.setDepth(depth = 3)
    s.setLocal(True)
    s.setSaveFile("output.dat")
    s.beginTrace()

### Parameters
* int Depth
        Specify how deep into the stack we will record.  By limiting this quantity, we can avoid a lot of "noise."
* bool Local
        If set to True, we will not follow the stack into source files outside of the project directory.

# Storing the results

Results will be stored in a directed graph, where each node represents a function, and an arrow on an edge shows the direction of function calls.

An edge may contain:
* Timestamp of each call
* Number of calls

A node may contain:
* Total number of calls
* Elapsed runtime
        * A breakdown including time spent waiting for child functions to return

### Advanced features

* An interactive web-based graph explorer
* On the fly changing of depth that we display
* Playback of program's run by using timestamp data
