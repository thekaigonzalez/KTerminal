//
// Created by kai on 6/4/21.
//

//
// Created by kai on 6/4/21.
//
#include <iostream>
#include <vector>

extern "C" void begin(std::vector<std::string>&argv)
{
    argv.erase(argv.cbegin());
    for (const auto& I : argv)
    {
        std::cout << I << " " << std::endl;
    }
}