#include <string.h>
#include <stdio.h>
void xorCipher(char *data, char key, int len){
    for(int i = 0;i < len; i++){
        data[i] = data[i] ^ key;
    }
}

int main(){
    printf("Enter data: ");
    char ch[40];
    scanf("%[^\n]", ch);
    int n = strlen(ch);
    printf("Enter key: ");
    char key;
    scanf(" %c", &key);

    printf("Encrypted data: ");
    xorCipher(ch, key, n);
    for(int i = 0; i < n; i++){
        printf("%c", ch[i]);
    }
    printf("\nDecrypted data: ");
    xorCipher(ch, key, n);
    for(int i = 0; i < n; i++){
        printf("%c", ch[i]);
    }
}