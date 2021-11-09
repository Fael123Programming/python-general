"""
    Python is a compiled-interpreted language that uses bytecodes as an intermediate type of file after compilation
    processes. We can compare this process with Java's compilation process: CPython (Python standard interpreter)
    translates all source code (script) into a specific type of bytecode defined for Python; after compilation
    process the resulting code is then, read, interpreted and put into execution by CPython.
    There are variations of Python source code interpretation such as Jython (which stands for compiling Python source
    code into Java environment - JVM), IronPython (the same thing of Jython but to .NET environment).
"""


from py_compile import compile
compile("program.py")  # This function does what is automatically done when you put a Python file into execution.
# It calls CPython compilation process manually and generate (at new modifications) a __pycash__ module containing
# the compiled code.
# The file in __pycache__ module is named as program.cpython-38.pyc
# Talking about compilation and interpretation, the famous errors and exceptions can be mentioned here: errors are
# detected during compilation time and exceptions during interpretation. For example, if you forgot to write a colon
# after an if statement's conditional then, a SyntaxError will be thrown.
# if True or False
#    print("Inside it")
