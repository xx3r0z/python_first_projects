import FreeSimpleGUI as fsg
import inspect

methods = [name for name, obj in inspect.getmembers(fsg) if inspect.isclass(obj) or inspect.isfunction(obj)]
print(methods)
