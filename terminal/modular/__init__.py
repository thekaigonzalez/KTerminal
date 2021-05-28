import importlib as imp



def arch_require(modname):
    return imp.import_module(modname)