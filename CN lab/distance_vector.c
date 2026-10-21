#include <stdio.h>

int main()
{
    printf("Enter no. of vertices: ");
    int n;
    scanf("%d", &n);

    printf("Enter no. of adj vertices: ");
    int adno;
    scanf("%d", &adno);

    printf("Enter source vertex no. and name: ");
    int svno;
    char svname;
    scanf("%d %c", &svno, &svname);

    int srcdelay[n];
    char adname[adno];
    for (int i = 0; i < adno; i++)
    {
        printf("\nEnter time delay and node name:");
        scanf("%d %c", &srcdelay[i], &adname[i]);
    }

    int neighbor_delay[adno][n];
    for (int i = 0; i < adno; i++)
    {
        printf("\nEnter time delay from %c to all other vertices", adname[i]);
        for (int j = 0; j < n; j++)
        {

            scanf(" %d", &neighbor_delay[i][j]);
        }
    }

    printf("delay via - vertex");
    for (int i = 0; i < n; i++)
    {
        int min = 30000;
        char next = '-';

        for (int j = 0; j < adno; j++)
        {
            if (min > srcdelay[j] + neighbor_delay[j][i])
            {
                min = srcdelay[j] + neighbor_delay[j][i];
                next = adname[j];
            }
        }

        if (i != svno - 1)
        {
            printf("\n %d %c", min, next);
        }
        else
        {
            printf("\n0 -");
        }
    }
}