#include <stdio.h>
#include <string.h>

int main(){
    char sd, ed, input[50], output[100];
    // sd,ed =  delimeters
    printf("Enter starting delimeter: ");
    scanf(" %c", &sd);

    printf("Enter ending delimeter: ");
    scanf(" %c", &ed);

    printf("Enter string: ");
    scanf("%49s", input);

    int ctrl = 0;
    output[ctrl++] = sd;
    for(int i = 0; i < strlen(input); i++){
        if(input[i] == sd || input[i] == ed){
            output[ctrl++] = '\\';
        }
        output[ctrl++] = input[i];
    }
    output[ctrl++] = ed;
    output[ctrl] = '\0';
    printf("Final string: ");
    printf("%s",output);
}