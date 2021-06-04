//
// Created by kai on 6/4/21.
//
#include <iostream>
#include <fstream>
#include <dlfcn.h>
#include <sstream>
#include <vector>

int main(int argc, char**argv)
{
    while (true) {
        std::cout << "(bash) ";
        std::string string;
        getline(std::cin, string);
        std::stringstream STRSTREAM;
        STRSTREAM << string;
        std::string argument;
        std::vector<std::string> ARGUMENTS{};
        while (getline(STRSTREAM, argument, ' ')) {
            ARGUMENTS.push_back(argument);
        }
        if (ARGUMENTS[0] == "exit")
        {
            abort();
        }
        else {
            typedef void (*command_t)(const std::vector<std::string> &ArgumentArray);
            std::ifstream ifile("./knix/usr/bin/" + ARGUMENTS[0]);
            if (!ifile) {
                std::cout << ARGUMENTS[0] + ": command not found\n";
            } else {
                void *lib = dlopen(("./knix/usr/bin/" + ARGUMENTS[0]).c_str(), RTLD_LAZY);
                auto command = (command_t) dlsym(lib, "begin");
                command(ARGUMENTS);
            }
        }
    }
}