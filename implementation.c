// noterman implementation in C

#include <stdlib.h>
#include <stdio.h>

const usage = "\nUSAGE:\n\nnoterman add\nnoterman change [id]\nnotermna delete [id]\n\n";

int main(int argc, char *argv[]) {
    if(argc==2) {
        if(argv[1]=="--add") {}
        else {
            printf(usage);
            return 1;
        }
    }

    else if(argc==3) {
        if(argv[1]=="--change") {}
        else if(argv[1]=="--delete") {}
        else {
            printf(usage);
            return 1;
        }
    }

    else {
        printf(usage);
        return 1;
    }
}
