#include <stdio.h>
#include <string.h>

int main()
{
    char gen[50], data[50], temp[50];
    printf("Enter gen: ");
    scanf("%s", &gen);
    printf("Enter data: ");
    scanf("%s", &data);

    int m = strlen(gen);
    int n = strlen(data);
    int start = 0;
    for (int i = 0; i < m; i++)
    {
        if (gen[i] == '1')
        {
            start = i;
            break;
        }
    }
    m -= start;
    for(int i = 0; i < m; i++){
        gen[i] = gen[start + i];
    }
    strcpy(temp, data);

    // xor
    for (int i = 0; i < n; i++)
    {
        if (temp[i] == '1')
        {
            for (int j = 0; j < m; j++)
            {
                if(temp[i+j] == gen[j]){
                    temp[i+j] = '0';
                }else{
                    temp[i+j] = '1';
                }
            }
        }
    }

    // check
    for(int i = 0; i < m+n-1; i++){
        if(temp[i] == '1'){
            printf("Invalid");
            return 0;
        }
    }
    printf("Valid");
}