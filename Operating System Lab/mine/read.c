#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>

int main() {
    int fd;
    char buffer[100];
    int bytesRead;

    fd = open("student.txt", O_RDONLY);

    if (fd == -1) {
        printf("Failed to open file.\n");
        return 1;
    }

    bytesRead = read(fd, buffer, sizeof(buffer) - 1);   

    if (bytesRead == -1) {
        printf("Failed to read file.\n");
        close(fd);
        return 1;
    }

    buffer[bytesRead] = '\0';

    printf("File Content:\n%s\n", buffer);

    close(fd);

    return 0;
}