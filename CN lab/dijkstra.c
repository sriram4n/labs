#include <stdio.h>

int main()
{
    int n;
    printf("Enter no. of vertices: ");
    scanf("%d", &n);
    int cost[n][n], path[n], distance[n], visited[n];
    int source = 0;
    printf("Enter adjacency matrix: ");
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            scanf("%d", &cost[i][j]);
        }
    }

    printf("Enter source vertex:");
    scanf("%d", &source);

    // initialize distance, path and visited
    for (int i = 0; i < n; i++)
    {
        visited[i] = 0;
        path[i] = source;
        distance[i] = cost[source][i];
    }
    distance[source] = 0;
    int current = -1;

    for (int i = 1; i < n; i++)
    {
        int minDist = 30000;
        // find minDist
        for (int j = 0; j < n; j++)
        {
            if (visited[j] != 1)
            {
                if (minDist > distance[j])
                {
                    minDist = distance[j];
                    current = j;
                }
            }
        }
        visited[current] = 1;

        // calc distance for remaining
        for (int j = 0; j < n; j++)
        {
            if (visited[j] != 1)
            {
                if (distance[j] > minDist + cost[current][j])
                {
                    distance[j] = minDist + cost[current][j];
                    path[j] = current;
                }
            }
        }
    }
    printf("Distance \t Node \t Path");
    // print
    for (int i = 0; i < n; i++)
    {
        int next = i;
        int steps = 0;

        printf("\n%d\t", distance[i]);
        printf("%d\t", i);
        printf("%d", i);
        while (next != source && steps < n)
        {
            next = path[next];
            printf(" <- %d", next);
            steps++;
        }
    }
}