import os, sys, inspect
import cgen



class_list = []

def get_klass(module):
   for name in dir(module):
        obj = getattr(module,name)
        if inspect.isclass(obj):
            print(obj.__name__)
            class_list.append(obj.__name__)


