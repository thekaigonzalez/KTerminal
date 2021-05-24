import curses
import importlib
def Evaluatecommand(command: str, workingdir: str, SCREEN, arrayTUse):

    """
    Evaluates a command by using the same method as KTerminal
    :param command: 
    :return: 
    """
    ktA = command.split()
    ktC = ktA.pop(0)
    m = importlib.import_module("usr.bin." + ktC)
    m.main(SCREEN, ktA, len(ktA), arrayTUse)
    try:
        m.ROOT_PERM = True
    except ImportError:
        SCREEN.addstr("")