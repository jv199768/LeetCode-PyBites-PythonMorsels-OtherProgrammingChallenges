#include <stdio.h>
#include <string.h>

#define MAX_LINE_LENGTH 1024

int main(int argc, char *argv[]) {
    if (argc < 3) {
        printf("Usage: %s <search_string> <filename>\n", argv[0]);
        return 1;
    }

    char *search_string = argv[1];
    char *filename = argv[2];

    FILE *file = fopen(filename, "r");
    if (file == NULL) {
        perror("Error opening file");
        return 1;
    }

    char line[MAX_LINE_LENGTH];
    int line_number = 1;

    while (fgets(line, sizeof(line), file) != NULL) {
        if (strstr(line, search_string) != NULL) {
            printf("%s:%d: %s", filename, line_number, line);
        }
        line_number++;
    }

    fclose(file);
    return 0;
}

