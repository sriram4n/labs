
#include <stdio.h>

#define BUCKET_SIZE 10

// Function to implement the Leaky Bucket Algorithm
void leakyBucket(int incoming[], int n, int outputRate)
{
    int bucketContent = 0;

    // Display table headings
    printf("\nTime\tIncoming\tBucket\tDropped\tOutgoing\tRemaining\n");

    // Process incoming packets at each time interval
    for (int i = 0; i < n; i++)
    {
        int accepted, dropped, sent;

        printf("%d\t%d\t\t", i + 1, incoming[i]);

        // Check whether incoming packets exceed bucket capacity
        if (bucketContent + incoming[i] > BUCKET_SIZE)
        {
            accepted = BUCKET_SIZE - bucketContent;
            dropped = incoming[i] - accepted;
            bucketContent += accepted;

            printf("%d\t%d\t", bucketContent, dropped);
        }
        else
        {
            // Accept all incoming packets
            bucketContent += incoming[i];

            printf("%d\t0\t", bucketContent);
        }

        // Send packets at the fixed output rate
        sent = (bucketContent < outputRate) ?
                bucketContent : outputRate;

        bucketContent -= sent;

        // Display outgoing packets and remaining packets
        printf("%d\t\t%d\n", sent, bucketContent);
    }

    // Empty the remaining bucket after incoming packets stop
    int i = n + 1;

    while (bucketContent > 0)
    {
        int sent = (bucketContent < outputRate) ?
                    bucketContent : outputRate;

        printf("%d\t0\t\t%d\t0\t%d\t\t%d\n",
               i, bucketContent, sent, bucketContent - sent);

        bucketContent -= sent;
        i++;
    }
}

int main()
{
    int n, outputRate;

    // Input the number of time intervals
    printf("\nEnter no. of time intervals: ");
    scanf("%d", &n);

    int incoming[n];

    // Input incoming packets at each interval
    printf("Enter incoming packets at each interval:\n");

    for (int i = 0; i < n; i++)
    {
        printf("Interval %d: ", i + 1);
        scanf("%d", &incoming[i]);
    }

    // Input the fixed output rate
    printf("Enter output rate: ");
    scanf("%d", &outputRate);

    // Call the Leaky Bucket function
    leakyBucket(incoming, n, outputRate);

    return 0;
}
