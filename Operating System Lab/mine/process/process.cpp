#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>
#include <stdlib.h>
int main() {
    pid_t pid;
    printf("Parent PID: %d\n", getpid());
    pid = fork();
    printf("Come back  %d \n", pid);
    //pid = fork();
    if (pid < 0) {
        printf("Fork failed\n");
        return 1;
    }
    if(pid == 0) {
        // Child process
        printf("\nChild Process\n");
        printf("Child PID: %d\n", getpid());
        printf("Parent PID of Child: %d\n", getppid());
        // printf("%d \n", pid);
        printf("Child is executing...\n");

        printf("Child process is terminating...\n");
        exit(0);
    }
    else {
        // Parent process
        printf("\nParent Process\n");
        printf("Parent PID: %d\n", getpid());
        printf("Child PID: %d\n", pid);
        printf("Parent is executing...\n");
        // printf("%d \n", pid);

        wait(NULL);
        printf("Child has terminated.\n");
        printf("Parent process is terminating...\n");
    }

    
    return 0;
}