//
// Created by kaigonzalez2 on 5/27/21.
//
#include <unistd.h>
#include <string.h>
#include <dlfcn.h>
#include <assert.h>

#include <dirent.h>
#include "primitive.h"


int main(int argc, char* argv[])
{
    printf("Creating a few configuration files...\n");
    FILE* fsck = fopen("./iso.cfg", "w");
    FILE* fs = fopen("./fs.cfg", "w");
    FILE* user = fopen("./iso.cfg", "w");
    FILE* inno = fopen("./inno.cfg", "w");
    FILE* setup = fopen("./setup.cfg", "w");

    fputs("valid=true", fs);
    fputs("checker=true\nusr=true\ndir=usr/clib", user);
    fputs("../", inno);
    fputs("INLINE=FALSE",setup);
    fputs("STD=10", fsck);


    fclose(fsck);
    fclose(user);
    fclose(fs);
    fclose(setup);
    fclose(inno);
    printf("done");


    return 1;


}
