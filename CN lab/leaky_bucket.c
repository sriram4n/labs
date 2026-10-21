#include <stdio.h>

int main()
{
    int size = 10;

    printf("Enter no. of time intravels: ");
    int n;
    scanf("%d", &n);

    int incoming[n];
    printf("Enter incoming packets at each intravel\n");
    for (int i = 0; i < n; i++)
    {
        printf("Intravel %d", i);
        scanf("%d", &incoming[i]);
    }

    printf("Enter output rate: ");
    int rate;
    scanf("%d", &rate);

    printf("Time\t Input\t Bucket \t Dropped\t Output\t Remaining\t\n");

    int bucket = 0;
    for (int i = 0; i < n; i++)
    {
        int dropped = 0;

        if (bucket + incoming[i] > size)
        {
            dropped = bucket + incoming[i] - size;
            bucket = size;
        }
        else
        {
            bucket += incoming[i];
        }
        int sent = bucket > rate ? rate : bucket;
        bucket -= sent;
        printf("%d\t%d\t\t%d\t%d\t%d\t\t%d\n",
               i + 1, incoming[i], bucket + sent, dropped, sent, bucket); // print
    }
    int i = n;
    while (bucket > 0)
    {
        int sent = rate > bucket ? bucket : rate;
        bucket -= sent;

        printf("%d\t0\t\t%d\t0\t%d\t\t%d\n",
               i + 1, bucket + sent, sent, bucket);
        i++;
    }
}