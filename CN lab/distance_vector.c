
#include <stdio.h>
#include <conio.h>

void main()
{
    int nv, sn, road, min;
    int edel[20][20], tdel[20][20];
    char sv, adver[20], ch;

    clrscr();

    // Input number of vertices
    printf("\nEnter no. of vertices: ");
    scanf("%d", &nv);

    // Input source vertex number and name
    printf("\nEnter the source vertex no. and name: ");
    scanf("%d", &sn);
    fflush(stdin);
    sv = getchar();

    // Input number of adjacent vertices
    printf("\nEnter no. of adjacent vertices to vertex %c: ", sv);
    scanf("%d", &road);

    // Input delay and name of each adjacent vertex
    for (int i = 0; i < road; i++)
    {
        printf("\nEnter time delay and node name: ");
        scanf("%d %c", &edel[0][i], &adver[i]);
    }

    // Input delays from each adjacent vertex to all vertices
    for (int i = 0; i < road; i++)
    {
        printf("\nEnter time delay from %c to all other nodes: ",
               adver[i]);

        for (int j = 0; j < nv; j++)
        {
            scanf("%d", &tdel[i][j]);
        }
    }

    // Calculate minimum delay and next-hop vertex
    printf("\nDelay via - vertex\n");

    for (int i = 0; i < nv; i++)
    {
        min = 1000;
        ch = '-';

        for (int j = 0; j < road; j++)
        {
            if (min > (tdel[i][j] + edel[0][j]))
            {
                min = tdel[i][j] + edel[0][j];
                ch = adver[j];
            }
        }

        // Display the minimum delay and next hop
        if (i != sn - 1)
        {
            printf("\n%d %c", min, ch);
        }
        else
        {
            printf("\n0 -");
        }
    }

    getch();
}
