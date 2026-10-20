
#include <stdio.h>
#include <stdlib.h>

typedef struct
{
    int frame_no;
    char data[50];
} Frame;

int compose(const void *a, const void *b)
{
    return ((Frame *)a)->frame_no - ((Frame *)b)->frame_no;
}

int main()
{
    int n;

    printf("Enter the no. of frames required: ");
    scanf("%d", &n);

    Frame buffer[n];

    printf("Enter the frame number and data count of codes:\n");

    for (int i = 0; i < n; i++)
    {
        printf("Frame %d:", i);
        printf("\nFrame no.: ");
        scanf("%d", &buffer[i].frame_no);
        printf("\nData: ");
        scanf(" %c", &buffer[i].data);
    }

    qsort(buffer, n, sizeof(Frame), compose);

    printf("\nSorted frames:\n");

    for (int i = 0; i < n; i++)
    {
        printf("Frame %d: %s\n", buffer[i].frame_no, buffer[i].data);
    }

    return 0;
}
