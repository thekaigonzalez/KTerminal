import importlib as imp



def require(modname):
    return imp.import_module(modname)