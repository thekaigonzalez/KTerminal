//
// Created by kai on 6/4/21.
//
#include <iostream>
#include <vector>
#include "../../kefi/kcurses.h"
extern "C" void curses_init(const std::vector<std::string>&argv)
{
    clear();
}