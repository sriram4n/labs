#include <stdio.h>
#include <stdlib.h>
typedef struct
{
    int frame_no;
    char data[20];
} Frame;
int compose(const void *a, const void *b)
{
    return ((Frame *)a)->frame_no - ((Frame *)b)->frame_no;
}
int main()
{

    printf("Enter no. of frames: ");
    int n;
    scanf("%d", &n);
    Frame buffer[n];

    printf("Enter Frame no. and data.\n");
    for (int i = 0; i < n; i++)
    {
        printf("Frame %d: ", i);
        printf("\n Frame no: ");
        scanf("%d", &buffer[i].frame_no);
        printf("\n Data: ");
        scanf("%s", &buffer[i].data);
    }

    qsort(buffer, n, sizeof(Frame), compose);

    printf("Sorted buffer: ");
    for (int i = 0; i < n; i++)
    {
        printf("\nFrame %d : %s", buffer[i].frame_no, buffer[i].data);
    }
}