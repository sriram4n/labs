#include <stdio.h>

int main(){
    int n, buffer_size;
    printf("Enter no. of frames to transmit: ");
    scanf("%d",&n);
    printf("Enter buffer size: ");
    scanf("%d", &buffer_size);

    int arr[n];
    printf("Enter the frames: ");
    for(int i =0; i< n; i++){
        scanf("%d", &arr[i]);
    }

    for(int i = 0; i < n; i++){
        printf("%d", arr[i]);
        if((i+1) % buffer_size == 0 || i == n-1){
            printf("\nAcknowledgement of above frames recieved\n");
        }
    }
}