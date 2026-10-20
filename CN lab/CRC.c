// take inputs, remove initial 0s, copy data and add 0s of len gen to temp, perform xor, combine result with gen and print gen

#include <stdio.h>
#include <string.h>

int main()
{
    char gen[50], data[50], temp[100];

    printf("Enter polynomial: ");
    scanf("%s", gen);

    printf("Enter the frame: ");
    scanf("%s", data);

    int m = strlen(gen);
    int n = strlen(data);

    // remove preceeding 0s
    int start = 0;
    for (int i = 0; i < m; i++)
    {
        if (gen[i] == '1')
        {
            start = i;
            break;
        }
    }
    m = m - start;
    for (int i = 0; i < m; i++)
    {
        gen[i] = gen[start + i];
    }

    // copy data into temp with 0s
    int ctrl = m + n - 1;
    for (int i = 0; i < ctrl; i++)
    {
        if (i < n)
        {
            temp[i] = data[i];
        }
        else
        {
            temp[i] = '0';
        }
    }
    temp[ctrl] = '\0';
    // perform xor on temp
    for (int i = 0; i < n; i++)
    {
        if (temp[i] == '1')
        {
            for (int j = 0; j < m; j++)
            {
                if (temp[i + j] == gen[j])
                {
                    temp[i + j] = '0';
                }
                else
                {
                    temp[i + j] = '1';
                }
            }
        }
    }

    // combine temp and data
    printf("The message is : %s", temp);
    for (int i = n; i < ctrl; i++)
    {
        printf("%c", temp[i]);
    }
}