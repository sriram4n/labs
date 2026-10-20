#include <stdio.h>

int main(){
    int n, window_size;

    printf("Enter no. of frames to transmit: ");
    scanf("%d", &n);

    int arr[n];

    printf("Enter window size: ");
    scanf("%d", &window_size);

    printf("Enter frames to transmit: ");
    for(int i = 0; i < n; i++){
        scanf("%d", &arr[i]);
    }

    printf("\nAfter sending %d frames, sender waits for acknowledgement from receiver\n", window_size);

    for(int i = 0; i < n; i++){
        printf("%d ", arr[i]);

        if((i + 1) % window_size == 0 || i == n - 1){
            printf("\nAck received;\n");
        }
    }

}