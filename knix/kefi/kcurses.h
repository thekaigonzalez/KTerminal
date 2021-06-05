#include <iostream>



void clear()
{
#if defined(unix)
    system("clear");
#elif defined(_WIN32)
    system("cls");
#elif defined(__MACH__)
    system("clear");
#endif
}