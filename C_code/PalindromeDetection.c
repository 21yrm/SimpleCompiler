// #include <stdio.h>
// #include <stdbool.h> 
// include .h for running
size_t strlen(const char *_Str);
int printf( const char *restrict format, ... );
int scanf(const char *__format, ...);

int main() {
    char buffer[8192];
    scanf("%s", &buffer);
    bool flag = true;
    for (int i = 0; i < strlen(buffer) / 2; i++)
        if (buffer[i] != buffer[strlen(buffer) - i - 1]) {
            flag = false;
            break;
        }
    if (flag)
        printf("input string is palindrome\n");
    else 
        printf("input string is not palindrome\n");
    return 0;
}