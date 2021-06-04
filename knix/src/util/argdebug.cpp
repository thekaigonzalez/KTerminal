//
// Created by kai on 6/4/21.
//
#include <iostream>
#include <vector>

extern "C" void begin(const std::vector<std::string>&argv)
{
    for (const auto& arg : argv)
    {
        std::cout << arg << std::endl;
    }
}