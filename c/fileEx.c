#include<stdio.h>
int main()
{
    FILE *p;
    p=fopen("D:/NBHM/msc05.pdf","r");  /* forword slash is used */
    if(p==NULL)
        printf("File not exist ");
    else
        printf("File opened successfully");
    return 0;
}
