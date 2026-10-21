#include <stdio.h>

int main()
{
    printf("Enter no. of vertices: ");
    int n, source;
    scanf("%d", &n);
    int cost[n][n], visited[n], path[n], distance[n];
    printf("Enter adjacency matrix: ");
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            scanf("%d", &cost[i][j]);
        }
    }
    printf("Enter source vertex: ");
    scanf("%d", &source);
    // diagonals
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (i == j)
            {
                cost[i][j] = 0;
            }
            if (cost[i][j] < 0)
            {
                cost[i][j] = 30000;
            }
        }
    }
    // initialize
    for (int i = 0; i < n; i++)
    {
        visited[i] = 0;
        path[i] = source;
        distance[i] = cost[source][i];
    }
    distance[source] = 0;
    int current = -1;
    for (int j = 1; j < n; j++)
    {
        int minDist = 30000;

        for (int i = 0; i < n; i++)
        {
            if (visited[i] != 1)
            {
                if (minDist > distance[i])
                {
                    minDist = distance[i];
                    current = i;
                }
            }
        }
        visited[current] = 1;

        for (int i = 0; i < n; i++)
        {
            if (visited[i] != 1)
            {
                if(distance[i] > minDist + cost[current][i]){
                    distance[i] = minDist + cost[current][i];
                    path[i] = current;
                }
            }
        }
    }
    // print
    printf("Distance Node\t\t Path\n");

    for(int i = 0; i < n; i++){
        printf("\n%d\t",distance[i]);
        printf("%d\t\t",i);
        printf("%d",i);
        int next = i;
        int count = 0;
        while(next != source && count < n){
            next = path[next];
            printf("<- %d", next);
            count++;
        }
    }
}