#include <stdio.h>

int main(){
    int n;
    printf("Enter size of buffer: ");
    scanf("%d", &n);
    int buffer[n];
    int x = n + n/5;
    int result[x];
    int oneCount = 0;
    int ctrl = 0;
    printf("Enter input buffer: ");
    for(int i = 0; i < n; i++){
        scanf("%d", &buffer[i]);
    }
    for(int i = 0; i < n; i++){
        result[ctrl++] = buffer[i];
        if(buffer[i] == 1){
            oneCount++;
            if(oneCount == 5){
                result[ctrl++] = 0;
                oneCount = 0;
            }
        }else{
            oneCount = 0;
        }
    }
    printf("Result buffer: ");
    for(int i = 0; i < ctrl; i++){
        printf("%d ", result[i]);
    }
}