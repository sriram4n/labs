#include <stdio.h>
#include <string.h>

void xorCipher(char * data, char key, int len){
    for(int i = 0; i < len; i++){
        data[i] = data[i] ^ key;
    }
}

int main(){
    printf("Enter text:");
    char text[30];
    scanf("%[^\n]", text);
    char key;
    printf("Enter single character as key: ");
    scanf(" %c", &key);
    int len = strlen(text);

    xorCipher(text, key , len);
    printf("Encrypted : %s", text);
    xorCipher(text, key, len);
    printf("\nDecrupteD: %s", text);
}