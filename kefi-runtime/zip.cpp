//
// Created by kai on 6/4/21.
//

#include <zip.h>
#include <string>
#include <iostream>

zip* open_file_t(const std::string& name)
{
    int a = 0;
    return zip_open(name.c_str(), ZIP_CREATE, &a);
}
