# coding: utf-8
import importlib, codeg
modl = importlib.import_module('mod1')
code = codeg.gen_code(modl)
code
thefile = open('views.py','w')
for item in code:
    thefile.write(item)
thefile.close()

codeg.gen_sec_models()

