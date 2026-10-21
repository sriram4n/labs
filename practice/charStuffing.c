#include <stdio.h>
#include <string.h>

int main(){
    char sd, ed, string[40];
    printf("Enter strating delimiter: ");
    scanf(" %c", &sd);

    printf("Enter ending delimiter: ");
    scanf(" %c", &ed);

    printf("Enter string to be stuffed: ");
    scanf("%s", &string);

    int n = strlen(string);
    char output[80];
    int ctrl = 0;
    for(int i =0; i < n; i++){
        if(string[i] == sd || string[i] == ed){
            output[ctrl++] = '\\';
        }
        output[ctrl++] = string[i];
    }
    printf("Stuffed string: ");
    printf("%c", sd);
    for(int i = 0; i < ctrl; i++){
        printf("%c", output[i]);
    }   
    printf("%c", ed);
}