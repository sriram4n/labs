#include <stdio.h>
#include <string.h>

int main(){
    char gen[50], frame[50], temp[100];
    
    printf("Enter gen: ");
    scanf("%s", &gen);
    printf("Enter frame: ");
    scanf("%s", &frame);

    int m = strlen(gen), n = strlen(frame), start = 0;
    // remove preceeding 0s 
    for(int i = 0; i < m; i++){
        if(gen[i] == '1'){
            start = i;
            break;
        }
    }
    m -= start;
    for(int i = 0; i < m; i++){
        gen[i] = gen[start + i];
    }
    // copy into temp and add 0s
    int end = m + n - 1;
    for(int i = 0; i < end; i++){
        if(i < n){
            temp[i] = frame[i];
        }else{
            temp[i] = '0';
        }
    }
    // perform xor on temp
    for(int i = 0; i < n; i++){
        if(temp[i] == '1'){
            for(int j = 0; j < m; j++){
                if(temp[i+j] == gen[j]){
                    temp[i+j] = '0';
                }else{
                    temp[i+j] = '1';
                }
            }
        }
    }
    temp[end] = '\0';
    // combine & print
    printf("The message is: %s", frame);
    for(int i = n; i < end; i++){
        printf("%c", temp[i]);
    }
}