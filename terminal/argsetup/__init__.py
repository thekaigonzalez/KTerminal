import curses
from typing import List
from terminal.io import stdscr


class ArgumentPasser:
    def __init__(self, argarray: List[str]):
        self.args = argarray
        self.optlist = []
        self.desc = ""
        self.datalist = []
        self.execlist = []

        self.variables = []

        self.varnames = []
        self.vardatas = []

    def isoption(self, pos):
        if self.args[pos].startswith("-"):
            return True
        else:
            return False

    def echo(self, option: str, var: List[str], output: str, callback, position: int = 0):
        if self.args[position].startswith("-"):
            stdscr.addstr(output)
        else:
            callback()

    def bindonce(self, option: str, func):
        self.optlist.append("[-" + option + " ...] ")
        self.datalist += "-" + option
        self.datalist.append(option)
        self.execlist.append(func)
        for i in self.args:
            if i == "-" + option:
                func(self.args, self)

    def begin(self):
        abc = 0
        for i in self.args:
            if i == self.datalist[abc]:
                self.execlist[abc]()

            abc += 1

    def setDesc(self, dec):
        self.desc = dec

    def extract(self, stpos: int):
        a = stpos
        for variab in self.args:
            if variab.startswith("-"):
                if variab[1:len(variab)] not in self.optlist:
                    variablevalue = self.args[a + 1]
                    self.vardatas.append(variablevalue)
                    self.variables.append(self.args[a][1:len(variab)] + "=" + variablevalue)
                else:
                    break
            a += 1

    def parseconfig_getpos(self, nameOrValue: str, stopPos: int = 0, ):
        posis = 0
        for e in self.variables:

            variablename = e[0:e.find("=")]
            variablevalue = e[e.find("=") + 1:len(e)]
            if posis == stopPos:
                if nameOrValue == "NAME":
                    return variablename
                elif nameOrValue == "VALUE":
                    return variablevalue
                posis += 1

    def setbindv(self, name: str, function, position=0):
        if self.args[position].startswith("-"):
            if self.args[position][1:len(self.args[position])]:
                var = self.args[position + 1]
                self.variables.append(name + "=" + var)
                self.varnames.append(self.args[position][1:len(self.args[position])])
                self.vardatas.append(var)
                function(self.variables, self.varnames, self.vardatas)

    def sendhelp(self):

        stdscr.addstr(''.join(self.optlist))
        stdscr.addstr("\n\n" + self.desc + "\n")
