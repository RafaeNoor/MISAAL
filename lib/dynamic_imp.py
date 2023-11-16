import imp
import sys
from importlib.machinery import SourceFileLoader

# dynamic import
def dynamic_imp(name, class_name):

    # find_module() method is used
    # to find the module and return
    # its description and path
    try:
        fp, path, desc = imp.find_module(name)

    except ImportError:
        print ("module not found: " + name)

    try:
    # load_modules loads the module
    # dynamically ans takes the filepath
    # module and description as parameter
        example_package = imp.load_module(name, fp,
                                          path, desc)

    except Exception as e:
        print(e)

    try:
        myclass = imp.load_module("% s.% s" % (name,
                                               class_name),
                                  fp, path, desc)

    except Exception as e:
        print(e)

    return example_package, myclass



class Dimport:
    def __init__(self, module_name, class_name):
        #__import__ method used
        # to fetch module
        module =  SourceFileLoader(class_name, module_name).load_module() #__import__(module_name)

        # getting attribute by
        # getattr() method
        my_class = getattr(module, class_name)
        self.imported = my_class



