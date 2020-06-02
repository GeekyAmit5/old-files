#include <stdio.h>

int main()
{
    int x,y,i;
    printf("Enter the Upper Bound : ");
    scanf("%d",&x);
    printf("Enter the Lower Bound : ");
    scanf("%d",&y);
    printf("The Prime Numbers From %d to %d Are : \n",x,y);
    for(i=x;i<=y;i++)
    {
        if(pc(i)==i)
        printf("%d\n",i);
    }
    return 0;
}
pc(x)
int x;
{
    int j;
    for(j=2;j<=x;j++)
    {
        if(x%j==0)
        break;
    }
    return j;
}
