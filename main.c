#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
#include <sys/ioctl.h>

int main()
{
    pid_t p = fork();
    if (!p){

        char * meow[] = {"/bin/python","/usr/local/share/shellMIP/main.py"};
        execvp(meow[0],meow);
        exit(EXIT_FAILURE);
    }
    else wait(0);
}