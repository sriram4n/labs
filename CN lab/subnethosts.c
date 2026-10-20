#include <stdio.h>

int a[10][10], visited[10], n;

void spanning_tree(int root)
{
    int queue[10], front = 0, rear = 0;

    queue[rear++] = root;
    visited[root] = 1;

    printf("\nSpanning Tree\n");

    while (front < rear)
    {
        int k = queue[front++];

        for (int i = 0; i < n; i++)
        {
            if (a[k][i] == 1 && visited[i] == 0)
            {
                visited[i] = 1;
                queue[rear++] = i;
                printf("%d -> %d\n", k + 1, i + 1);
            }
        }
    }
}

int main()
{
    printf("Enter no. of hosts: ");
    scanf("%d", &n);

    printf("Enter adjacency matrix: ");
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            scanf("%d", &a[i][j]);
        }
        visited[i] = 0;
    }

    printf("Enter root host (0 to %d): ", n - 1);
    int root;
    scanf("%d", &root);

    spanning_tree(root);

    return 0;
}