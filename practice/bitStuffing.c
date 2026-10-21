#include <stdio.h>

int main(){
    int n;
    printf("Enter size of frame: ");
    scanf("%d", &n);

    int frame[n];
    printf("Enter the frame bits: ");
    for(int i = 0; i < n; i++){
        scanf("%d", &frame[i]);
    }

    int output[n + n/5];
    int oneCount =0, ctrl = 0;
    for(int i = 0; i < n; i++){
        output[ctrl++] = frame[i];
        if(frame[i] == 1){
            oneCount++;
        }else{
            oneCount = 0;
        }
        if(oneCount == 5){
            output[ctrl++] = 0;
            oneCount = 0;
        }
    }
    printf("Transmitted frame: ");
    for(int i = 0; i < ctrl; i++){
        printf("%d ", output[i]);
    }
}