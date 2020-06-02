#include<stdio.h>
int main()
{
    FILE *p;
    int c=1;
    p=fopen("D:/MSc/SEM - 1/MTL 505(C)/Tutorials/tut 4 solutions/q3.txt","r");  /* forword slash is used */
    if(p==NULL)
        printf("File not exist ");
    else
        printf("File opened successfully");

    while(c!=EOF)
    {
        printf("%c",c);
        c=fgetc(p);
    }
    return 0;
}
